import logging

def setup_logger():
    log = logging.getLogger()
    log.setLevel(logging.INFO)

    handler = logging.StreamHandler()
    handler.setLevel(logging.INFO)
    formatter = logging.Formatter('%(levelname)s: %(message)s')
    handler.setFormatter(formatter)
    log.addHandler(handler)
    return log