import pytz

class Constants:

    def __init__(self):

        self.__USR = 0
        self.__PWD = ""
        self.__TIMEZONE = pytz.timezone("America/Bogota")


    @property
    def USR(self):
        return self.__USR

    @property
    def PWD(self):
        return self.__PWD

    @property
    def TIMEZONE(self):
        return self.__TIMEZONE
