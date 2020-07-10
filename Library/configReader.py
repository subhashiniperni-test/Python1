import configparser


def readConfigData(section, key):
    config = configparser.ConfigParser()
    config.read("./ConfigurationFiles/Config.cfg")
    return config.get(section, key)

def fetchElementLocators(section, key):
    config = configparser.ConfigParser()
    config.read("./ConfigurationFiles/Element.cfg")
    return config.get(section, key)

def fetchElementLocators1(section, key):
    config = configparser.ConfigParser()
    config.read("./ConfigurationFiles/Element.cfg")
    return config.get(section, key)

