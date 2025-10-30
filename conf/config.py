import yaml
from pathlib import Path

def load_config():
    """Load configuration from YAML file"""
    config_path = Path(__file__).parent / "config.yml"
    
    if not config_path.exists():
        raise FileNotFoundError(f"Configuration file not found: {config_path}")
    
    with open(config_path, 'r', encoding='utf-8') as file:
        config = yaml.safe_load(file)
        
    return config

# Load configuration
config = load_config()

# Telegram Bot Token
TOKEN = config['telegram']['token']

# MEXC API
MEXC_API_KEY = config['mexc']['api_key']
MEXC_SECRET_KEY = config['mexc']['secret_key']

# BitMart API
BITMART_API_KEY = config['bitmart']['api_key']
BITMART_SECRET_KEY = config['bitmart']['secret_key']