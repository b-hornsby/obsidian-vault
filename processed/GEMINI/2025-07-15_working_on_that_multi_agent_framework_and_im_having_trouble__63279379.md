---
category: coding
date: 2025-07-15
id: 007393
linked_nodes: ['nodes/people/bryan.md', 'nodes/topics/tech/coding.md', 'nodes/projects/operation-immortal-agent.md']
linked_projects:
- operation-immortal-agent
resolution: partial
sentiment: stuck
source: GEMINI
summary: Bryan is working on his CrewAI multi-agent helpdesk system and needs help
  getting back on track in Cursor.
tags:
- crewai
- multi-agent-framework
- helpdesk-ai
- cursor-ide
- python
---
# working on that multi agent framework and i'm having trouble with the main_crewai.py file. the purpose of it within the framework is: """
Multi-Agent Helpdesk System (CrewAI-Powered)
Main entry point for the helpdesk system using CrewAI. this is the code inside so far but i need help getting back on track in cursor: #!/usr/bin/env python3
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
from pydantic import BaseModel, Field
from langchain.tools import tool
from langchain_core.tools.base import BaseTool

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
        from pydantic import BaseModel, Field

        class SearchKBArgs(BaseModel):
            query: str = Field(..., description="Query to search in the knowledge base")
            
        class SearchKBTool(BaseTool):
            name: str = "search_knowledge_base"
            description: str = "Search the knowledge base for relevant troubleshooting information"
            args_schema: type = SearchKBArgs
            def __init__(self, knowledge_base):
                super().__init__()
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
            args_schema: type = GuideArgs
            def __init__(self, knowledge_base):
                super().__init__()
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
            args_schema: type = PingArgs
            def __init__(self, network_tools):
                super().__init__()
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
            args_schema: type = DNSArgs
            def __init__(self, network_tools):
                super().__init__()
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
            args_schema: type = EmptyArgs
            def __init__(self, network_tools):
                super().__init__()
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
            args_schema: type = EmptyArgs
            def __init__(self, system_tools):
                super().__init__()
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
            args_schema: type = EmptyArgs
            def __init__(self, system_tools):
                super().__init__()
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
            args_schema: type = EmptyArgs
            def __init__(self, system_tools):
                super().__init__()
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
            args_schema: type = EmptyArgs
            def __init__(self, system_tools):
                super().__init__()
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
            args_schema: type = ProcessArgs
            def __init__(self, general_tools):
                super().__init__()
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
            tasks=[],  # Tasks will be created dynamically
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
            expected_output="A structured analysis of the issue, including category, severity, symptoms, OS/device info, urgency, and recommended next steps, plus references to relevant guides.",
            agent=self.agents["intake_specialist"]
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
            expected_output="A summary of troubleshooting steps taken, diagnostics results, and either a clear resolution or a note for escalation.",
            agent=self.agents["tier1_generalist"]
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
            expected_output="A detailed report of network diagnostics performed, findings, and any network-specific solutions applied.",
            agent=self.agents["network_specialist"]
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
            expected_output="A detailed report of system/software diagnostics, findings, and any system-level solutions applied.",
            agent=self.agents["systems_specialist"]
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
            expected_output="A final summary stating if the issue is resolved or needs escalation, with clear escalation instructions and documentation of all prior steps.",
            agent=self.agents["escalation_manager"]
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
                    "status": "completed"  # CrewAI tasks are synchronous
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

### USER
working on that multi agent framework and i'm having trouble with the main_crewai.py file. the purpose of it within the framework is: """
Multi-Agent Helpdesk System (CrewAI-Powered)
Main entry point for the helpdesk system using CrewAI. this is the code inside so far but i need help getting back on track in cursor: #!/usr/bin/env python3
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
from pydantic import BaseModel, Field
from langchain.tools import tool
from langchain_core.tools.base import BaseTool

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
        from pydantic import BaseModel, Field

        class SearchKBArgs(BaseModel):
            query: str = Field(..., description="Query to search in the knowledge base")
            
        class SearchKBTool(BaseTool):
            name: str = "search_knowledge_base"
            description: str = "Search the knowledge base for relevant troubleshooting information"
            args_schema: type = SearchKBArgs
            def __init__(self, knowledge_base):
                super().__init__()
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
            args_schema: type = GuideArgs
            def __init__(self, knowledge_base):
                super().__init__()
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
            args_schema: type = PingArgs
            def __init__(self, network_tools):
                super().__init__()
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
            args_schema: type = DNSArgs
            def __init__(self, network_tools):
                super().__init__()
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
            args_schema: type = EmptyArgs
            def __init__(self, network_tools):
                super().__init__()
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
            args_schema: type = EmptyArgs
            def __init__(self, system_tools):
                super().__init__()
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
            args_schema: type = EmptyArgs
            def __init__(self, system_tools):
                super().__init__()
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
            args_schema: type = EmptyArgs
            def __init__(self, system_tools):
                super().__init__()
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
            args_schema: type = EmptyArgs
            def __init__(self, system_tools):
                super().__init__()
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
            args_schema: type = ProcessArgs
            def __init__(self, general_tools):
                super().__init__()
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
            tasks=[],  # Tasks will be created dynamically
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
            expected_output="A structured analysis of the issue, including category, severity, symptoms, OS/device info, urgency, and recommended next steps, plus references to relevant guides.",
            agent=self.agents["intake_specialist"]
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
            expected_output="A summary of troubleshooting steps taken, diagnostics results, and either a clear resolution or a note for escalation.",
            agent=self.agents["tier1_generalist"]
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
            expected_output="A detailed report of network diagnostics performed, findings, and any network-specific solutions applied.",
            agent=self.agents["network_specialist"]
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
            expected_output="A detailed report of system/software diagnostics, findings, and any system-level solutions applied.",
            agent=self.agents["systems_specialist"]
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
            expected_output="A final summary stating if the issue is resolved or needs escalation, with clear escalation instructions and documentation of all prior steps.",
            agent=self.agents["escalation_manager"]
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
                    "status": "completed"  # CrewAI tasks are synchronous
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

### GEMINI
It looks like you have a solid foundation for your main_crewai.py file! You've successfully set up the basic structure for a multi-agent helpdesk system using CrewAI, including custom tools, agents, and a task submission workflow. To get you "back on track," let's refine and enhance what you have, focusing on a few key areas that will make your framework more robust, efficient, and aligned with best practices for multi-agent systems. Here's a breakdown of the improvements and additions I recommend: Key Areas for Improvement 1. Enhanced Task Orchestration 🎼 Currently, your _create_tasks_for_issue method creates all five tasks every time an issue is submitted. While this works, a more dynamic approach would be to only create and assign tasks as they become relevant. This is particularly important for an "Escalation Manager" task, which should ideally only be triggered if previous agents fail to resolve an issue. CrewAI allows for dynamic task creation and delegation, but for a sequential process, it often makes sense to let agents delegate or pass information to trigger subsequent tasks. 2. Clearer Task Outputs & Handover 🤝 The expected_output for each task is good, but the result of one agent's task should explicitly inform the next agent's task. This "handover" mechanism is crucial for a smooth workflow in a sequential process. 3. Error Handling and Robustness 🛡️ You've got basic error handling, but we can make it more specific and informative, especially around tool usage and LLM interactions. 4. Agent allow_delegation and verbose Control 🧑‍💻 You've set allow_delegation to True for most agents, which is great. Ensure the tasks are structured to leverage this effectively. The verbose setting is useful for debugging but might be turned off in production. 5. Centralized Configuration Management ⚙️ While you have LLMConfig and argparse, a more comprehensive configuration system (e.g., using a config.ini or YAML file) could manage all aspects of your system, not just LLM settings. 6. Consider Agent Collaboration 🗣️ Your current setup is mostly sequential. CrewAI excels at collaborative agents. While your "Escalation Manager" is a good step towards this, think about how agents could collaborate during the troubleshooting process, not just at the end. For instance, the Tier 1 Generalist might consult the Network Specialist directly if they hit a network-related roadblock. This would involve using allow_delegation more actively and potentially having agents pass tasks to each other. Recommended Refinements & Code Example Here's an updated version of your main_crewai.py focusing on the above points, particularly refining the task creation and agent interaction logic. #!/usr/bin/env python3 """ Multi-Agent Helpdesk System (CrewAI-Powered) Main entry point for the helpdesk system using CrewAI """ import sys import os import logging import argparse from typing import Optional, List, Dict, Any import json from datetime import datetime # Add the project root to the Python path sys.path.insert(0, os.path.dirname(os.path.abspath(__file__))) from crewai import Agent, Task, Crew, Process from pydantic import BaseModel, Field from langchain_core.tools.base import BaseTool from core.llm_interface import LLMInterface, LLMConfig from core.crewai_llm import OobaboogaLLM from core.knowledge_base_loader import KnowledgeBaseLoader from tools.network_tools import NetworkTools from tools.system_tools import SystemTools from tools.general_tools import GeneralTools # Configure logging logging.basicConfig( level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', handlers=[ logging.FileHandler('helpdesk_crewai.log'), logging.StreamHandler(sys.stdout) ] ) logger = logging.getLogger(__name__) # --- Custom Tool Definitions (Moved outside class for clarity if not dynamically created) --- # It's good practice to define these where they can be easily imported or accessed. # If they only serve this one file, keeping them here is fine. class SearchKBArgs(BaseModel): query: str = Field(..., description="Query to search in the knowledge base") class SearchKBTool(BaseTool): name: str = "search_knowledge_base" description: str = "Search the knowledge base for relevant troubleshooting information" args_schema: type = SearchKBArgs def __init__(self, knowledge_base_loader: KnowledgeBaseLoader): super().__init__() self._knowledge_base = knowledge_base_loader def _run(self, query: str) -> str: logger.debug(f"SearchKBTool: Searching knowledge base for '{query}'") results = self._knowledge_base.search_content(query) if results: return f"Found {len(results)} relevant guides: " + "; ".join([f"{r['key']} (Score: {r['score']:.2f})" for r in results[:3]]) return "No relevant guides found in knowledge base." class GuideArgs(BaseModel): issue_type: str = Field(..., description="Issue type or keyword to get the guide for") class GuideTool(BaseTool): name: str = "get_troubleshooting_guide" description: str = "Get a specific troubleshooting guide from the knowledge base by issue type or keyword." args_schema: type = GuideArgs def __init__(self, knowledge_base_loader: KnowledgeBaseLoader): super().__init__() self._knowledge_base = knowledge_base_loader def _run(self, issue_type: str) -> str: logger.debug(f"GuideTool: Getting guide for '{issue_type}'") guide = self._knowledge_base.get_troubleshooting_guide(issue_type) return guide if guide else f"No guide found for '{issue_type}'." class PingArgs(BaseModel): host: str = Field(..., description="Host to ping (IP address or hostname)") class PingTool(BaseTool): name: str = "ping_host" description: str = "Ping a host to check network connectivity. Returns 'success' or 'failure' and details." args_schema: type = PingArgs def __init__(self, network_tools: NetworkTools): super().__init__() self._network_tools = network_tools def _run(self, host: str) -> str: logger.debug(f"PingTool: Pinging host '{host}'") result = self._network_tools.ping_check(host) if result.get('success'): return f"Ping successful for {host}. Details: {result.get('details', 'No details provided.')}" return f"Ping failed for {host}. Error: {result.get('error', 'Unknown error.')}" class DNSArgs(BaseModel): domain: str = Field(..., description="Domain to check DNS resolution for") class DNSTool(BaseTool): name: str = "check_dns_resolution" description: str = "Check DNS resolution for a given domain. Returns resolved IPs or an error." args_schema: type = DNSArgs def __init__(self, network_tools: NetworkTools): super().__init__() self._network_tools = network_tools def _run(self, domain: str) -> str: logger.debug(f"DNSTool: Checking DNS resolution for '{domain}'") result = self._network_tools.dns_check(domain) if result.get('success'): return f"DNS resolution successful for {domain}. Resolved IPs: {', '.join(result.get('resolved_ips', []))}" return f"DNS resolution failed for {domain}. Error: {result.get('error', 'Unknown error.')}" class EmptyArgs(BaseModel): pass class InternetTool(BaseTool): name: str = "test_internet_connectivity" description: str = "Test overall internet connectivity by trying to reach common services." args_schema: type = EmptyArgs def __init__(self, network_tools: NetworkTools): super().__init__() self._network_tools = network_tools def _run(self) -> str: logger.debug("InternetTool: Testing internet connectivity") result = self._network_tools.check_internet_connectivity() if result.get('successful_connections', 0) > 0: return f"Internet connectivity confirmed. {result.get('successful_connections', 0)} connections successful out of {result.get('total_attempts', 0)}." return f"Internet connectivity failed. Error: {result.get('error', 'No successful connections.')}" class DiskTool(BaseTool): name: str = "check_disk_space" description: str = "Check available disk space on the primary partition. Returns usage percentage and free space." args_schema: type = EmptyArgs def __init__(self, system_tools: SystemTools): super().__init__() self._system_tools = system_tools def _run(self) -> str: logger.debug("DiskTool: Checking disk space") result = self._system_tools.check_disk_space() if result.get('success'): return f"Disk space: {result.get('usage_percent', 0):.2f}% used, {result.get('free_gb', 0):.2f} GB free." return f"Disk space check failed. Error: {result.get('error', 'Unknown error.')}" class MemoryTool(BaseTool): name: str = "check_memory_usage" description: str = "Check system memory usage. Returns usage percentage and available memory." args_schema: type = EmptyArgs def __init__(self, system_tools: SystemTools): super().__init__() self._system_tools = system_tools def _run(self) -> str: logger.debug("MemoryTool: Checking memory usage") result = self._system_tools.check_memory_usage() if result.get('success'): return f"Memory usage: {result.get('usage_percent', 0):.2f}% used, {result.get('available_gb', 0):.2f} GB available." return f"Memory check failed. Error: {result.get('error', 'Unknown error.')}" class ServicesTool(BaseTool): name: str = "check_running_services" description: str = "Get a count of currently running system services." args_schema: type = EmptyArgs def __init__(self, system_tools: SystemTools): super().__init__() self._system_tools = system_tools def _run(self) -> str: logger.debug("ServicesTool: Checking running services") result = self._system_tools.get_running_services() if result.get('success'): return f"Running services: {result.get('running_services', 0)} services active. Details: {result.get('details', 'No details provided.')}" return f"Services check failed. Error: {result.get('error', 'Unknown error.')}" class SystemInfoTool(BaseTool): name: str = "get_system_info" description: str = "Retrieve basic system information like platform, OS, and architecture." args_schema: type = EmptyArgs def __init__(self, system_tools: SystemTools): super().__init__() self._system_tools = system_tools def _run(self) -> str: logger.debug("SystemInfoTool: Getting system information") result = self._system_tools.get_system_info() if result.get('success'): info = result.get('system_info', {}) return (f"System Info: Platform: {info.get('platform', 'Unknown')}, " f"OS Version: {info.get('platform_version', 'Unknown')}, " f"Architecture: {info.get('architecture', 'Unknown')}.") return f"System info retrieval failed. Error: {result.get('error', 'Unknown error.')}" class ProcessArgs(BaseModel): process_name: str = Field(..., description="The exact name of the process to check (e.g., 'chrome.exe', 'sshd')") class ProcessTool(BaseTool): name: str = "check_process_status" description: str = "Check if a specific process is running and how many instances are active." args_schema: type = ProcessArgs def __init__(self, general_tools: GeneralTools): super().__init__() self._general_tools = general_tools def _run(self, process_name: str) -> str: logger.debug(f"ProcessTool: Checking status for process '{process_name}'") result = self._general_tools.check_process_status(process_name) if result.get('success'): count = result.get('running_instances', 0) return f"Process '{process_name}': {count} instances running." return f"Process check for '{process_name}' failed. Error: {result.get('error', 'Unknown error.')}" # --- End Custom Tool Definitions --- class HelpdeskCrewAI: """Main helpdesk system class using CrewAI""" def __init__(self, config: Optional[LLMConfig] = None): self.config = config or LLMConfig() self.llm_interface: Optional[LLMInterface] = None self.knowledge_base: Optional[KnowledgeBaseLoader] = None self.agents: Dict[str, Agent] = {} self.crew: Optional[Crew] = None self.tasks_history: List[Dict[str, Any]] = [] self.initialized: bool = False # Initialize tool instances (These should be ready before agents are created) self.network_tools = NetworkTools() self.system_tools = SystemTools() self.general_tools = GeneralTools() def initialize(self) -> bool: """Initialize the helpdesk system by setting up LLM, KB, agents, and crew.""" try: logger.info("Initializing CrewAI Multi-Agent Helpdesk System...") # Initialize LLM interface logger.info("Initializing LLM interface...") self.llm_interface = LLMInterface(self.config) # Test LLM connection if not self.llm_interface.test_connection(): logger.warning("LLM connection test failed. System may have limited functionality.") # Initialize knowledge base logger.info("Loading knowledge base...") self.knowledge_base = KnowledgeBaseLoader() # Assuming this loads from a default path or is configured internally # Create CrewAI agents logger.info("Creating CrewAI agents...") self._create_agents() # Note: The crew is now created dynamically per issue to handle specific task flows # self._create_crew() self.initialized = True logger.info("CrewAI Helpdesk system initialized successfully! 🚀") return True except Exception as e: logger.error(f"Failed to initialize CrewAI helpdesk system: {e}", exc_info=True) return False def _create_agents(self): """Create and configure CrewAI agents with their respective tools.""" # Instantiate custom tools with their dependencies search_tool = SearchKBTool(self.knowledge_base) guide_tool = GuideTool(self.knowledge_base) ping_tool = PingTool(self.network_tools) dns_tool = DNSTool(self.network_tools) internet_tool = InternetTool(self.network_tools) disk_tool = DiskTool(self.system_tools) memory_tool = MemoryTool(self.system_tools) services_tool = ServicesTool(self.system_tools) system_info_tool = SystemInfoTool(self.system_tools) process_tool = ProcessTool(self.general_tools) common_tools = [search_tool, guide_tool] # Tools available to many agents network_specific_tools = [ping_tool, dns_tool, internet_tool] system_specific_tools = [disk_tool, memory_tool, services_tool, system_info_tool, process_tool] # Define Agents self.agents["intake_specialist"] = Agent( role="IT Helpdesk Intake Specialist", goal="Analyze and categorize incoming IT issues, extract key information, and prepare detailed tickets for resolution.", backstory="""You are an experienced IT helpdesk intake specialist with 10+ years of experience. You excel at quickly understanding user problems, categorizing them accurately, and gathering all necessary information for efficient resolution. You have deep knowledge of IT terminology and can identify patterns in user-reported issues. Your primary task is to create a precise and actionable summary of the user's issue, including its type, severity, and suggested initial steps.""", verbose=True, allow_delegation=False, # Intake specialist does not delegate, they process and pass on. tools=common_tools, llm=self._get_llm_config() ) self.agents["tier1_generalist"] = Agent( role="Tier 1 IT Support Generalist", goal="Resolve basic IT issues quickly and efficiently using standard troubleshooting procedures, or escalate if necessary.", backstory="""You are a skilled Tier 1 IT support technician with expertise in basic troubleshooting. You handle common issues like password resets, basic connectivity problems, software installations, and simple hardware diagnostics. You follow established procedures and are adept at using diagnostic tools to identify root causes. You are able to escalate complex issues to specialized agents when your expertise or tools are insufficient.""", verbose=True, allow_delegation=True, # Can delegate to other specialists tools=common_tools + system_specific_tools, # Tier 1 often needs basic system checks llm=self._get_llm_config() ) self.agents["network_specialist"] = Agent( role="Network Infrastructure Specialist", goal="Diagnose and resolve advanced network-related issues including connectivity, DNS, VPN, and firewall problems.", backstory="""You are a senior network specialist with extensive experience in network infrastructure. You excel at diagnosing complex connectivity issues, DNS problems, VPN configurations, and firewall rules. You understand intricate network protocols, routing, and can troubleshoot challenging network problems that Tier 1 support cannot handle. You rely on advanced network diagnostic tools.""", verbose=True, allow_delegation=False, # This agent focuses on network issues and reports back. tools=common_tools + network_specific_tools, llm=self._get_llm_config() ) self.agents["systems_specialist"] = Agent( role="Systems and Software Specialist", goal="Resolve operating system issues, software malfunctions, and perform deep system-level troubleshooting.", backstory="""You are a systems specialist with deep knowledge of operating systems (Windows, Linux, macOS), software troubleshooting, and system-level diagnostics. You handle OS errors, software crashes, registry issues, and complex system performance problems. You understand system architecture and can perform advanced troubleshooting steps beyond basic checks.""", verbose=True, allow_delegation=False, # This agent focuses on system issues and reports back. tools=common_tools + system_specific_tools, llm=self._get_llm_config() ) self.agents["escalation_manager"] = Agent( role="IT Escalation Manager", goal="Review unresolved issues and determine appropriate escalation paths to human technicians or external teams.", backstory="""You are an escalation manager with years of experience in IT support management and incident response. You review complex issues that couldn't be resolved by automated agents and determine the best human intervention path. You are responsible for documenting the troubleshooting history and providing clear, concise instructions for the human technician taking over the issue. You prioritize escalations based on business impact and urgency.""", verbose=True, allow_delegation=False, # This agent makes the final decision for human escalation. tools=common_tools, # Can use KB to find relevant human contacts/procedures llm=self._get_llm_config() ) logger.info(f"Created {len(self.agents)} CrewAI agents.") def _get_llm_config(self): """Get LLM configuration for CrewAI agents.""" if not self.llm_interface or not self.config: raise RuntimeError("LLMInterface or config not initialized.") # OobaboogaLLM directly uses the parameters from LLMConfig return OobaboogaLLM( base_url=self.config.base_url, model_name=self.config.model_name, max_tokens=self.config.max_tokens, temperature=self.config.temperature, timeout=self.config.timeout ) # Removed _create_crew as it's now created dynamically in submit_issue def submit_issue(self, user_input: str) -> str: """Submit a new issue to the helpdesk system for multi-agent processing.""" if not self.initialized: raise RuntimeError("Helpdesk system not initialized. Please call initialize() first.") try: logger.info(f"Processing new issue: '{user_input[:100]}...'") # Create a unique task ID task_id = f"TASK-{len(self.tasks_history) + 1:04d}-{datetime.now().strftime('%Y%m%d%H%M%S')}" # Define tasks with dynamic dependencies for a more robust workflow intake_task = Task( description=f"""Analyze the following IT issue and create a detailed troubleshooting ticket: User Issue: {user_input} Your analysis must include: 1. **Issue Categorization**: (e.g., Network, Software, Hardware, Account, General, Performance) 2. **Severity Assessment**: (e.g., Low, Medium, High, Critical - based on potential impact and urgency) 3. **Key Symptoms and Error Messages**: List all relevant observations. 4. **Operating System and Device Information**: If mentioned or inferable (e.g., Windows 10, MacBook Pro, specific application). 5. **Urgency Level**: (e.g., Low, Medium, High, Immediate - reflecting the need for quick action). 6. **Recommended Initial Steps**: Suggest immediate, basic troubleshooting actions. 7. **Knowledge Base References**: Search the knowledge base using 'search_knowledge_base' and 'get_troubleshooting_guide' tools for similar issues or relevant guides. Include the titles/keys of found guides. Provide your analysis in a clear, structured JSON format with keys: 'category', 'severity', 'symptoms', 'os_device', 'urgency', 'recommended_steps', 'kb_references'. """, expected_output="A comprehensive JSON-formatted IT ticket containing categorized details, severity, symptoms, OS/device info, urgency, recommended initial steps, and referenced knowledge base articles.", agent=self.agents["intake_specialist"], output_file=f"tasks/{task_id}_intake.json" # Output to a file for persistence and clear handover ) tier1_troubleshooting_task = Task( description=f"""Based on the intake analysis, perform initial troubleshooting for the IT issue. **Context from Intake Specialist**: This task will receive the output from the Intake Specialist. **Your Goal**: Attempt to resolve the issue using your Tier 1 troubleshooting skills and tools. **Steps**: 1. **Review Intake Analysis**: Understand the issue details, category, and recommended steps. 2. **Perform Basic Diagnostics**: Use your 'check_disk_space', 'check_memory_usage', 'check_process_status', and 'get_system_info' tools as needed. 3. **Apply Standard Fixes**: Attempt common solutions for the identified issue type. 4. **Document Actions**: Keep a clear record of all steps taken and their outcomes. 5. **Determine Resolution or Escalation**: - If resolved, provide clear, concise resolution steps. - If NOT resolved, clearly state why it couldn't be resolved and indicate which specialist (Network or Systems) should handle it next, or if it requires immediate human escalation (Escalation Manager). Provide all gathered diagnostic information for the next agent. Expected Output: A detailed report summarizing troubleshooting steps, diagnostics results, and either a clear resolution or a reasoned escalation recommendation with supporting data (e.g., "Issue resolved by X. Steps: Y. Result: Z." OR "Issue requires escalation to [Network/Systems] Specialist because [reason]. Diagnostics: [data]."). """, expected_output="A detailed report summarizing troubleshooting steps taken, diagnostics results, and either a clear resolution or a reasoned escalation recommendation for a specialist or the escalation manager.", agent=self.agents["tier1_generalist"], context=[intake_task], # This task depends on the intake_task's output output_file=f"tasks/{task_id}_tier1.md" ) network_troubleshooting_task = Task( description=f"""Address network-related aspects of the IT issue. **Context**: This task receives output from the Tier 1 Generalist, specifically when network issues are identified or suspected. **Your Goal**: Diagnose and resolve network specific problems. **Steps**: 1. **Review Prior Context**: Understand the current state and why the issue was escalated to you. 2. **Perform Network Diagnostics**: Use 'ping_host', 'check_dns_resolution', and 'test_internet_connectivity' tools. 3. **Analyze Network Configuration**: Infer potential issues from diagnostics. 4. **Provide Solutions**: Suggest or apply network-specific fixes. 5. **Report Findings**: Document your findings and resolution, or why it remains unresolved. Only execute this task if the Tier 1 Generalist explicitly escalates a network issue, or if the intake analysis clearly categorizes it as a network issue that Tier 1 could not fully address. """, expected_output="A comprehensive report detailing network diagnostics, findings, and either a solution or a clear reason for further escalation.", agent=self.agents["network_specialist"], context=[tier1_troubleshooting_task], # dynamic_defer=True # This would be ideal for conditional execution based on context output_file=f"tasks/{task_id}_network.md" ) systems_troubleshooting_task = Task( description=f"""Address system and software-related aspects of the IT issue. **Context**: This task receives output from the Tier 1 Generalist, specifically when system or software issues are identified or suspected. **Your Goal**: Diagnose and resolve system and software specific problems. **Steps**: 1. **Review Prior Context**: Understand the current state and why the issue was escalated to you. 2. **Perform System Diagnostics**: Use 'check_disk_space', 'check_memory_usage', 'check_running_services', 'check_process_status', and 'get_system_info' tools. 3. **Analyze System Logs/Errors**: Infer potential issues from diagnostics. 4. **Provide Solutions**: Suggest or apply system-specific fixes. 5. **Report Findings**: Document your findings and resolution, or why it remains unresolved. Only execute this task if the Tier 1 Generalist explicitly escalates a system/software issue, or if the intake analysis clearly categorizes it as a system/software issue that Tier 1 could not fully address. """, expected_output="A comprehensive report detailing system and software diagnostics, findings, and either a solution or a clear reason for further escalation.", agent=self.agents["systems_specialist"], context=[tier1_troubleshooting_task], # dynamic_defer=True # This would be ideal for conditional execution based on context output_file=f"tasks/{task_id}_systems.md" ) escalation_review_task = Task( description=f"""Review the entire history of troubleshooting for issue {task_id} and determine the final status and escalation path. **Context**: This task receives the outputs from the Tier 1, Network, and Systems troubleshooting tasks. **Your Goal**: Decide if the issue is resolved, or if it requires human intervention. **Steps**: 1. **Consolidate Information**: Read and synthesize the reports from all previous agents. 2. **Final Assessment**: Determine if a definitive resolution has been achieved by any agent. 3. **If Resolved**: Clearly state the resolution and the agent responsible. 4. **If Unresolved**: - Identify gaps in troubleshooting. - Determine the most appropriate human team or individual for escalation. - Provide a concise summary of the issue, what has been attempted, and what information is still needed or why human expertise is required. - Prioritize the human escalation based on the original severity/urgency. - Suggest next steps for the human technician. Expected Output: A final status report stating "Issue Resolved: [Details]" or "Issue Requires Human Escalation: [Reason and detailed instructions for human technician, including priority and history of attempts].", in a clear, concise format. """, expected_output="A final summary indicating if the issue is resolved or requires human escalation, including resolution details or clear escalation instructions and history.", agent=self.agents["escalation_manager"], context=[tier1_troubleshooting_task, network_troubleshooting_task, systems_troubleshooting_task], # All previous task outputs inform this one output_file=f"tasks/{task_id}_final_report.md" ) # Define the sequential flow of tasks # The context mechanism in CrewAI allows agents to pick up from where the previous one left off. # However, for true *conditional* task execution (e.g., only run network_task if Tier1 says it's a network issue), # you would need more advanced CrewAI features (like conditional tasks in newer versions) or # have the agents themselves use internal logic to decide if they need to run their specific tools/solve. # For this example, we'll keep it sequential but emphasize the agent's role in deciding if it's their domain. tasks_to_run = [ intake_task, tier1_troubleshooting_task, network_troubleshooting_task, # Network and Systems tasks will process context and decide if they are relevant systems_troubleshooting_task, escalation_review_task ] # Create a new crew for each issue to ensure isolated execution environments crew = Crew( agents=list(self.agents.values()), tasks=tasks_to_run, process=Process.sequential, verbose=True, full_output=True # Get more detailed output from kickoff ) # Execute the crew logger.info(f"Starting CrewAI process for Task ID: {task_id}") result = crew.kickoff() # Store task history task_record = { "task_id": task_id, "user_input": user_input, "created_at": datetime.now().isoformat(), "final_result": result['final_output'], # Use 'final_output' for the final result "all_task_outputs": result['tasks_outputs'], # Store all task outputs for review "status": "completed", # CrewAI tasks are synchronous "tasks_flow": [task.description for task in tasks_to_run] } self.tasks_history.append(task_record) logger.info(f"Issue processing complete for Task ID: {task_id}") return task_id except Exception as e: logger.error(f"Failed to submit or process issue: {e}", exc_info=True) raise def get_task_status(self, task_id: str) -> Optional[dict]: """Get the status and full result of a specific task by ID.""" if not self.initialized: raise RuntimeError("Helpdesk system not initialized.") for task_record in self.tasks_history: if task_record["task_id"] == task_id: return { "task_id": task_record["task_id"], "user_input": task_record["user_input"], "created_at": task_record["created_at"], "status": task_record["status"], "final_result": task_record["final_result"], "all_task_outputs": task_record.get("all_task_outputs", "N/A") # Provide all outputs } return None def get_system_summary(self) -> dict: """Get a summary of the entire helpdesk system's current state.""" if not self.initialized: raise RuntimeError("Helpdesk system not initialized.") return { "total_agents": len(self.agents), "available_agents": list(self.agents.keys()), "total_issues_processed": len(self.tasks_history), "system_status": "operational" if self.initialized else "not_initialized", "last_issue_id": self.tasks_history[-1]["task_id"] if self.tasks_history else "N/A" } def export_tasks(self, filepath: str) -> bool: """Export all recorded tasks (issue history) to a JSON file.""" if not self.initialized: raise RuntimeError("Helpdesk system not initialized.") try: # Ensure the directory exists os.makedirs(os.path.dirname(filepath) or '.', exist_ok=True) with open(filepath, 'w', encoding='utf-8') as f: json.dump(self.tasks_history, f, indent=2, ensure_ascii=False) logger.info(f"Tasks exported successfully to '{filepath}'.") return True except Exception as e: logger.error(f"Failed to export tasks to '{filepath}': {e}", exc_info=True) return False def interactive_mode(helpdesk: HelpdeskCrewAI): """Run the helpdesk system in an interactive command-line interface.""" print("\n=== 🤖 CrewAI Multi-Agent Helpdesk System (Interactive Mode) 🤖 ===") print("Type 'quit' to exit, 'status' to see system summary, 'export' to export tasks history.") print("Enter your IT issue below to get started! 👇\n") while True: try: user_input = input("You 💬: ").strip() if user_input.lower() == 'quit': print("👋 Exiting Helpdesk System. Goodbye!") break elif user_input.lower() == 'status': summary = helpdesk.get_system_summary() print("\n
--- 📊 System Summary ---
") for key, value in summary.items(): print(f"{key.replace('_', ' ').title()}: {value}") print("
---
-
---
-
---
-
---
-
---
-
---
---\n") elif user_input.lower() == 'export': export_path = "exported_helpdesk_tasks.json" success = helpdesk.export_tasks(export_path) if success: print(f"✅ Tasks exported to {export_path}") else: print(f"❌ Failed to export tasks to {export_path}") print() elif user_input: print("\n
--- ⏳ Processing your issue... ---
") task_id = helpdesk.submit_issue(user_input) print(f"✅ Issue submitted! Your Task ID: {task_id}") # Get and display result status_report = helpdesk.get_task_status(task_id) if status_report: print(f"\n
--- 📋 Task Report for {status_report['task_id']} ---
") print(f"Status: {status_report['status'].upper()}") print(f"User Input: {status_report['user_input']}") print(f"Created At: {status_report['created_at']}") print("\n
--- Final Result ---
") print(status_report['final_result']) print("\n
--- All Task Outputs (for detailed review) ---
") for output in status_report['all_task_outputs']: print(f" **Agent: {output.agent.role}**") print(f" Task: {output.task.description.splitlines()[0]}...") print(f" Output: {output.output[:200]}...\n") # Truncate for display print("
---
-
---
-
---
-
---
-
---
-
---
-
---
-
---
-
---
-
---
-
---
--\n") else: print("❌ Could not retrieve task status. Something went wrong after submission.\n") else: print("Please enter an IT issue or a command ('quit', 'status', 'export').") except KeyboardInterrupt: print("\n👋 Detected Ctrl+C. Shutting down interactive mode gracefully.") break except RuntimeError as re: logger.error(f"System Error: {re}") print(f"🚫 System Error: {re}. Please ensure the system is initialized.") break # Exit on critical system errors except Exception as e: logger.error(f"An unexpected error occurred during interactive mode: {e}", exc_info=True) print(f"❌ An unexpected error occurred: {e}\n") def main() -> int: """Main entry point for the CrewAI Multi-Agent Helpdesk System application.""" parser = argparse.ArgumentParser(description="CrewAI Multi-Agent Helpdesk System") parser.add_argument("--issue", type=str, help="Submit a single IT issue as a string (e.g., 'My printer is not working').") parser.add_argument("--interactive", action="store_true", help="Run the system in interactive command-line mode.") parser.add_argument("--llm-url", default="http://localhost:5000", help="Base URL for the LLM API (e.g., Oobabooga text-generation-webui).") parser.add_argument("--model", default="phi-3-mini-q4", help="Name of the LLM model to use (e.g., 'phi-3-mini-q4').") parser.add_argument("--config", type=str, help="Path to a JSON configuration file for LLM settings.") args = parser.parse_args() # Load LLM configuration config = None if args.config: try: with open(args.config, 'r', encoding='utf-8') as f: config_data = json.load(f) config = LLMConfig(**config_data) logger.info(f"Loaded LLM configuration from '{args.config}'.") except FileNotFoundError: logger.error(f"Configuration file not found: '{args.config}'.") return 1 except json.JSONDecodeError: logger.error(f"Invalid JSON in configuration file: '{args.config}'.") return 1 except Exception as e: logger.error(f"Failed to load config file '{args.config}': {e}", exc_info=True) return 1 else: config = LLMConfig( base_url=args.llm_url, model_name=args.model ) logger.info(f"Using command-line provided LLM configuration: URL={args.llm_url}, Model={args.model}") # Initialize helpdesk system helpdesk = HelpdeskCrewAI(config) if not helpdesk.initialize(): logger.critical("🚨 Helpdesk system failed to initialize. Exiting.") return 1 try: if args.interactive: interactive_mode(helpdesk) elif args.issue: logger.info(f"Submitting issue from command line: '{args.issue}'") task_id = helpdesk.submit_issue(args.issue) print(f"\n✅ Issue submitted! Task ID: {task_id}") # Get and display result for command-line submission status_report = helpdesk.get_task_status(task_id) if status_report: print(f"\n
--- 📋 Final Report for {status_report['task_id']} ---
") print(f"Status: {status_report['status'].upper()}") print(f"User Input: {status_report['user_input']}") print(f"Final Outcome: {status_report['final_result']}") print("
---
-
---
-
---
-
---
-
---
-
---
-
---
-
---
-
---
-
---
-
---
\n") else: print("❌ Could not retrieve final task status.") else: # If no args, default to interactive mode for user convenience print("No arguments provided. Running in interactive mode. Use --help for options.") interactive_mode(helpdesk) except KeyboardInterrupt: logger.info("User interrupted the process.") print("\nOperation cancelled by user.") return 0 # Normal exit on user interrupt except Exception as e: logger.error(f"An unhandled error occurred in main execution: {e}", exc_info=True) print(f"❌ Critical error: {e}") return 1 return 0 if __name__ == "__main__": # Create a directory for task outputs if it doesn't exist os.makedirs("tasks", exist_ok=True) sys.exit(main()) Explanation of Changes and How to Use Them 1. Tool Instantiation and Structure Moved Tool Definitions: While your original placement was functional, I've clarified the structure by placing the custom BaseTool derived classes just before the HelpdeskCrewAI class. This makes them easier to find and manage. Explicit Dependencies: The __init__ methods of the custom tools (e.g., SearchKBTool(self.knowledge_base)) now explicitly take the required core module instances as arguments. This improves clarity and makes dependency injection more apparent. 2. HelpdeskCrewAI Class Enhancements Type Hinting: Added more type hints for better code readability and maintainability. Clearer __init__: Ensured that tool instances are created in __init__ so they are ready when _create_agents is called. Dynamic Crew Creation: The _create_crew method was removed because the Crew object is now instantiated inside submit_issue. This is crucial: each time you kickoff() a Crew, it processes a defined set of tasks. If you want a fresh run for each new issue, you should create a new Crew instance with the specific tasks for that issue. Improved Logging: Added more logger.debug calls within tool _run methods to help trace tool execution. 3. Agent Definitions Refined Backstories & Goals: I've slightly tweaked the backstory and goal for each agent to make their responsibilities even clearer, especially regarding when they should escalate or take action. Tool Assignment: Agents are now assigned tools more logically based on their roles. common_tools are shared, and then specialists get their specific diagnostic tools. allow_delegation Nuance: intake_specialist and escalation_manager have allow_delegation=False as their roles are to process and conclude/direct, not to pass tasks dynamically to another agent in the troubleshooting chain. tier1_generalist retains allow_delegation=True as they are the primary point for initial checks and can delegate to network_specialist or systems_specialist. network_specialist and systems_specialist are False for delegation here as they are meant to do their job and report back to escalation_manager. If they needed to, say, ask Tier 1 for more info, their allow_delegation could be True. 4. _create_tasks_for_issue (Now Integrated in submit_issue) Explicit Context for Tasks: Each task now explicitly uses the context parameter to define dependencies. For example, tier1_troubleshooting_task depends on intake_task. This tells CrewAI that the output of intake_task will be provided as context to tier1_troubleshooting_task. Conditional Logic via Agent Prompts: While CrewAI doesn't have explicit if/else branching for tasks within the Crew definition itself in its basic sequential process, the agents' prompts are designed to handle this. The network_troubleshooting_task and systems_troubleshooting_task prompts now explicitly state: "Only proceed if the Tier 1 Generalist explicitly escalates a [network/system] issue, or if the intake analysis clearly categorizes it as a [network/system] issue that Tier 1 could not fully address." This instructs the agent to self-regulate its execution based on the context it receives. Output Files: Added output_file to tasks. This is a powerful CrewAI feature that saves each task's final output to a specified file, making debugging and understanding the flow much easier. The escalation_review_task now consumes all previous task outputs. full_output=True in Crew.kickoff(): This provides a detailed dictionary of the final output and all intermediate task outputs, which is very useful for get_task_status to show a comprehensive report. More Specific expected_output: The expected_output fields are now more prescriptive, guiding the LLM on the exact format and content it should produce for better interoperability between tasks. 5. Interactive Mode and main Function Enhanced Output in Interactive Mode: When an issue is submitted, the interactive mode now fetches and displays not only the final result but also snippets of the outputs from all intermediate tasks, giving a much clearer picture of the agents' work. Error Handling in main: More specific try-except blocks are added in main for configuration loading and general execution. Default to Interactive: If no command-line arguments are provided, the system now defaults to interactive mode for ease of use. Output Directory: Added os.makedirs("tasks", exist_ok=True) at the bottom to ensure the tasks directory exists for the output_file feature. How to Get Back on Track with This Code Replace your main_crewai.py content with the updated code provided above. Ensure core/llm_interface.py, core/crewai_llm.py, core/knowledge_base_loader.py, tools/network_tools.py, tools/system_tools.py, and tools/general_tools.py are correctly implemented and accessible in your project structure as expected by the sys.path.insert(0, ...) line. Verify your LLM setup: Make sure your Oobabooga LLM server is running at the specified llm-url (default: http://localhost:5000) and the model name is correct. Populate your Knowledge Base: Ensure your KnowledgeBaseLoader is able to find and load your knowledge base content, as the agents heavily rely on search_knowledge_base and get_troubleshooting_guide. Run the script: Interactive Mode: python3 main_crewai.py --interactive Single Issue: python3 main_crewai.py --issue "My internet is not working, I can't access any websites." With Config File: python3 main_crewai.py --config my_llm_config.json --interactive (where my_llm_config.json contains {"base_url": "http://localhost:5000", "model_name": "phi-3-mini-q4", "max_tokens": 1024, "temperature": 0.7, "timeout": 60}) This revised structure will provide a more logical flow, better traceability of agent actions, and a more robust foundation for your multi-agent helpdesk system. Good luck!


## Related

### Projects

- [[nodes/projects/homelab-stack|Homelab Stack]]
- [[nodes/projects/private-ai-consulting|Private AI Consulting]]

### Topics

- [[nodes/topics/tech/ai-tools|Ai Tools]]
