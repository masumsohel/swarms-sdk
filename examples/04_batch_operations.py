"""
Batch Operations Example

This example demonstrates how to run multiple agents and swarms in batch mode.
"""

import asyncio
import os
from swarms_client import SwarmsClient
from swarms_client.models import AgentSpec


async def main():
    api_key = os.getenv("SWARMS_API_KEY", "your-api-key-here")

    async with SwarmsClient(api_key=api_key) as client:
        try:
            # Batch Agent Operations
            agent_configs = [
                {
                    "agent_name": "market_researcher",
                    "task": "Research market trends in AI",
                    "model_name": "gpt-4",
                    "temperature": 0.7,
                    "max_tokens": 1000,
                    "role": "researcher",
                },
                {
                    "agent_name": "tech_analyst",
                    "task": "Analyze emerging technologies",
                    "model_name": "gpt-4",
                    "temperature": 0.7,
                    "max_tokens": 1000,
                    "role": "analyst",
                },
            ]

            agent_results = await client.run_agent_batch(agent_configs)
            print("Batch Agent Results:", agent_results)

            # Batch Swarm Operations
            swarm_configs = [
                {
                    "name": "market_analysis_team",
                    "task": "Analyze global market trends",
                    "agents": [
                        AgentSpec(
                            agent_name="researcher",
                            model_name="gpt-4",
                            role="researcher",
                        ).model_dump(),
                        AgentSpec(
                            agent_name="analyst", model_name="gpt-4", role="analyst"
                        ).model_dump(),
                    ],
                    "max_loops": 1,
                },
                {
                    "name": "tech_review_team",
                    "task": "Review latest tech innovations",
                    "agents": [
                        AgentSpec(
                            agent_name="tech_expert", model_name="gpt-4", role="expert"
                        ).model_dump(),
                        AgentSpec(
                            agent_name="writer", model_name="gpt-4", role="writer"
                        ).model_dump(),
                    ],
                    "max_loops": 1,
                },
            ]

            swarm_results = await client.run_swarm_batch(swarm_configs)
            print("Batch Swarm Results:", swarm_results)

        except Exception as e:
            print(f"Error in batch operations: {e}")


if __name__ == "__main__":
    asyncio.run(main())
