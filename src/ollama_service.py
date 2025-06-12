import requests
import yaml
from pathlib import Path


def load_config(config_path: str | Path = 'configs/config.yaml') -> dict:
    """Load YAML configuration."""
    with open(config_path, 'r', encoding='utf-8') as f:
        return yaml.safe_load(f)


def generate(prompt: str, config: dict | None = None) -> str:
    """Send a prompt to the Ollama API and return the response."""
    cfg = config or load_config()
    url = cfg.get('ollama_base_url', 'http://localhost:11434') + '/api/generate'
    model = cfg.get('model', 'llama3-8b')
    response = requests.post(url, json={'model': model, 'prompt': prompt})
    response.raise_for_status()
    data = response.json()
    return data.get('response', '')


if __name__ == '__main__':
    cfg = load_config()
    answer = generate('Hello, how are you?', config=cfg)
    print(answer)
