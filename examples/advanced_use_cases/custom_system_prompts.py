"""
Custom System Prompts Example

This example demonstrates how to use custom system prompts and role definitions
to create specialized agents with specific behaviors and expertise.
"""

import asyncio
from swarms_client import SwarmsClient


# Example system prompts for different specialist roles
MEDICAL_EXPERT_PROMPT = """You are an expert medical researcher with extensive knowledge in clinical studies,
medical terminology, and healthcare systems. Your responses should be evidence-based,
reference current medical literature, and maintain professional medical terminology while
still being accessible to an informed audience. Consider patient privacy, medical ethics,
and current best practices in all analyses."""

TECHNICAL_ARCHITECT_PROMPT = """You are a senior technical architect with expertise in distributed systems,
cloud architecture, and system design. Your analysis should focus on scalability,
reliability, security, and performance. Consider industry best practices, design patterns,
and trade-offs in your recommendations. Use technical terminology appropriately and
provide clear architectural reasoning."""

DATA_SCIENTIST_PROMPT = """You are a data scientist specializing in machine learning and statistical analysis.
Your approach should emphasize statistical rigor, proper methodology, and data quality.
Consider aspects like data bias, model validation, and statistical significance in your
analysis. Explain complex concepts clearly while maintaining technical accuracy."""


async def run_specialist_analysis(client, topic: str, system_prompt: str, role: str):
    """Run analysis with a specialist agent using a custom system prompt."""
    result = await client.run_agent(
        agent_name=f"{role}_specialist",
        task=topic,
        model_name="gpt-4",
        system_prompt=system_prompt,
        temperature=0.7,
        max_tokens=1500,
        role_context={
            "expertise_level": "expert",
            "domain": role,
            "response_style": "analytical",
        },
    )
    return result


async def main():
    # Initialize the client
    async with SwarmsClient() as client:
        # Example topic for analysis
        topic = """
        Analyze the potential impact of large language models in clinical diagnosis,
        considering technical implementation, data privacy, and clinical validation.
        """

        # Run analysis with different specialists
        specialists = [
            ("Medical Expert", MEDICAL_EXPERT_PROMPT, "medical"),
            ("Technical Architect", TECHNICAL_ARCHITECT_PROMPT, "technical"),
            ("Data Scientist", DATA_SCIENTIST_PROMPT, "data"),
        ]

        print("\nMulti-Perspective Analysis:")
        for title, prompt, role in specialists:
            print(f"\n{title} Analysis:")
            result = await run_specialist_analysis(client, topic, prompt, role)
            print(result)

        # Create a collaborative swarm with custom system prompts
        swarm = await client.create_swarm(
            name="healthcare_ai_analysis",
            task=topic,
            description="Multi-disciplinary analysis of AI in healthcare",
            agents=[
                {
                    "agent_name": "medical_expert",
                    "model_name": "gpt-4",
                    "role": "medical_specialist",
                    "system_prompt": MEDICAL_EXPERT_PROMPT,
                    "task": "Analyze medical implications and requirements",
                },
                {
                    "agent_name": "tech_architect",
                    "model_name": "gpt-4",
                    "role": "tech_specialist",
                    "system_prompt": TECHNICAL_ARCHITECT_PROMPT,
                    "task": "Evaluate technical implementation aspects",
                },
                {
                    "agent_name": "data_scientist",
                    "model_name": "gpt-4",
                    "role": "data_specialist",
                    "system_prompt": DATA_SCIENTIST_PROMPT,
                    "task": "Assess data and model requirements",
                },
            ],
            max_loops=2,
            swarm_type="collaborative",
            service_tier="standard",
            swarm_behavior={
                "collaboration_style": "round_table",
                "consensus_required": True,
                "cross_validation": True,
            },
        )

        # Run the swarm
        print("\nCollaborative Swarm Analysis:")
        result = await client.run_swarm(swarm["swarm_id"])
        print(result)

        # Get detailed interaction logs
        logs = await client.get_swarm_logs(swarm["swarm_id"])
        print("\nAgent Interaction Logs:")
        for log in logs:
            print(f"\n{log['agent_name']} ({log['role']}):")
            print(f"Action: {log.get('action_type', 'unknown')}")
            print(f"Message: {log['message']}")


if __name__ == "__main__":
    asyncio.run(main())
