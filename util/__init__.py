import colorlog
import sys


def get_logger(name: str) -> colorlog.log:
    handler = colorlog.StreamHandler(stream=sys.stdout)
    handler.setFormatter(colorlog.ColoredFormatter(
        '%(log_color)s[%(levelname)s][%(name)s]:%(message)s'))

    logger = colorlog.getLogger(name)
    logger.addHandler(handler)
    logger.setLevel(colorlog.DEBUG)

    return logger


