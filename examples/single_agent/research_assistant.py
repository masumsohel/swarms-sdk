"""
Research Assistant Example

This example demonstrates a single agent that acts as a research assistant
using the search tool to gather information.
"""

import asyncio
import os
from swarms_client import SwarmsClient
from examples.tools.tools import SwarmTools
import json


async def run_research_assistant():
    api_key = os.getenv("SWARMS_API_KEY", "your-api-key-here")

    async with SwarmsClient(api_key=api_key) as client:
        # Configure the research assistant with search tool
        result = await client.run_agent(
            agent_name="research_assistant",
            task="Research the latest advancements in quantum computing and summarize key findings",
            model_name="gpt-4",
            temperature=0.7,
            max_tokens=2000,
            system_prompt="""You are an expert research assistant specializing in quantum computing.
            Use the search tool to gather current information and provide comprehensive analysis.
            Focus on practical applications and breakthrough discoveries.""",
            description="A research assistant that gathers and analyzes information about quantum computing",
            role="researcher",
            max_loops=1,
            tools_dictionary=[SwarmTools.search_tool()],
        )

        print("\nResearch Assistant Results:")
        print(json.dumps(result, indent=2))
        return result


if __name__ == "__main__":
    asyncio.run(run_research_assistant())
