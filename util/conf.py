from ruamel.yaml import YAML

from util.log import get_logger
from util.arg import get_args

yaml = YAML()
logger = get_logger(__name__)
args = get_args()


def read_yaml(yaml_path: str) -> dict:
    with open(yaml_path, "r") as f_yaml:
        datas = yaml.load(f_yaml)
    return datas


def get_conf() -> dict:
    conf_data = read_yaml(args["conf"])
    conf_data["env"] = args["env"]
    return conf_data
