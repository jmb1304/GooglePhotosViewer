import configparser


class Config:
    config = ""

    def __init__(self):
        self.config = configparser.ConfigParser()
        self.config.read('config.ini')

    def getConfig(self):
        return self.config
