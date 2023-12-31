import configparser

config = configparser.RawConfigParser()
config.read("../config.ini")

class ReadConfig():
    @staticmethod
    def getSiteURL():
        url = config.get('common info', 'baseURL')
        return url

    @staticmethod
    def getUsername():
        username = config.get('common info', 'username')
        return username

    @staticmethod
    def getPassword():
        password = config.get('common info', 'baseURL')
        return password

