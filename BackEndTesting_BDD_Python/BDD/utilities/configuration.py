import configparser
def getConfig():
    config=configparser.ConfigParser()
    config.read('/Users/revathyanilasreekumar/Python_API_UI_Testing/BackEndTesting_BDD_Python/BDD/utilities/properties.ini')
    return config

def getPassword():
    return "12346677"