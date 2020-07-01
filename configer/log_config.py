import logging


def get_logger(name):
    log = logging.getLogger(name)
    log.setLevel(logging.ERROR)
    return log
