# Swarms Client Examples

This directory contains example scripts demonstrating various features of the Swarms Client SDK.

## Prerequisites

Before running these examples, make sure you have:

1. Installed the Swarms Client SDK
2. Set up your API key (either as an environment variable or directly in the code)
3. Python 3.7+ installed

## Setting up your environment

```bash
# Set your API key as an environment variable
export SWARMS_API_KEY="your-api-key-here"

# Install required packages
pip install swarms-client
```

## Directory Structure

The examples are organized into the following directories:

### Tools (`/tools`)
- `tools.py` - Common tools that can be used by agents:
  - Search Tool
  - Code Executor Tool
  - API Creator Tool

### Single Agent Examples (`/single_agent`)
1. **Research Assistant** (`research_assistant.py`)
   - Demonstrates using the search tool
   - Performs research on specific topics
   - Provides comprehensive analysis

2. **Code Developer** (`code_developer.py`)
   - Uses the code executor tool
   - Implements and tests algorithms
   - Provides documented code solutions

### Multi-Agent Examples (`/multi_agent`)
1. **Financial Analysis Swarm** (`financial_analysis_swarm.py`)
   - Multiple agents analyzing financial data
   - Includes data analyzer, risk analyst, and strategy validator
   - Uses both search and code execution tools

2. **Medical Analysis Swarm** (`medical_analysis_swarm.py`)
   - Specialized medical research and analysis
   - Includes clinical analyst, researcher, and protocol validator
   - Focuses on treatment analysis and recommendations

## Running the Examples

Each example can be run directly using Python:

```bash
# Single Agent Examples
python single_agent/research_assistant.py
python single_agent/code_developer.py

# Multi-Agent Examples
python multi_agent/financial_analysis_swarm.py
python multi_agent/medical_analysis_swarm.py
```

## Notes

- Make sure to replace "your-api-key-here" with your actual Swarms API key
- Each example includes error handling and proper resource cleanup
- The examples use async/await syntax for better performance
- All examples use the context manager (`async with`) to ensure proper cleanup
- Tools can be combined and customized for specific use cases

## Additional Resources

- [Swarms API Documentation](https://docs.swarms.world)
- [Python SDK Documentation](https://github.com/swarms-world/swarms-sdk)
- [Tools Documentation](https://docs.swarms.world/tools) 