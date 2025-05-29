import json
import argparse

def load_config(path):
    """Load JSON config from the given file path."""
    with open(path, 'r') as file:
        return json.load(file)

def main():
    parser = argparse.ArgumentParser(description="Run the local LLM using the config file.")
    parser.add_argument('--config', default='config.json', help='Path to the config file')
    args = parser.parse_args()

    config = load_config(args.config)

    print("Configuration loaded:")
    for key, value in config.items():
        print(f"  {key}: {value}")

    # Here’s where you’d add your code to load and run your LLM using the settings above.
    # For now, this script just reads and shows the config.

if __name__ == "__main__":
    main()
