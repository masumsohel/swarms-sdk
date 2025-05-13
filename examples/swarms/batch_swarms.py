"""
Batch Swarm Processing Example

This example demonstrates how to run multiple swarms in parallel, each handling
a different complex task with its own team of specialized agents.
"""

import asyncio
from swarms_client import SwarmsClient


async def main():
    # Initialize the client
    async with SwarmsClient() as client:
        # Define multiple swarms for different complex tasks
        swarms = [
            {
                "name": "market_research",
                "task": "Analyze market trends for electric vehicles in 2024",
                "description": "Market analysis team for EV industry",
                "agents": [
                    {
                        "agent_name": "market_analyst",
                        "model_name": "gpt-4",
                        "role": "analyst",
                        "task": "Analyze market data and trends",
                    },
                    {
                        "agent_name": "competitor_analyst",
                        "model_name": "gpt-4",
                        "role": "researcher",
                        "task": "Research competitor strategies",
                    },
                ],
                "max_loops": 2,
                "swarm_type": "analytical",
            },
            {
                "name": "content_creation",
                "task": "Create a social media campaign for a new tech product",
                "description": "Creative team for social media content",
                "agents": [
                    {
                        "agent_name": "content_strategist",
                        "model_name": "gpt-4",
                        "role": "strategist",
                        "task": "Develop content strategy",
                    },
                    {
                        "agent_name": "copywriter",
                        "model_name": "gpt-4",
                        "role": "writer",
                        "task": "Write engaging copy",
                    },
                ],
                "max_loops": 2,
                "swarm_type": "creative",
            },
            {
                "name": "code_review",
                "task": "Review and optimize a Python web application",
                "description": "Code review and optimization team",
                "agents": [
                    {
                        "agent_name": "code_analyzer",
                        "model_name": "gpt-4",
                        "role": "analyzer",
                        "task": "Analyze code quality and structure",
                    },
                    {
                        "agent_name": "performance_optimizer",
                        "model_name": "gpt-4",
                        "role": "optimizer",
                        "task": "Suggest performance improvements",
                    },
                ],
                "max_loops": 2,
                "swarm_type": "technical",
            },
        ]

        # Run all swarms in parallel
        results = await client.run_swarm_batch(swarms)

        # Process results from each swarm
        for i, result in enumerate(results):
            print(f"\nSwarm {i+1} ({swarms[i]['name']}) Results:")
            print(result)


if __name__ == "__main__":
    asyncio.run(main())
