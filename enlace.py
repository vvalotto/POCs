from abc import abstractmethod, ABCMeta, ABC


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


class EnlaceUSB(AbsEnlace, ABC):

    def __init__(self):
        pass

    def conectar(self):
        """ Conectar mediante USB """
        print('Conectando por USB')

    def desconectar(self):
        """ Desconectar mediante USB """
        print('Desconectando por USB')

    def enviar(self, datos):
        print('Enviando: ' + str(datos))

    def recibir(self):
        return 'datos'


class EnlaceDongle(AbsEnlace):

    def __init__(self):
        pass