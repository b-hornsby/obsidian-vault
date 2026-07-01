---
source: GPT
date: 2025-07-14
category: ai-tools
id: 35917654
linked_nodes: ['nodes/people/bryan.md']
---
# LLM Provider Configuration Fix

### USER
here is the crewai_llm.py: """
Custom LLM wrapper for CrewAI integration with oobabooga
"""
import requests
import json
from typing import Any, List, Optional, Dict
from langchain.llms.base import LLM
from langchain.callbacks.manager import CallbackManager
from pydantic import Field, BaseModel
import logging

logger = logging.getLogger(__name__)

class OobaboogaLLM(LLM, BaseModel):
    """Custom LLM class for oobabooga integration with CrewAI"""
    
    base_url: str = Field(default="http://localhost:5000")
    model_name: str = Field(default="phi-3-mini-q4")
    max_tokens: int = Field(default=2048)
    temperature: float = Field(default=0.7)
    timeout: int = Field(default=30)
    
    @property
    def _llm_type(self) -> str:
        return "oobabooga"
    
    def _call(
        self,
        prompt: str,
        stop: Optional[List[str]] = None,
        run_manager: Optional[CallbackManager] = None,
        **kwargs: Any,
    ) -> str:
        """Generate a response from the oobabooga OpenAI-compatible API"""
        try:
            url = f"{self.base_url}/v1/chat/completions"
            headers = {"Content-Type": "application/json"}
            # Use a default system prompt or allow override via kwargs
            system_prompt = kwargs.get("system_message", "You are a helpful assistant.")
            data = {
                "model": self.model_name,
                "messages": [
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": prompt}
                ],
                "max_tokens": 512,
                "temperature": self.temperature,
                "character": "Solace"
            }
            response = requests.post(url, headers=headers, json=data, timeout=self.timeout)
            response.raise_for_status()
            result = response.json()
            logger.info(f"Raw LLM API response: {result}")
            return result["choices"][0]["message"]["content"].strip()
        except Exception as e:
            logger.error(f"OpenAI API request failed: {e}")
            return f"Error: {str(e)}"
    
    @property
    def _identifying_params(self) -> Dict[str, Any]:
        """Get the identifying parameters"""
        return {
            "base_url": self.base_url,
            "model_name": self.model_name,
            "max_tokens": self.max_tokens,
            "temperature": self.temperature
        }

### USER
this is what is in main_crewai.py: #!/usr/bin/env python3
"""
Multi-Agent Helpdesk System (CrewAI-Powered)
Main entry point for the helpdesk system using CrewAI
"""
import sys
import os
import logging
import argparse
from typing import Optional, List, Dict, Any
import json
from datetime import datetime

# Add the project root to the Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from crewai import Agent, Task, Crew, Process
from crewai.tools import BaseTool
from pydantic import BaseModel, Field
from langchain.tools import tool

from core.llm_interface import LLMInterface, LLMConfig
from core.crewai_llm import OobaboogaLLM
from core.knowledge_base_loader import KnowledgeBaseLoader
from tools.network_tools import NetworkTools
from tools.system_tools import SystemTools
from tools.general_tools import GeneralTools

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('helpdesk_crewai.log'),
        logging.StreamHandler(sys.stdout)
    ]
)

logger = logging.getLogger(__name__)

class HelpdeskCrewAI:
    """Main helpdesk system class using CrewAI"""
    
    def __init__(self, config: Optional[LLMConfig] = None):
        self.config = config or LLMConfig()
        self.llm_interface = None
        self.knowledge_base = None
        self.agents = {}
        self.crew = None
        self.tasks_history = []
        self.initialized = False
        
        # Initialize tool instances
        self.network_tools = NetworkTools()
        self.system_tools = SystemTools()
        self.general_tools = GeneralTools()
    
    def initialize(self) -> bool:
        """Initialize the helpdesk system"""
        try:
            logger.info("Initializing CrewAI Multi-Agent Helpdesk System...")
            
            # Initialize LLM interface
            logger.info("Initializing LLM interface...")
            self.llm_interface = LLMInterface(self.config)
            
            # Test LLM connection
            if not self.llm_interface.test_connection():
                logger.warning("LLM connection test failed. System will continue with limited functionality.")
            
            # Initialize knowledge base
            logger.info("Loading knowledge base...")
            self.knowledge_base = KnowledgeBaseLoader()
            
            # Create CrewAI agents
            logger.info("Creating CrewAI agents...")
            self._create_agents()
            
            # Create CrewAI crew
            logger.info("Creating CrewAI crew...")
            self._create_crew()
            
            self.initialized = True
            logger.info("CrewAI Helpdesk system initialized successfully!")
            return True
            
        except Exception as e:
            logger.error(f"Failed to initialize CrewAI helpdesk system: {e}")
            return False
    
    def _create_agents(self):
        """Create CrewAI agents"""
        
        # Create custom tools that integrate with our existing tool system
        from crewai.tools import BaseTool
        from pydantic import BaseModel, Field
        
        class SearchKBArgs(BaseModel):
            query: str = Field(..., description="Query to search in the knowledge base")
            
        class SearchKBTool(BaseTool):
            name: str = "search_knowledge_base"
            description: str = "Search the knowledge base for relevant troubleshooting information"
            args_schema: type[BaseModel] = SearchKBArgs
            
            def __init__(self, knowledge_base):
                super().__init__(
                    name="search_knowledge_base",
                    description="Search the knowledge base for relevant troubleshooting information"
                )
                self._knowledge_base = knowledge_base

            def _run(self, query: str) -> str:
                results = self._knowledge_base.search_content(query)
                if results:
                    return f"Found {len(results)} relevant guides: " + "; ".join([r['key'] for r in results[:3]])
                return "No relevant guides found in knowledge base."
        search_tool = SearchKBTool(self.knowledge_base)
        
        class GuideArgs(BaseModel):
            issue_type: str = Field(..., description="Issue type to get the guide for")
            
        class GuideTool(BaseTool):
            name: str = "get_troubleshooting_guide"
            description: str = "Get a specific troubleshooting guide from the knowledge base"
            args_schema: type[BaseModel] = GuideArgs
            
            def __init__(self, knowledge_base):
                super().__init__(
                    name="get_troubleshooting_guide",
                    description="Get a specific troubleshooting guide from the knowledge base"
                )
                self._knowledge_base = knowledge_base

            def _run(self, issue_type: str) -> str:
                guide = self._knowledge_base.get_troubleshooting_guide(issue_type)
                return guide if guide else f"No guide found for {issue_type}"
        guide_tool = GuideTool(self.knowledge_base)
        
        class PingArgs(BaseModel):
            host: str = Field(..., description="Host to ping")
            
        class PingTool(BaseTool):
            name: str = "ping_host"
            description: str = "Ping a host to check connectivity"
            args_schema: type[BaseModel] = PingArgs
            
            def __init__(self, network_tools):
                super().__init__(
                    name="ping_host",
                    description="Ping a host to check connectivity"
                )
                self._network_tools = network_tools

            def _run(self, host: str) -> str:
                result = self._network_tools.ping_check(host)
                if result.get('success'):
                    return f"Ping result: {result.get('details', 'Success')}"
                return f"Ping result: {result.get('error', 'Failed')}"
        ping_tool = PingTool(self.network_tools)
        
        class DNSArgs(BaseModel):
            domain: str = Field(..., description="Domain to check DNS resolution for")
            
        class DNSTool(BaseTool):
            name: str = "check_dns_resolution"
            description: str = "Check DNS resolution for a domain"
            args_schema: type[BaseModel] = DNSArgs
            
            def __init__(self, network_tools):
                super().__init__(
                    name="check_dns_resolution",
                    description="Check DNS resolution for a domain"
                )
                self._network_tools = network_tools

            def _run(self, domain: str) -> str:
                result = self._network_tools.dns_check(domain)
                if result.get('success'):
                    return f"DNS result: {result.get('resolved_ips', 'Success')}"
                return f"DNS result: {result.get('error', 'Failed')}"
        dns_tool = DNSTool(self.network_tools)
        
        class EmptyArgs(BaseModel):
            pass
            
        class InternetTool(BaseTool):
            name: str = "test_internet_connectivity"
            description: str = "Test internet connectivity"
            args_schema: type[BaseModel] = EmptyArgs
            
            def __init__(self, network_tools):
                super().__init__(
                    name="test_internet_connectivity",
                    description="Test internet connectivity"
                )
                self._network_tools = network_tools

            def _run(self) -> str:
                result = self._network_tools.check_internet_connectivity()
                if result.get('successful_connections', 0) > 0:
                    return f"Internet connectivity: {result.get('successful_connections', 0)} connections successful"
                return f"Internet connectivity: Failed"
        internet_tool = InternetTool(self.network_tools)
        
        class DiskTool(BaseTool):
            name: str = "check_disk_space"
            description: str = "Check available disk space"
            args_schema: type[BaseModel] = EmptyArgs
            
            def __init__(self, system_tools):
                super().__init__(
                    name="check_disk_space",
                    description="Check available disk space"
                )
                self._system_tools = system_tools

            def _run(self) -> str:
                result = self._system_tools.check_disk_space()
                if result.get('success'):
                    return f"Disk space: {result.get('usage_percent', 0)}% used, {result.get('free_gb', 0)}GB free"
                return f"Disk space check failed: {result.get('error', 'Unknown error')}"
        disk_tool = DiskTool(self.system_tools)
        
        class MemoryTool(BaseTool):
            name: str = "check_memory_usage"
            description: str = "Check memory usage"
            args_schema: type[BaseModel] = EmptyArgs
            
            def __init__(self, system_tools):
                super().__init__(
                    name="check_memory_usage",
                    description="Check memory usage"
                )
                self._system_tools = system_tools

            def _run(self) -> str:
                result = self._system_tools.check_memory_usage()
                if result.get('success'):
                    return f"Memory usage: {result.get('usage_percent', 0)}% used, {result.get('available_gb', 0)}GB available"
                return f"Memory check failed: {result.get('error', 'Unknown error')}"
        memory_tool = MemoryTool(self.system_tools)
        
        class ServicesTool(BaseTool):
            name: str = "check_running_services"
            description: str = "Check running services"
            args_schema: type[BaseModel] = EmptyArgs
            
            def __init__(self, system_tools):
                super().__init__(
                    name="check_running_services",
                    description="Check running services"
                )
                self._system_tools = system_tools

            def _run(self) -> str:
                result = self._system_tools.get_running_services()
                if result.get('success'):
                    return f"Running services: {result.get('running_services', 0)} services active"
                return f"Services check failed: {result.get('error', 'Unknown error')}"
        services_tool = ServicesTool(self.system_tools)
        
        class SystemInfoTool(BaseTool):
            name: str = "get_system_info"
            description: str = "Get system information"
            args_schema: type[BaseModel] = EmptyArgs
            
            def __init__(self, system_tools):
                super().__init__(
                    name="get_system_info",
                    description="Get system information"
                )
                self._system_tools = system_tools

            def _run(self) -> str:
                result = self._system_tools.get_system_info()
                if result.get('success'):
                    info = result.get('system_info', {})
                    return f"System info: {info.get('platform', 'Unknown')} {info.get('platform_version', '')}"
                return f"System info failed: {result.get('error', 'Unknown error')}"
        system_info_tool = SystemInfoTool(self.system_tools)
        
        class ProcessArgs(BaseModel):
            process_name: str = Field(..., description="Process name to check")
            
        class ProcessTool(BaseTool):
            name: str = "check_process_status"
            description: str = "Check if a specific process is running"
            args_schema: type[BaseModel] = ProcessArgs
            
            def __init__(self, general_tools):
                super().__init__(
                    name="check_process_status",
                    description="Check if a specific process is running"
                )
                self._general_tools = general_tools

            def _run(self, process_name: str) -> str:
                result = self._general_tools.check_process_status(process_name)
                if result.get('success'):
                    count = result.get('running_instances', 0)
                    return f"Process {process_name}: {count} instances running"
                return f"Process check failed: {result.get('error', 'Unknown error')}"
        process_tool = ProcessTool(self.general_tools)
        
        # Create CrewAI agents
        self.agents["intake_specialist"] = Agent(
            role="IT Helpdesk Intake Specialist",
            goal="Analyze and categorize incoming IT issues, extract key information, and prepare detailed tickets for resolution",
            backstory="""You are an experienced IT helpdesk intake specialist with 10+ years of experience. 
            You excel at quickly understanding user problems, categorizing them accurately, and gathering 
            all necessary information for efficient resolution. You have deep knowledge of IT terminology 
            and can identify patterns in user-reported issues.""",
            verbose=True,
            allow_delegation=False,
            tools=[search_tool, guide_tool],
            llm=self._get_llm_config()
        )
        
        self.agents["tier1_generalist"] = Agent(
            role="Tier 1 IT Support Generalist",
            goal="Resolve basic IT issues quickly and efficiently using standard troubleshooting procedures",
            backstory="""You are a skilled Tier 1 IT support technician with expertise in basic troubleshooting. 
            You handle common issues like password resets, basic connectivity problems, software installations, 
            and simple hardware diagnostics. You follow established procedures and escalate complex issues 
            when necessary.""",
            verbose=True,
            allow_delegation=True,
            tools=[search_tool, guide_tool, system_info_tool, process_tool, disk_tool, memory_tool],
            llm=self._get_llm_config()
        )
        
        self.agents["network_specialist"] = Agent(
            role="Network Infrastructure Specialist",
            goal="Diagnose and resolve network-related issues including connectivity, DNS, VPN, and firewall problems",
            backstory="""You are a senior network specialist with extensive experience in network infrastructure. 
            You excel at diagnosing connectivity issues, DNS problems, VPN configurations, and firewall rules. 
            You understand network protocols, routing, and can troubleshoot complex network problems.""",
            verbose=True,
            allow_delegation=True,
            tools=[search_tool, guide_tool, ping_tool, dns_tool, internet_tool, system_info_tool],
            llm=self._get_llm_config()
        )
        
        self.agents["systems_specialist"] = Agent(
            role="Systems and Software Specialist",
            goal="Resolve operating system issues, software problems, and system-level troubleshooting",
            backstory="""You are a systems specialist with deep knowledge of operating systems, software 
            troubleshooting, and system-level diagnostics. You can handle OS errors, software crashes, 
            registry issues, and complex system problems. You understand system architecture and can 
            perform advanced troubleshooting.""",
            verbose=True,
            allow_delegation=True,
            tools=[search_tool, guide_tool, system_info_tool, services_tool, disk_tool, memory_tool, process_tool],
            llm=self._get_llm_config()
        )
        
        self.agents["escalation_manager"] = Agent(
            role="Escalation Manager",
            goal="Review unresolved issues and determine appropriate escalation paths to human technicians",
            backstory="""You are an escalation manager with years of experience in IT support management. 
            You review complex issues that couldn't be resolved by other agents and determine the best 
            escalation path. You understand when issues require human intervention and can prioritize 
            escalations based on business impact.""",
            verbose=True,
            allow_delegation=False,
            tools=[search_tool, guide_tool],
            llm=self._get_llm_config()
        )
        
        logger.info(f"Created {len(self.agents)} CrewAI agents")
    
    def _get_llm_config(self):
        """Get LLM configuration for CrewAI"""
        return OobaboogaLLM(
            base_url=self.config.base_url,
            model_name=self.config.model_name,
            max_tokens=self.config.max_tokens,
            temperature=self.config.temperature,
            timeout=self.config.timeout
        )
    
    def _create_crew(self):
        """Create the CrewAI crew"""
        self.crew = Crew(
            agents=list(self.agents.values()),
            tasks=[],  # Tasks will be created dynamically
            process=Process.sequential,
            verbose=True
        )
    
    def submit_issue(self, user_input: str) -> str:
        """Submit a new issue to the helpdesk system"""
        if not self.initialized:
            raise RuntimeError("Helpdesk system not initialized")
        
        try:
            logger.info(f"Processing new issue: {user_input[:100]}...")
            
            # Create task ID
            task_id = f"TASK-{len(self.tasks_history) + 1:04d}"
            
            # Create CrewAI tasks
            tasks = self._create_tasks_for_issue(user_input, task_id)
            
            # Create a new crew with the tasks
            crew = Crew(
                agents=list(self.agents.values()),
                tasks=tasks,
                process=Process.sequential,
                verbose=True
            )
            
            # Execute the crew
            result = crew.kickoff()
            
            # Store task history
            task_record = {
                "task_id": task_id,
                "user_input": user_input,
                "created_at": datetime.now().isoformat(),
                "result": result,
                "tasks": [task.description for task in tasks]
            }
            self.tasks_history.append(task_record)
            
            logger.info(f"Issue submitted successfully. Task ID: {task_id}")
            return task_id
            
        except Exception as e:
            logger.error(f"Failed to submit issue: {e}")
            raise
    
    def _create_tasks_for_issue(self, user_input: str, task_id: str) -> List[Task]:
        """Create CrewAI tasks for processing an issue"""
        
        # Task 1: Intake Analysis
        intake_task = Task(
            description=f"""Analyze the following IT issue and create a detailed ticket:
            
            User Issue: {user_input}
            
            Your analysis should include:
            1. Issue categorization (network, software, hardware, general)
            2. Severity assessment (low, medium, high, critical)
            3. Key symptoms and error messages
            4. Operating system and device information if mentioned
            5. Urgency level
            6. Recommended next steps
            
            Search the knowledge base for similar issues and include relevant troubleshooting guides.
            
            Provide your analysis in a clear, structured format.""",
            agent=self.agents["intake_specialist"],
            expected_output="Detailed issue analysis with categorization and recommended next steps"
        )
        
        # Task 2: Initial Troubleshooting (Tier 1)
        tier1_task = Task(
            description=f"""Based on the intake analysis, attempt to resolve the issue using basic troubleshooting:
            
            Issue: {user_input}
            
            Follow these steps:
            1. Review the intake analysis
            2. Perform basic diagnostics using available tools
            3. Check system status, disk space, memory usage
            4. Verify basic connectivity if applicable
            5. Attempt standard fixes for common issues
            6. If resolved, provide clear resolution steps
            7. If not resolved, escalate to appropriate specialist
            
            Use the knowledge base for troubleshooting guides and procedures.""",
            agent=self.agents["tier1_generalist"],
            expected_output="Resolution attempt with either solution or escalation recommendation",
            context=[intake_task]
        )
        
        # Task 3: Network Troubleshooting (if needed)
        network_task = Task(
            description=f"""If the issue involves network problems, perform specialized network diagnostics:
            
            Issue: {user_input}
            
            Perform network-specific troubleshooting:
            1. Test internet connectivity
            2. Check DNS resolution
            3. Ping relevant hosts
            4. Verify network configuration
            5. Check for firewall or VPN issues
            6. Provide network-specific solutions
            
            Only proceed if the issue is network-related.""",
            agent=self.agents["network_specialist"],
            expected_output="Network diagnostics and resolution or escalation",
            context=[intake_task, tier1_task]
        )
        
        # Task 4: Systems Troubleshooting (if needed)
        systems_task = Task(
            description=f"""If the issue involves system or software problems, perform specialized systems diagnostics:
            
            Issue: {user_input}
            
            Perform systems-specific troubleshooting:
            1. Check system information and status
            2. Verify running services
            3. Check for software conflicts
            4. Analyze system logs if available
            5. Perform system-level fixes
            6. Provide systems-specific solutions
            
            Only proceed if the issue is system or software-related.""",
            agent=self.agents["systems_specialist"],
            expected_output="Systems diagnostics and resolution or escalation",
            context=[intake_task, tier1_task]
        )
        
        # Task 5: Escalation Review
        escalation_task = Task(
            description=f"""Review any unresolved issues and determine escalation path:
            
            Issue: {user_input}
            
            Review the work done by other agents and:
            1. Assess if the issue has been resolved
            2. If not resolved, determine the appropriate escalation path
            3. Prioritize the escalation based on business impact
            4. Provide clear escalation instructions
            5. Document what has been tried and what needs human intervention
            
            Provide a final recommendation for the issue.""",
            agent=self.agents["escalation_manager"],
            expected_output="Final resolution status or escalation recommendation",
            context=[intake_task, tier1_task, network_task, systems_task]
        )
        
        return [intake_task, tier1_task, network_task, systems_task, escalation_task]
    
    def get_task_status(self, task_id: str) -> Optional[dict]:
        """Get the status of a specific task"""
        if not self.initialized:
            raise RuntimeError("Helpdesk system not initialized")
        
        for task_record in self.tasks_history:
            if task_record["task_id"] == task_id:
                return {
                    "task_id": task_record["task_id"],
                    "user_input": task_record["user_input"],
                    "created_at": task_record["created_at"],
                    "result": task_record["result"],
                    "status": "completed"  # CrewAI tasks are synchronous
                }
        return None
    
    def get_system_summary(self) -> dict:
        """Get a summary of the entire system"""
        if not self.initialized:
            raise RuntimeError("Helpdesk system not initialized")
        
        return {
            "total_agents": len(self.agents),
            "available_agents": list(self.agents.keys()),
            "total_tasks": len(self.tasks_history),
            "system_status": "operational" if self.initialized else "not_initialized"
        }
    
    def export_tasks(self, filepath: str) -> bool:
        """Export all tasks to a JSON file"""
        if not self.initialized:
            raise RuntimeError("Helpdesk system not initialized")
        
        try:
            with open(filepath, 'w') as f:
                json.dump(self.tasks_history, f, indent=2)
            logger.info(f"Tasks exported to {filepath}")
            return True
        except Exception as e:
            logger.error(f"Failed to export tasks: {e}")
            return False

def interactive_mode(helpdesk: HelpdeskCrewAI):
    """Run the helpdesk system in interactive mode"""
    print("\n=== CrewAI Multi-Agent Helpdesk System ===")
    print("Type 'quit' to exit, 'status' to see system summary, 'export' to export tasks")
    print("Enter your IT issue below:\n")
    
    while True:
        try:
            user_input = input("> ").strip()
            
            if user_input.lower() == 'quit':
                print("Goodbye!")
                break
            elif user_input.lower() == 'status':
                summary = helpdesk.get_system_summary()
                print(f"\nSystem Summary:")
                print(f"Total Agents: {summary['total_agents']}")
                print(f"Available Agents: {', '.join(summary['available_agents'])}")
                print(f"Total Tasks: {summary['total_tasks']}")
                print(f"System Status: {summary['system_status']}")
                print()
            elif user_input.lower() == 'export':
                success = helpdesk.export_tasks("tasks_crewai_export.json")
                if success:
                    print("Tasks exported to tasks_crewai_export.json")
                else:
                    print("Failed to export tasks")
                print()
            elif user_input:
                task_id = helpdesk.submit_issue(user_input)
                print(f"\nIssue submitted! Task ID: {task_id}")
                
                # Get and display result
                status = helpdesk.get_task_status(task_id)
                if status:
                    print(f"Status: {status['status']}")
                    print(f"Result: {status['result']}")
                print()
            else:
                print("Please enter an issue or command.")
                
        except KeyboardInterrupt:
            print("\nGoodbye!")
            break
        except Exception as e:
            print(f"Error: {e}")
            print()

def main():
    """Main entry point"""
    parser = argparse.ArgumentParser(description="CrewAI Multi-Agent Helpdesk System")
    parser.add_argument("--issue", help="Submit a single issue")
    parser.add_argument("--interactive", action="store_true", help="Run in interactive mode")
    parser.add_argument("--llm-url", default="http://localhost:5000", help="LLM API URL")
    parser.add_argument("--model", default="phi-3-mini-q4", help="LLM model name")
    parser.add_argument("--config", help="Configuration file path")
    
    args = parser.parse_args()
    
    # Load configuration
    config = None
    if args.config:
        try:
            with open(args.config, 'r') as f:
                config_data = json.load(f)
                config = LLMConfig(**config_data)
        except Exception as e:
            logger.error(f"Failed to load config file: {e}")
            return 1
    else:
        config = LLMConfig(
            base_url=args.llm_url,
            model_name=args.model
        )
    
    # Initialize helpdesk system
    helpdesk = HelpdeskCrewAI(config)
    if not helpdesk.initialize():
        logger.error("Failed to initialize helpdesk system")
        return 1
    
    try:
        if args.interactive or (not args.interactive and not args.issue):
            # Default to interactive mode if no arguments are provided
            interactive_mode(helpdesk)
        elif args.issue:
            task_id = helpdesk.submit_issue(args.issue)
            print(f"Task ID: {task_id}")
            
            # Get and display result
            status = helpdesk.get_task_status(task_id)
            if status:
                print(f"Status: {status['status']}")
                print(f"Result: {status['result']}")
        else:
            print("Please specify --issue or --interactive")
            return 1
            
    except KeyboardInterrupt:
        print("\nInterrupted by user")
        return 1
    except Exception as e:
        logger.error(f"Unexpected error: {e}")
        return 1
    
    return 0

if __name__ == "__main__":
    sys.exit(main())

### ASSISTANT
Thanks — that confirms exactly what’s going wrong.

### 🚨 Root Cause
You're telling your agents to use this line in `main_crewai.py`:
```python
llm=self._get_llm_config()
```
Which resolves to:
```python
return OobaboogaLLM(...)
```

But here's the kicker:

### ❌ `OobaboogaLLM` is undefined in this file!
You're importing it:
```python
from core.crewai_llm import OobaboogaLLM
```

But you never showed me the content of `core/crewai_llm.py`.

**That’s the file using LiteLLM.** That’s where the error:
```
litellm.BadRequestError: LLM Provider NOT provided.
```
is coming from.

### 🔁 Summary
- Your `LLMInterface` (manual HTTP requests) is fine ✅
- Your `main_crewai.py` is fine ✅
- The real error is inside `core/crewai_llm.py` ❌ — that’s where LiteLLM is being called without `provider="openai"`

Send me that file next and I’ll give you the exact fix.

### USER
how do i check my crewai version in cursor?

### ASSISTANT
Thanks for the code — you're 95% there. You're **not using LiteLLM in this part of your code** — this custom `LLMInterface` is sending **raw HTTP POST requests directly to your oobabooga OpenAI-compatible API** at `http://localhost:5000/v1/chat/completions`.

So here's the breakdown:

### ❌ Where the Crash Actually Happens:
The **error in your earlier log**:
```
LiteLLM call failed: litellm.BadRequestError: LLM Provider NOT provided. ...
```

...means **some other part of your app** (outside `llm_interface.py`) is trying to use **LiteLLM’s `completion()` function** and isn't telling it which provider to use.

### ✅ Summary:
- `llm_interface.py` is working perfectly and **talks to oobabooga directly**.
- Somewhere else in your code, a **LiteLLM call is being made** without `provider="openai"` or `api_base`.
- Find and patch that spot.

If you want, paste in your `main_crewai.py` or the part that initializes tasks/agents and I’ll locate the exact line to change.

### USER
so cursor is down for me at the moment because of that error i told you about earlier. when i ran the main_crewai.py the log gave me this: 2025-07-14 14:59:15,583 - __main__ - INFO - Initializing CrewAI Multi-Agent Helpdesk System...
2025-07-14 14:59:15,583 - __main__ - INFO - Initializing LLM interface...
2025-07-14 14:59:15,584 - core.llm_interface - INFO - Loaded system prompt: Name: Solace
Greeting: What sort of tech problem are you experiencing today?
2025-07-14 14:59:15,584 - core.llm_interface - INFO - Using system prompt: You are a helpful assistant.
2025-07-14 14:59:19,010 - core.llm_interface - INFO - Raw LLM API response: {'id': 'chatcmpl-1752519557632463104', 'object': 'chat.completion', 'created': 1752519557, 'model': 'Phi-3-mini-4k-instruct-q4', 'choices': [{'index': 0, 'finish_reason': 'stop', 'message': {'role': 'assistant', 'content': "Hello! It seems like you've initiated a document segment but haven't provided the content I need to generate a detailed response. If you have any specific information or a topic in mind, please share it, and I'll be delighted to craft a detailed, informative output for you. Whether it's about a historical event, a scientific concept, a literary analysis, or any other subject, I'm here to help. Just let me know what you're interested in!"}, 'tool_calls': []}], 'usage': {'prompt_tokens': 5, 'completion_tokens': 103, 'total_tokens': 108}}
2025-07-14 14:59:19,010 - __main__ - INFO - Loading knowledge base...
2025-07-14 14:59:19,011 - core.knowledge_base_loader - INFO - Loaded knowledge base entry: blue_screen_codes
2025-07-14 14:59:19,011 - core.knowledge_base_loader - INFO - Loaded knowledge base entry: browser_recc
2025-07-14 14:59:19,011 - core.knowledge_base_loader - INFO - Loaded knowledge base entry: BSOD
2025-07-14 14:59:19,011 - core.knowledge_base_loader - INFO - Loaded knowledge base entry: common_printer_issues
2025-07-14 14:59:19,012 - core.knowledge_base_loader - INFO - Loaded knowledge base entry: common_windows_commands
2025-07-14 14:59:19,012 - core.knowledge_base_loader - INFO - Loaded knowledge base entry: contact_it_support
2025-07-14 14:59:19,012 - core.knowledge_base_loader - INFO - Loaded knowledge base entry: display_resolution_wrong_or_fuzzy
2025-07-14 14:59:19,012 - core.knowledge_base_loader - INFO - Loaded knowledge base entry: dns_not_resolving
2025-07-14 14:59:19,012 - core.knowledge_base_loader - INFO - Loaded knowledge base entry: file_explorer_not_opening
2025-07-14 14:59:19,013 - core.knowledge_base_loader - INFO - Loaded knowledge base entry: hardware_diagnostics
2025-07-14 14:59:19,013 - core.knowledge_base_loader - INFO - Loaded knowledge base entry: hardware_request_process
2025-07-14 14:59:19,013 - core.knowledge_base_loader - INFO - Loaded knowledge base entry: high_disk_usage_windows11
2025-07-14 14:59:19,014 - core.knowledge_base_loader - INFO - Loaded knowledge base entry: how_to_clear_browser_cache
2025-07-14 14:59:19,014 - core.knowledge_base_loader - INFO - Loaded knowledge base entry: how_to_connect_to_vpn
2025-07-14 14:59:19,014 - core.knowledge_base_loader - INFO - Loaded knowledge base entry: how_to_install_software
2025-07-14 14:59:19,014 - core.knowledge_base_loader - INFO - Loaded knowledge base entry: how_to_reset_password
2025-07-14 14:59:19,015 - core.knowledge_base_loader - INFO - Loaded knowledge base entry: how_to_set_up_new_user
2025-07-14 14:59:19,015 - core.knowledge_base_loader - INFO - Loaded knowledge base entry: it_policy_overview
2025-07-14 14:59:19,015 - core.knowledge_base_loader - INFO - Loaded knowledge base entry: keyboard_not_responding
2025-07-14 14:59:19,015 - core.knowledge_base_loader - INFO - Loaded knowledge base entry: microsoft_office_faq
2025-07-14 14:59:19,015 - core.knowledge_base_loader - INFO - Loaded knowledge base entry: monitor_setup_guide
2025-07-14 14:59:19,016 - core.knowledge_base_loader - INFO - Loaded knowledge base entry: mouse_lagging_or_not_working
2025-07-14 14:59:19,016 - core.knowledge_base_loader - INFO - Loaded knowledge base entry: networking_troubleshooting
2025-07-14 14:59:19,016 - core.knowledge_base_loader - INFO - Loaded knowledge base entry: password_best_practices
2025-07-14 14:59:19,016 - core.knowledge_base_loader - INFO - Loaded knowledge base entry: slow_boot_time
2025-07-14 14:59:19,016 - core.knowledge_base_loader - INFO - Loaded knowledge base entry: software_request_process
2025-07-14 14:59:19,017 - core.knowledge_base_loader - INFO - Loaded knowledge base entry: system_freezing
2025-07-14 14:59:19,017 - core.knowledge_base_loader - INFO - Loaded knowledge base entry: taskbar_or_start_menu_not_responding
2025-07-14 14:59:19,017 - core.knowledge_base_loader - INFO - Loaded knowledge base entry: usb_device_not_recognized
2025-07-14 14:59:19,017 - core.knowledge_base_loader - INFO - Loaded knowledge base entry: wifi_drops_frequently
2025-07-14 14:59:19,017 - core.knowledge_base_loader - INFO - Loaded knowledge base entry: windows_activation_failed
2025-07-14 14:59:19,017 - core.knowledge_base_loader - INFO - Loaded knowledge base entry: windows_defender_not_turning_on
2025-07-14 14:59:19,018 - core.knowledge_base_loader - INFO - Loaded knowledge base entry: windows_random_shutdowns
2025-07-14 14:59:19,018 - core.knowledge_base_loader - INFO - Loaded 33 knowledge base entries
2025-07-14 14:59:19,018 - __main__ - INFO - Creating CrewAI agents...
2025-07-14 14:59:19,035 - __main__ - INFO - Created 5 CrewAI agents
2025-07-14 14:59:19,035 - __main__ - INFO - Creating CrewAI crew...
2025-07-14 14:59:19,047 - __main__ - INFO - CrewAI Helpdesk system initialized successfully!
2025-07-14 14:59:31,408 - __main__ - INFO - Processing new issue: my pc keeps freezing...
2025-07-14 14:59:31,513 - root - ERROR - LiteLLM call failed: litellm.BadRequestError: LLM Provider NOT provided. Pass in the LLM provider you are trying to call. You passed model=phi-3-mini-q4
 Pass model as E.g. For 'Huggingface' inference endpoints pass in `completion(model='huggingface/starcoder',..)` Learn more: https://docs.litellm.ai/docs/providers
2025-07-14 14:59:31,516 - __main__ - ERROR - Failed to submit issue: litellm.BadRequestError: LLM Provider NOT provided. Pass in the LLM provider you are trying to call. You passed model=phi-3-mini-q4
 Pass model as E.g. For 'Huggingface' inference endpoints pass in `completion(model='huggingface/starcoder',..)` Learn more: https://docs.litellm.ai/docs/providers

### ASSISTANT
Perfect — your `OobaboogaLLM` class **already uses direct requests** to the local oobabooga OpenAI-compatible API endpoint, which is great and matches your `LLMInterface`.

**You are *not* using LiteLLM in this class**, so the `litellm.BadRequestError: LLM Provider NOT provided.` error must come from somewhere else.

### So where is the LiteLLM error coming from?

You mentioned this error before:

```
litellm.BadRequestError: LLM Provider NOT provided.
```

This indicates somewhere **else** in your code, a call to LiteLLM is happening **without specifying `provider`** and `api_base`.

**Check if any other part of your project imports or uses LiteLLM directly.**

For example, do you have any file importing like:

```python
from litellm import completion
```

or

```python
import litellm
```

and calling it without `provider="openai"`?

### If you want, I can also help you search for any LiteLLM usage in your codebase and fix those calls. Just send me any file where you suspect LiteLLM is used or search your code for `litellm` import.

If you want, I can guide you on how to search for the LiteLLM calls or help you fix any snippet you share!

### USER
i believe its in this part of the llm_interface codebase: """
LLM Interface for connecting to local phi-3 model via oobabooga
"""
import requests
import json
from typing import Dict, Any, Optional
from dataclasses import dataclass
import logging
from core.character_loader import load_character

logger = logging.getLogger(__name__)

@dataclass
class LLMConfig:
    """Configuration for LLM connection"""
    base_url: str = "http://localhost:5000"  # <-- Make sure this matches your OpenAI API port
    model_name: str = "phi-3-mini-4k-instruct-q4"
    max_tokens: int = 2048
    temperature: float = 0.7
    timeout: int = 30

class LLMInterface:
    """Interface for communicating with local phi-3 model via oobabooga OpenAI API"""

    def __init__(self, config: Optional[LLMConfig] = None):
        self.config = config or LLMConfig()
        self.session = requests.Session()
        self.system_prompt = load_character()
        logger.info(f"Loaded system prompt: {self.system_prompt}")

    def generate_response(self, prompt: str, system_message: str = "") -> str:
        """Generate a response from the LLM using OpenAI-compatible API"""
        url = f"{self.config.base_url}/v1/chat/completions"
        headers = {"Content-Type": "application/json"}
        # Use the loaded system prompt unless a specific one is provided
        system_prompt = system_message if system_message is not None and system_message.strip() else self.system_prompt
        logger.info(f"Using system prompt: {system_prompt}")
        data = {
            "model": self.config.model_name,
            "messages": [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": prompt}
            ],
            "max_tokens": 512,
            "temperature": 0.7,
            "character": "Solace"
        }
        try:
            response = self.session.post(url, headers=headers, json=data, timeout=self.config.timeout)
            response.raise_for_status()
            result = response.json()
            logger.info(f"Raw LLM API response: {result}")
            return result["choices"][0]["message"]["content"].strip()
        except Exception as e:
            logger.error(f"OpenAI API request failed: {e}")
            return f"Error: {str(e)}"

    def analyze_issue(self, user_input: str) -> Dict[str, Any]:
        """Analyze user input to extract issue details"""
        system_prompt = """You are an IT helpdesk intake specialist. Analyze the user's issue and extract:
1. Issue type (network, software, hardware, general)
2. Severity level (low, medium, high, critical)
3. Key symptoms and error messages
4. Operating system and device type if mentioned
5. Urgency level

Return your analysis as a JSON object with these fields."""
        
        prompt = f"Please analyze this IT issue: {user_input}"
        
        try:
            response = self.generate_response(prompt, system_prompt)
            # Try to extract JSON from response
            if "{" in response and "}" in response:
                start = response.find("{")
                end = response.rfind("}") + 1
                json_str = response[start:end]
                return json.loads(json_str)
            else:
                # Fallback to basic analysis
                return {
                    "issue_type": "general",
                    "severity": "medium",
                    "symptoms": [user_input],
                    "os": "unknown",
                    "urgency": "normal"
                }
        except Exception as e:
            logger.error(f"Error analyzing issue: {e}")
            return {
                "issue_type": "general",
                "severity": "medium",
                "symptoms": [user_input],
                "os": "unknown",
                "urgency": "normal"
            }
    
    def route_task(self, issue_analysis: Dict[str, Any]) -> str:
        """Determine which agent should handle the task"""
        system_prompt = """You are a task dispatcher. Based on the issue analysis, determine which agent should handle this task.
Available agents:
- Tier 1 Generalist: Basic troubleshooting, connectivity, passwords, simple fixes
- Network Specialist: Network issues, DNS, VPN, firewall, connectivity problems
- Systems Specialist: OS errors, software crashes, registry issues, application problems

Return only the agent name."""
        
        prompt = f"Route this issue to the appropriate agent: {json.dumps(issue_analysis)}"
        
        try:
            response = self.generate_response(prompt, system_prompt)
            # Clean up response
            response = response.strip().lower()
            if "network" in response:
                return "Network Specialist"
            elif "system" in response:
                return "Systems Specialist"
            else:
                return "Tier 1 Generalist"
        except Exception as e:
            logger.error(f"Error routing task: {e}")
            return "Tier 1 Generalist"
    
    def test_connection(self) -> bool:
        """Test if the LLM is accessible"""
        try:
            response = self.generate_response("Hello", "You are a helpful assistant.")
            return len(response) > 0 and "error" not in response.lower()
        except Exception as e:
            logger.error(f"LLM connection test failed: {e}")
            return False

### ASSISTANT
Thanks for the full log — this gives **exactly** what we need.

### ❌ What Broke It:
The issue **is not with Cursor** — it’s coming from **LiteLLM**, which is trying to forward the model request but **doesn't know what provider to use**.

Here's the **critical error**:
```
LiteLLM call failed: litellm.BadRequestError: LLM Provider NOT provided. 
Pass in the LLM provider you are trying to call. You passed model=phi-3-mini-q4
```

So even though your config has `model_name: "phi-3-mini-q4"`, **you never told LiteLLM whether this is a local model, an OpenAI call, HuggingFace, etc.**

### ✅ Option 1: Run in Cursor Terminal

Open the **integrated terminal** in Cursor and run:

```bash
pip show crewai
```

You'll get output like:

```
Name: crewai
Version: 0.19.0
Summary: Multi-agent framework for AI teamwork
...
```

### ✅ Option 3: Check `pyproject.toml` or `requirements.txt`

If you’re using `pyproject.toml` or `requirements.txt` in your project:

- Look inside those files for a line like:

```
crewai==0.19.0
```
---
## Related

### Projects

- [[nodes/projects/homelab-stack|Homelab Stack]]
- [[nodes/projects/private-ai-consulting|Private AI Consulting]]

### Topics

- [[nodes/topics/tech/coding|Coding]]
- [[nodes/topics/tech/ai-tools|Ai Tools]]