import yaml

def get_config(config_path):
    with open(config_path) as fp:
        return yaml.load(fp, yaml.FullLoader)

config = get_config('CONFIG.yml')