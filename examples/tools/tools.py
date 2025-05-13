"""
Swarms Tools Module

This module provides common tools that can be used by agents in the Swarms ecosystem.
"""

from typing import Any, Dict, List


class SwarmTools:
    @staticmethod
    def search_tool() -> Dict[str, Any]:
        """
        Create a search tool configuration for agents.
        """
        return {
            "name": "search",
            "description": "Search the internet for information",
            "parameters": {
                "type": "object",
                "properties": {
                    "query": {"type": "string", "description": "The search query"}
                },
                "required": ["query"],
            },
        }

    @staticmethod
    def code_executor() -> Dict[str, Any]:
        """
        Create a code execution tool configuration for agents.
        """
        return {
            "name": "code_executor",
            "description": "Execute code in various programming languages",
            "parameters": {
                "type": "object",
                "properties": {
                    "code": {"type": "string", "description": "The code to execute"},
                    "language": {
                        "type": "string",
                        "description": "Programming language (python, javascript, etc.)",
                    },
                },
                "required": ["code", "language"],
            },
        }

    @staticmethod
    def api_creator() -> Dict[str, Any]:
        """
        Create an API creation tool configuration for agents.
        """
        return {
            "name": "api_creator",
            "description": "Create API endpoints and specifications",
            "parameters": {
                "type": "object",
                "properties": {
                    "endpoint": {"type": "string", "description": "API endpoint path"},
                    "method": {
                        "type": "string",
                        "description": "HTTP method (GET, POST, etc.)",
                    },
                    "request_schema": {
                        "type": "object",
                        "description": "JSON schema for request",
                    },
                    "response_schema": {
                        "type": "object",
                        "description": "JSON schema for response",
                    },
                },
                "required": ["endpoint", "method"],
            },
        }

    @staticmethod
    def get_all_tools() -> List[Dict[str, Any]]:
        """
        Get all available tools configurations.
        """
        return [
            SwarmTools.search_tool(),
            SwarmTools.code_executor(),
            SwarmTools.api_creator(),
        ]
