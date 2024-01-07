import os
import pathlib
import logging
from logging.handlers import TimedRotatingFileHandler

import colorlog


env = os.getenv("ENV", "dev")
default_level_dict = {
    "dev": "debug",
    "test": "debug",
    "prod": "info"
}
default_level = default_level_dict.get(env, "info")

log_colors = {
    "DEBUG": "cyan",
    "INFO": "green",
    "WARNING": "yellow",
    "ERROR": "red",
    "CRITICAL": "purple"
}


def get_logger(name: str = "project", level: str = default_level) -> logging.Logger:
    # set logger
    logger = logging.getLogger(name)
    level_dict = {
        "debug": logging.DEBUG,
        "info": logging.INFO,
        "warning": logging.WARNING,
        "error": logging.ERROR,
        "critical": logging.CRITICAL
    }
    logger.setLevel(level_dict[level])

    if not logger.handlers:
        # time rotating file handler
        log_path = log_path_util(name)
        rotate_fh = TimedRotatingFileHandler(filename=log_path, when="midnight", interval=1, backupCount=365)
        rotate_fh.setLevel(logging.INFO)
        rotate_fh_fmt = logging.Formatter("%(asctime)-15s [%(filename)s] %(levelname)s %(lineno)d: %(message)s")
        rotate_fh.setFormatter(rotate_fh_fmt)
        logger.addHandler(rotate_fh)

        # stream handler
        console = logging.StreamHandler()
        console.setLevel(logging.DEBUG)
        console_fmt_str = "%(asctime)-15s [%(filename)s] %(log_color)s%(levelname)s%(reset)s %(lineno)d: %(message)s"
        console_fmt = colorlog.ColoredFormatter(console_fmt_str, log_colors=log_colors)
        console.setFormatter(console_fmt)
        logger.addHandler(console)
    return logger


def log_path_util(name: str) -> str:
    log_path = pathlib.Path(f"./log/")
    log_path.mkdir(parents=True, exist_ok=True)
    return str(log_path / f"{name}.log")
