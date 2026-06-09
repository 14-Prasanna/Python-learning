import logging

def log_generator():

    logging.basicConfig(
        filename="logfile.log",
        level=logging.DEBUG,
        format="%(asctime)s - %(levelname)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        force=True
    )

    logger = logging.getLogger()
    return logger