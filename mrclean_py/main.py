import os

import yaml

CONFIG_FILE_PATH = "mrclean.config"


def check_config_file_exists() -> bool:
    if not os.path.exists(CONFIG_FILE_PATH):
        print(
            f'You should have a configuration file named "{CONFIG_FILE_PATH}" in this folder.'
        )
        return False
    return True


def load_yaml_config() -> dict:
    try:
        with open(CONFIG_FILE_PATH, "r") as f:
            return yaml.safe_load(f)
    except Exception as e:
        print(f"Error while loading yaml config file:\n{e}")
        return None


# Called directly when using the command "mrclean-py" after installing the package
# See pyproject.toml
def main():
    if not check_config_file_exists():
        exit(0)
    config = load_yaml_config()
    if config is None:
        exit(0)
