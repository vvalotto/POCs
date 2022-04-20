from socket import timeout
from holter_comands import *
from abc import ABCMeta, abstractmethod
from holter_comands import *
from enlace import *


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
        # Lee estatus del holter
        self._comando.armar_comando()
        self._destinatario.enviar(self._comando.paquete)
        print(self._comando.paquete)
        paquete_recibido = self._destinatario.recibir(1)
        print ('paquete', paquete_recibido)       
        self._respuesta.desarmar_respuesta(paquete_recibido)
        self._destinatario.desenlazar()
        return self._respuesta.guardar_estado()
        

class LectorConfiguracionHolter(AbsComando):

    def ejecutar(self):
        # lee Configuracion del holter
        self._comando.armar_comando()
        self._destinatario.enviar(self._comando.paquete)
        print(self._comando.paquete)
        configuracion = self._destinatario.recibir(1)
        return self._respuesta.desarmar_respuesta(configuracion)
        

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


class PonerModoMonitoreo(AbsComando):
    def ejecutar(self):
        # Activar modo monitoreo
        self._comando.armar_comando()
        self._destinatario.enviar(self._comando.paquete)
        print(self._comando.paquete)
        # Recepción de confirmación
        confirmacion = self._destinatario.recibir(1)
        return self._respuesta.desarmar_respuesta(confirmacion)


class GetECGMonitor(AbsComando):
    def ejecutar(self):
        datos_ecg_monitoreo = self._destinatario.recibir(4)
        return self._respuesta.desarmar_respuesta(datos_ecg_monitoreo)


class PonerConfiguracion(AbsComando):
    pass


class BorrarMemoria(AbsComando):
    pass


class HolterDisconnect(AbsComando):
    def ejecutar(self):
        self._destinatario.desenlazar()


class PararHolter(AbsComando):
    
    def ejecutar(self):
        # Activar modo idle y desenlazar holter
        self._comando.armar_comando()
        self._destinatario.enviar(self._comando.paquete)
        print('Para holter:', self._comando.paquete)
        configuracion = self._destinatario.recibir()
        self._destinatario.desenlazar()
        return self._respuesta.desarmar_respuesta(configuracion)
        

class Destinatario:
    
    def __init__(self, tipo_vinculo):
        self._tipo_vinculo = tipo_vinculo

    def enviar(self, paquete):
        print(type(self._tipo_vinculo))
        self._tipo_vinculo.conectar()
        self._tipo_vinculo.enviar(paquete)

    def recibir(self, amount_packages = 1):
        return self._tipo_vinculo.recibir(amount_packages)
    
    def desenlazar(self):
        self._tipo_vinculo.desconectar()


class Invocador:

    def __init__(self):
        self._comandos = {}

    def registrar_comando(self, nombre, comando):
        self._comandos[nombre] = comando

    def ejecutar(self, nombre):
        if nombre in self._comandos.keys():
            recibido = self._comandos[nombre].ejecutar()
            return recibido
        else:
            raise 'Comando no reconocido'