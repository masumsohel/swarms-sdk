"""
Code Developer Example

This example demonstrates a single agent that acts as a code developer
using the code executor tool to write and test code.
"""

import asyncio
import os
import json
from swarms_client import SwarmsClient
from examples.tools.tools import SwarmTools


async def run_code_developer():
    api_key = os.getenv("SWARMS_API_KEY", "your-api-key-here")

    async with SwarmsClient(api_key=api_key) as client:
        # Configure the code developer with code executor tool
        result = await client.run_agent(
            agent_name="code_developer",
            task="""Create a Python function that implements a binary search algorithm.
            The function should be well-documented and include test cases.""",
            model_name="gpt-4",
            temperature=0.7,
            max_tokens=2000,
            system_prompt="""You are an expert software developer specializing in algorithm implementation.
            Use the code executor tool to write, test, and debug code.
            Ensure your code is efficient, well-documented, and follows best practices.
            Include comprehensive test cases to verify functionality.""",
            description="A code developer that implements and tests algorithms",
            role="developer",
            max_loops=2,  # Allow for write-test-debug cycle
            tools_dictionary=[SwarmTools.code_executor()],
        )

        print("\nCode Developer Results:")
        print(json.dumps(result, indent=2))
        return result


if __name__ == "__main__":
    asyncio.run(run_code_developer())
