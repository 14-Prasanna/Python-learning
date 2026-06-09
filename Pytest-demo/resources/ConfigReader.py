from configparser import ConfigParser
import os

def get_value(section, key):

    config = ConfigParser()

    base_dir = os.path.dirname(__file__)  
    file_path = os.path.join(base_dir, "config.ini")

    config.read(file_path)

    if not config.sections():
        raise Exception(f"Config not loaded from: {file_path}")

    return config.get(section, key)