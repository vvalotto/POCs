from paquete_datos import *
from abc import ABCMeta, abstractmethod
from paquete_datos import *


class AbsComando(metaclass=ABCMeta):

    def __init__(self, destinatario, comando):
        self._destinatario = destinatario
        self._comando = comando

    @staticmethod
    @abstractmethod
    def ejecutar(self):
        pass


class LectorStatusHolter(AbsComando):

    def ejecutar(self):
        # lee estatus del holter
        self._comando.armar_comando()
        self._destinatario.enviar(self._comando.paquete)
        print(self._comando.paquete)
        self._destinatario.recibir()


class LectorConfiguracionHolter(AbsComando):

    def ejecutar(self):
        # lee Configuracion del holter
        self._comando.armar_comando()
        self._destinatario.enviar(self._comando.paquete)
        print(self._comando.paquete)
        self._destinatario.recibir()


class IdentificadorHolter(AbsComando):
    pass


class ObtenerMemoria(AbsComando):
    pass


class ObtenerEventos(AbsComando):
    pass


class ObtenerEGC(AbsComando):
    pass


class PonerHora(AbsComando):


    pass


class PonerModo(AbsComando):
    pass


class PonerConfiguracion(AbsComando):
    pass


class BorrarMemoria(AbsComando):
    pass


class PararHolter(AbsComando):
    pass


class Destinatario:

    def __init__(self, tipo_vinculo):
        self._tipo_vinculo = tipo_vinculo

    def enviar(self, paquete):
        print(self._tipo_vinculo)
        print('Enviar paquete')

    def recibir(self):
        print(self._tipo_vinculo)
        print('Recibir paquete')


class Invocador:

    def __init__(self):
        self._comandos = {}

    def registrar_comando(self, nombre, comando):
        self._comandos[nombre] = comando

    def ejecutar(self, nombre):
        if nombre in self._comandos.keys():
            self._comandos[nombre].ejecutar()
        else:
            raise 'Comando no reconocido'


