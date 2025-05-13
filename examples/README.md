# Swarms API Examples

This directory contains a collection of examples demonstrating various features and capabilities of the Swarms API. Each example is designed to showcase different aspects of the API and provide practical use cases for implementation.

## Directory Structure

- `single_agent/`: Examples of using individual agents for specific tasks
- `batch_agents/`: Examples of running multiple agents in parallel
- `multi_agent_systems/`: Examples of collaborative agent systems
- `swarms/`: Examples of swarm-based operations
- `advanced_use_cases/`: Complex examples combining multiple features

## Prerequisites

Before running these examples, make sure you have:

1. Installed the Swarms API client:
```bash
pip install swarms-client
```

2. Set up your API key:
```bash
export SWARMS_API_KEY='your-api-key'
```

## Examples Overview

### Single Agent Examples
- `basic_agent.py`: Demonstrates basic usage of a single agent for text analysis
- Shows how to initialize the client and run simple tasks

### Batch Agents Examples
- `parallel_analysis.py`: Shows how to run multiple agents in parallel
- Demonstrates efficient processing of multiple tasks simultaneously

### Multi-Agent Systems Examples
- `collaborative_research.py`: Demonstrates a team of agents working together
- Shows how to create specialized agents for different aspects of a task

### Swarm Examples
- `batch_swarms.py`: Shows how to run multiple swarms in parallel
- Demonstrates managing complex tasks with multiple agent teams

### Advanced Use Cases
- `autonomous_research_platform.py`: A comprehensive research platform using multiple swarms
- `custom_system_prompts.py`: Demonstrates using custom system prompts and role definitions
- `agent_behaviors.py`: Shows advanced agent behaviors and interaction patterns

## Advanced Features Demonstrated

### Custom System Prompts
- Defining specialized agent roles with custom prompts
- Role-specific behavior and expertise
- Context-aware responses

### Advanced Agent Behaviors
- Structured debate patterns
- Chain-of-thought reasoning
- Memory and context management
- Adaptive behavior based on feedback
- Consensus building mechanisms

### Interaction Patterns
- Debate-style interactions with moderator
- Sequential reasoning steps
- Cross-validation between agents
- Evidence-based argumentation
- Collaborative problem-solving

### Swarm Behaviors
- Custom collaboration styles
- Consensus requirements
- Cross-validation mechanisms
- Round-table discussions
- Hierarchical organization

## Running the Examples

Each example can be run directly using Python:

```bash
python examples/single_agent/basic_agent.py
```

For advanced examples:
```bash
python examples/advanced_use_cases/custom_system_prompts.py
python examples/advanced_use_cases/agent_behaviors.py
```

Make sure to replace the API key in the examples with your own or set it as an environment variable.

## Best Practices

The examples demonstrate several best practices:

1. Proper error handling and logging
2. Efficient resource management with async/await
3. Structured organization of complex tasks
4. Proper cleanup of resources
5. Type hints for better code maintainability
6. Custom system prompts for specialized roles
7. Advanced interaction patterns
8. Context and memory management
9. Evidence-based reasoning
10. Collaborative consensus building

## Contributing

Feel free to contribute additional examples or improvements to existing ones. Make sure to:

1. Follow the existing code structure
2. Include proper documentation
3. Add error handling
4. Test your examples thoroughly
5. Document any new features or patterns

## License

These examples are provided under the MIT License. See the LICENSE file in the root directory for details. 