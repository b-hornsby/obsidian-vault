---
id: 079502
source: GEMINI
date: 2025-07-19
tags: ['ai-helpdesk', 'config-file', 'python', 'dotenv', 'oobabooga']
category: coding
sentiment: building
resolution: partial
linked_projects: ['nodes/projects/homelab-stack.md']
linked_nodes: ['nodes/people/bryan.md', 'nodes/topics/tech/coding.md']
summary: Bryan is providing the code for his config.py file, which includes settings for the LLM, knowledge base, and safety configurations for his AI helpdesk project.
---
# this is for config.py: import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class Config:
    """Configuration settings for the AI-Powered Hybrid Helpdesk"""
    
    # LLM Configuration (Oobabooga Text Generation WebUI)
    LLM_PROVIDER = "Oobabooga Text Generation WebUI"
    LLM_MODEL_NAME = "Meta-Llama-3.1-8B-Instruct-Q4_K_M.gguf"
    LLM_API_ENDPOINT = "http://0.0.0.0:5000/v1"
    LLM_API_TYPE = "openai"
    LLM_API_KEY = os.getenv("OOBABOOGA_API_KEY", "dummy-key")  # Oobabooga typically doesn't require a real key
    
    # Knowledge Base Configuration
    KNOWLEDGE_BASE_PATH = "./data/"
    
    # Web Search Configuration (optional)
    SERPER_API_KEY = os.getenv("SERPER_API_KEY", "")
    
    # Safety Configuration
    ENABLE_REAL_COMMANDS = False  # Set to True only in controlled environments
    ALLOWED_SOFTWARE_INSTALLATIONS = [
        "google-chrome",
        "vlc-player",
        "7zip",
        "notepad-plus-plus"
    ]
    
    # Allowed network diagnostic commands
    ALLOWED_NETWORK_COMMANDS = [
        "ping",
        "ipconfig",
        "nslookup",
        "tracert",
        "netstat",
        "arp"
    ]
    
    # Allowed system maintenance actions
    ALLOWED_SYSTEM_ACTIONS = [
        "clear_temp_files",
        "check_disk_space",
        "restart_print_spooler",
        "get_event_logs",
        "check_services"
    ]
    
    # Project Information
    PROJECT_NAME = "AI-Powered Hybrid Helpdesk"
    PROJECT_DESCRIPTION = "A multi-agent workflow system designed using CrewAI to function as a real-world hybrid IT helpdesk"
    
    @classmethod
    def get_llm_config(cls):
        """Get LLM configuration for CrewAI"""
        return {
            "api_key": cls.LLM_API_KEY,
            "base_url": cls.LLM_API_ENDPOINT,
            "model": cls.LLM_MODEL_NAME,
            "temperature": 0.7,
            "max_tokens": 8192
        } 

### USER
this is for config.py: import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class Config:
    """Configuration settings for the AI-Powered Hybrid Helpdesk"""
    
    # LLM Configuration (Oobabooga Text Generation WebUI)
    LLM_PROVIDER = "Oobabooga Text Generation WebUI"
    LLM_MODEL_NAME = "Meta-Llama-3.1-8B-Instruct-Q4_K_M.gguf"
    LLM_API_ENDPOINT = "http://0.0.0.0:5000/v1"
    LLM_API_TYPE = "openai"
    LLM_API_KEY = os.getenv("OOBABOOGA_API_KEY", "dummy-key")  # Oobabooga typically doesn't require a real key
    
    # Knowledge Base Configuration
    KNOWLEDGE_BASE_PATH = "./data/"
    
    # Web Search Configuration (optional)
    SERPER_API_KEY = os.getenv("SERPER_API_KEY", "")
    
    # Safety Configuration
    ENABLE_REAL_COMMANDS = False  # Set to True only in controlled environments
    ALLOWED_SOFTWARE_INSTALLATIONS = [
        "google-chrome",
        "vlc-player",
        "7zip",
        "notepad-plus-plus"
    ]
    
    # Allowed network diagnostic commands
    ALLOWED_NETWORK_COMMANDS = [
        "ping",
        "ipconfig",
        "nslookup",
        "tracert",
        "netstat",
        "arp"
    ]
    
    # Allowed system maintenance actions
    ALLOWED_SYSTEM_ACTIONS = [
        "clear_temp_files",
        "check_disk_space",
        "restart_print_spooler",
        "get_event_logs",
        "check_services"
    ]
    
    # Project Information
    PROJECT_NAME = "AI-Powered Hybrid Helpdesk"
    PROJECT_DESCRIPTION = "A multi-agent workflow system designed using CrewAI to function as a real-world hybrid IT helpdesk"
    
    @classmethod
    def get_llm_config(cls):
        """Get LLM configuration for CrewAI"""
        return {
            "api_key": cls.LLM_API_KEY,
            "base_url": cls.LLM_API_ENDPOINT,
            "model": cls.LLM_MODEL_NAME,
            "temperature": 0.7,
            "max_tokens": 8192
        } 

### GEMINI
Please provide the screenshot of the errors you're encountering. Without seeing the exact error messages and their line/column numbers, I can't effectively diagnose the issue. The config.py file you provided looks structurally sound for managing application settings. The LLM_API_KEY is correctly set to pull from OOBABOOGA_API_KEY or default to "dummy-key", which aligns with our .env discussion. The get_llm_config class method also correctly formats the dictionary for CrewAI's LLM initialization. Once you share the screenshot, I'll be able to pinpoint the problem and guide you through fixing it.


## Related

### Projects

- [[nodes/projects/homelab-stack|Homelab Stack]]

### Topics

- [[nodes/topics/tech/coding|Coding]]
- [[nodes/topics/tech/ai-tools|Ai Tools]]
