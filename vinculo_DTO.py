"""DTO MONITOREO"""
class MonitoreoDTO:

    def __init__(self) -> None:
        self.__channel_1 = []
        self.__channel_2 = []
        self.__channel_3 = []

    @property
    def channel_1(self):
        return self.__channel_1

    @channel_1
    def channel_1(self, valor):
        self.__channel_1 = valor

    @property
    def channel_2(self):
        return self.__channel_2

    @channel_2
    def channel_2(self, valor):
        self.__channel_2 = valor

    @property
    def channel_3(self):
        return self.__channel_3

    @channel_3
    def channel_3(self, valor):
        self.__channel_3 = valor
