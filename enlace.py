from abc import abstractmethod, ABCMeta


class AbsEnlace(metaclass=ABCMeta):

    @abstractmethod
    def conectar(self):
        pass

    @abstractmethod
    def desconectar(self):
        pass

    @abstractmethod
    def enviar(self, datos):
        pass

    @abstractmethod
    def recibir(self):
        pass


class EnlaceUSB(AbsEnlace):

    def __init__(self):
        pass


class EnlaceDongle(AbsEnlace):

    def __init__(self):
        pass