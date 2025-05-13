"""
Create and Run Swarm Example

This example demonstrates how to create and run a swarm with multiple agents.
"""

import asyncio
import os
from swarms_client import SwarmsClient
from swarms_client.models import AgentSpec


async def main():
    api_key = os.getenv("SWARMS_API_KEY", "your-api-key-here")

    async with SwarmsClient(api_key=api_key) as client:
        # Define agents for the swarm
        agents = [
            AgentSpec(
                agent_name="researcher",
                model_name="gpt-4",
                role="researcher",
                system_prompt="You are a research expert who analyzes data thoroughly.",
                max_tokens=1000,
                temperature=0.7,
            ),
            AgentSpec(
                agent_name="writer",
                model_name="gpt-4",
                role="writer",
                system_prompt="You are a skilled writer who creates clear summaries.",
                max_tokens=1000,
                temperature=0.7,
            ),
        ]

        try:
            # Create and run a swarm
            swarm_result = await client.create_swarm(
                name="research_team",
                task="Analyze the latest trends in AI and create a summary report.",
                agents=agents,
                description="A swarm that researches and summarizes AI trends",
                max_loops=2,
                return_history=True,
                service_tier="standard",
                swarm_type="SequentialWorkflow",
            )
            print("Swarm Result:", swarm_result)

            # Get swarm logs
            if "swarm_id" in swarm_result:
                logs = await client.get_swarm_logs(swarm_result["swarm_id"])
                print("Swarm Logs:", logs)

        except Exception as e:
            print(f"Error running swarm: {e}")


if __name__ == "__main__":
    asyncio.run(main())
