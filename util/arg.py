from pathlib import Path
from argparse import ArgumentParser


def get_args() -> dict:
    parser = ArgumentParser(description="Project arguments")
    parser.add_argument("-c",
                        "--conf",
                        type=str,
                        default=None,
                        help="Project configuration file path")
    parser.add_argument("-e",
                        "--env",
                        type=str,
                        choices=["dev", "test", "prod"],
                        default="dev",
                        help="Project environment mode")
    args = parser.parse_args()
    if args.conf is None:
        if args.env == "dev":
            file_path = Path(f"./conf/default.yaml")
        else:
            file_path = Path(f"./conf/default.{args.env}.yaml")
    else:
        file_path = Path(args.conf)

    if not file_path.exists():
        raise FileNotFoundError(f"{file_path} not exists!")

    args.conf = str(file_path)
    return vars(args)
