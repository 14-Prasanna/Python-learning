from configparser import ConfigParser, NoSectionError, NoOptionError
import os

def get_config(category, key):
    # Get the correct path to config.ini (inside resources folder)
    current_dir = os.path.dirname(os.path.abspath(__file__))
    config_path = os.path.join(current_dir, "config.ini")
    
    config = ConfigParser()
    read_files = config.read(config_path)
    
    if not read_files:
        raise Exception(f"config.ini file not found at: {config_path}")
    
    try:
        return config.get(category, key).strip()
    except NoSectionError:
        available = config.sections()
        raise Exception(f"Section '{category}' not found in config.ini. Available sections: {available}")
    except NoOptionError:
        raise Exception(f"Key '{key}' not found in section '{category}'")
    except Exception as e:
        raise Exception(f"Config error: {e}")