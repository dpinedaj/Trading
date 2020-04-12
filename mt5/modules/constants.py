import pytz

class Constants:

    def __init__(self):

        self.__USR = 27401862
        self.__PWD = 'dfkfksv1'
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
