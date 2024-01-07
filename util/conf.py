import os

from ruamel.yaml import YAML

from util.log import get_logger

env = os.getenv("ENV", "dev")
model = os.getenv("MODEL", "default")
yaml = YAML()
logger = get_logger("util.conf")
logger.info(f"[ENV] {env}")


def read_yaml(yaml_path: str) -> dict:
    with open(yaml_path, "r") as f_yaml:
        datas = yaml.load(f_yaml)
    return datas


def write_yaml(data: any, yaml_path: str) -> None:
    with open(yaml_path, "w") as f_yaml:
        yaml.dump(data, f_yaml)


def get_conf() -> dict:
    if env == "dev":
        conf_path = f"./conf/{model}.yaml"
    else:
        conf_path = f"./conf/{model}.{env}.yaml"
    conf_data = read_yaml(conf_path)
    conf_data["env"] = env
    return conf_data
