# Personal Assistant

This project is an on‑prem personal AI assistant. Phase 1 provides the
foundation for running a local model through [Ollama](https://ollama.ai/).

## Setup

1. Install Python 3.11 or later and create a virtual environment::

    python3 -m venv .venv
    source .venv/bin/activate
    pip install -r requirements.txt

2. Install Ollama and download the Llama 3.1 8B model. Follow the
   instructions at <https://ollama.ai>.

3. Update `configs/config.yaml` if your Ollama service runs on a different
   host or port.

4. Test the connection:

    python -m src.ollama_service

This should print the model's response to a simple prompt.
