# AI Log Analysis Agent

A Python-based AI agent that analyzes log files using LangChain and a locally running Llama 3.2 model through Ollama.

## Features

- Reads log files and counts `INFO` and `DEBUG` entries.
- Uses LangChain tools to perform log analysis.
- Retrieves Docker container information through the Docker CLI.

## Tech Stack

- Python
- LangChain
- Ollama
- Llama 3.2
- Docker

## Prerequisites

- Python
- Ollama installed and running
- Llama 3.2 model downloaded
- Docker installed for container inspection

## Setup

Install the Python dependencies:

```bash
pip install -r requirements.txt
```

Download the model:

```bash
ollama pull llama3.2
```

## Run

Start Ollama, then run:

```bash
python "AI AGENT.py"
```

The agent uses helper functions defined in `fifteenthsept.py`.

## Notes

This project is a learning project exploring Python, local LLMs, LangChain tools, log analysis, and Docker integration.
