from paquete_datos import *
from abc import ABCMeta, abstractmethod
from paquete_datos import *


class AbsComando(metaclass=ABCMeta):

    def __init__(self, destinatario, comando, respuesta):
        self._destinatario = destinatario
        self._comando = comando
        self._respuesta = respuesta

    @abstractmethod
    def ejecutar(self):
        pass


class LectorStatusHolter(AbsComando):

    def ejecutar(self):
        # lee estatus del holter
        self._comando.armar_comando()
        self._destinatario.enviar(self._comando.paquete)
        print(type(self._comando))
        estado = self._destinatario.recibir()
        return self._respuesta.desarmar_respuesta(estado)


class LectorConfiguracionHolter(AbsComando):

    def ejecutar(self):
        # lee Configuracion del holter
        self._comando.armar_comando()
        self._destinatario.enviar(self._comando.paquete)
        print(self._comando.paquete)
        configuracion = self._destinatario.recibir()
        # self._respuesta.desarmar_respuesta(configuracion)


class ObtenerMemoria(AbsComando):
    pass


class ObtenerEventos(AbsComando):
    pass


class ObtenerEGC(AbsComando):
    pass


class PonerHora(AbsComando):

    def ejecutar(self):
        # Poner la hora holter
        self._comando.armar_comando()
        self._destinatario.enviar(self._comando.paquete)
        print(self._comando.paquete)
        respuesta_OK = self._destinatario.recibir()
        self._respuesta.desarmar_respuesta(respuesta_OK)


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
        self._tipo_vinculo.enviar(paquete)

    def recibir(self):
        print(self._tipo_vinculo)
        paquete = self._tipo_vinculo.recibir()
        return paquete


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


