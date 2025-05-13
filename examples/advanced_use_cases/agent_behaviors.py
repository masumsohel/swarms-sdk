"""
Advanced Agent Behaviors Example

This example demonstrates advanced agent behaviors including:
1. Custom interaction patterns
2. Memory and context management
3. Adaptive behavior based on feedback
4. Chain-of-thought reasoning
5. Debate and consensus building
"""

import asyncio
from typing import List, Dict, Any
from swarms_client import SwarmsClient


# Define different interaction patterns
DEBATE_PATTERN = {
    "format": "debate",
    "steps": [
        "present_argument",
        "counter_argument",
        "evidence_analysis",
        "synthesis",
        "consensus",
    ],
    "rules": {
        "require_evidence": True,
        "allow_rebuttals": True,
        "consensus_threshold": 0.8,
    },
}

CHAIN_OF_THOUGHT_PATTERN = {
    "format": "reasoning",
    "steps": [
        "initial_thoughts",
        "deeper_analysis",
        "consideration_of_alternatives",
        "final_conclusion",
    ],
    "rules": {
        "show_work": True,
        "explain_reasoning": True,
        "consider_edge_cases": True,
    },
}


async def create_debate_swarm(
    client, topic: str, positions: List[str]
) -> Dict[str, Any]:
    """Create a swarm of agents engaged in structured debate."""
    agents = []
    for i, position in enumerate(positions):
        agents.append(
            {
                "agent_name": f"debater_{i+1}",
                "model_name": "gpt-4",
                "role": "debate_participant",
                "task": f"Argue position: {position}",
                "system_prompt": f"""You are a logical debater focusing on position: {position}.
            Use evidence-based arguments, acknowledge valid counter-points, and work
            towards finding common ground while maintaining intellectual rigor.""",
                "behavior": {
                    "style": "analytical",
                    "assertiveness": 0.7,
                    "flexibility": 0.6,
                },
            }
        )

    # Add a moderator agent
    agents.append(
        {
            "agent_name": "moderator",
            "model_name": "gpt-4",
            "role": "debate_moderator",
            "task": "Guide the debate and facilitate consensus building",
            "system_prompt": """You are an impartial moderator. Guide the discussion,
        ensure fair participation, identify areas of agreement and disagreement,
        and help synthesize conclusions. Maintain focus and productive dialogue.""",
            "behavior": {"style": "neutral", "assertiveness": 0.5, "flexibility": 0.8},
        }
    )

    return await client.create_swarm(
        name="structured_debate",
        task=topic,
        description="A structured debate with multiple perspectives",
        agents=agents,
        max_loops=4,
        swarm_type="debate",
        interaction_pattern=DEBATE_PATTERN,
        service_tier="standard",
    )


async def run_chain_of_thought_analysis(
    client, topic: str, context: Dict[str, Any]
) -> Dict[str, Any]:
    """Run an analysis using chain-of-thought reasoning."""
    return await client.run_agent(
        agent_name="reasoning_agent",
        task=topic,
        model_name="gpt-4",
        system_prompt="""You are an analytical thinker who breaks down complex
        problems step by step. Show your reasoning process explicitly, consider
        multiple approaches, and explain why you choose certain paths over others.""",
        interaction_pattern=CHAIN_OF_THOUGHT_PATTERN,
        context=context,
        temperature=0.7,
        max_tokens=2000,
    )


async def main():
    # Initialize the client
    async with SwarmsClient() as client:
        # Example 1: Structured Debate
        debate_topic = """
        Should artificial intelligence systems be allowed to make autonomous decisions
        in critical healthcare scenarios without human oversight?
        """

        positions = [
            "Full autonomy with robust safeguards",
            "Hybrid approach with human supervision",
            "Restricted to advisory role only",
        ]

        print("\nStructured Debate Example:")
        debate_swarm = await create_debate_swarm(client, debate_topic, positions)
        debate_result = await client.run_swarm(debate_swarm["swarm_id"])

        print("\nDebate Results:")
        print(debate_result)

        # Get and display debate interaction logs
        debate_logs = await client.get_swarm_logs(debate_swarm["swarm_id"])
        print("\nDebate Process:")
        for log in debate_logs:
            print(f"\n{log['agent_name']} ({log['role']}):")
            print(f"Step: {log.get('debate_step', 'unknown')}")
            print(f"Argument: {log['message']}")

        # Example 2: Chain of Thought Analysis
        analysis_topic = """
        Analyze the ethical implications of using predictive AI models for criminal
        sentencing recommendations.
        """

        context = {
            "relevant_cases": ["Case A", "Case B", "Case C"],
            "current_practices": "Description of current practices...",
            "known_biases": ["Bias 1", "Bias 2"],
            "success_metrics": ["Metric 1", "Metric 2"],
        }

        print("\nChain of Thought Analysis:")
        cot_result = await run_chain_of_thought_analysis(
            client, analysis_topic, context
        )

        print("\nReasoning Process:")
        for step in cot_result.get("reasoning_steps", []):
            print(f"\nStep: {step['name']}")
            print(f"Reasoning: {step['explanation']}")
            print(f"Confidence: {step['confidence']}")


if __name__ == "__main__":
    asyncio.run(main())
