import configparser

config = configparser.ConfigParser()
config.read('config.ini')

def get_config_value(section, key):
    return config.get(section, key)
