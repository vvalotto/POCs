from abc import ABCMeta, abstractmethod


class ComandoHolter(metaclass=ABCMeta):
    LARGO_PAQUETE = 13

    @property
    def paquete(self):
        return self._datos

    def __init__(self):
        self._header = None
        self._type = None
        self._payload = None
        self._checksum = None
        self._datos = None

    @abstractmethod
    def armar_comando(self, payload=None):
        pass

    def _obtener_checksum(self, datos):
        checksum = 0
        for i in range(self.LARGO_PAQUETE - 1):
            checksum ^= datos[i]
        return checksum

    def _armar_paquete(self):
        self._datos = self._header + \
                self._type + \
                self._payload

        self._checksum = self._obtener_checksum(self._datos).to_bytes(1, 'big')
        self._datos += self._checksum


class ComandoHolterStatus(ComandoHolter):

    def armar_comando(self, payload=None):
        self._header = b'\xa5'
        self._type = b'\x61'
        self._payload = b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
        self._armar_paquete()


class ComandoHolterConfiguracion(ComandoHolter):

    def armar_comando(self, payload=None):
        self._header = b'\a5'
        self._type = b'\62'
        self._payload = b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
        self._armar_paquete()


class ComandoHolterMemoria(ComandoHolter):
    pass


class ComandoHolterProduccion(ComandoHolter):
    pass


class ComandoHolterEvento(ComandoHolter):
    pass


class ComandoHolterEGC(ComandoHolter):
    pass


class ComandoHolterFechaHora(ComandoHolter):

    def armar_comando(self, payload=None):
        self._header = b'\xa5'
        self._type = b'\x80'
        self._payload = payload
        self._armar_paquete()


class ComandoHolterModo(ComandoHolter):

    def armar_comando(self, payload=None):
        self._header = b'\xa5'
        self._type = b'\x81'
        self._payload = payload
        self._armar_paquete()


class ComandoHolterPreparacion(ComandoHolter):
    pass


class ComandoHolterBorradoMemoria(ComandoHolter):
    pass


class ComandoHolterApagadoSistema(ComandoHolter):
    pass


class RespuestaHolter(metaclass=ABCMeta):
    LARGO_PAQUETE = 13

    @property
    def paquete(self):
        return self._datos

    def __init__(self):
        self._header = None
        self._type = None
        self._payload = None
        self._checksum = None
        self._datos = None

    @abstractmethod
    def desarmar_respuesta(self, datos):
        pass

    def _obtener_checksum(self, datos):
        checksum = 0
        for i in range(self.LARGO_PAQUETE - 1):
            checksum ^= datos[i]
        return checksum

    def _desarmar_paquete(self, datos):
        self._header = None
        self._type = None
        self._payload = None
        self._checksum = None
        self._datos = datos

        self._checksum = self._obtener_checksum(self._datos).to_bytes(1, 'big')
        self._datos += self._checksum


class RespuestaHolterStatus(RespuestaHolter):

    def desarmar_respuesta(self, datos):
        self._desarmar_paquete(datos)

    def guardar_estado(self):
        estado = None

        return estado


class RespuestaHolterConfiguracion(RespuestaHolter):

    def desarmar_respuesta(self, datos):
        pass


class RespuestaHolterMemoria(RespuestaHolter):
    pass


class RespuestaHolterProduccion(RespuestaHolter):
    pass


class RespuestaHolterEGCMonitoreo(RespuestaHolter):
    pass


class RespuestaHolterEvento(RespuestaHolter):
    pass


class RespuestaHolterEGC(RespuestaHolter):
    pass


class RespuestaHolterEscritiuraOK(RespuestaHolter):
    pass


class RespuestaHolterBorrado(RespuestaHolter):
    pass


class RespuestaHolterApagado(RespuestaHolter):
    pass



