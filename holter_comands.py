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


class ComandEmpty(ComandoHolter):
    
    def armar_comando(self, payload=None):
        pass


class ComandoLecturaStatusEnvio(ComandoHolter):

    def armar_comando(self, payload=None):
        self._header = b'\xa5'
        self._type = b'\x60'
        self._payload = b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
        self._armar_paquete()
 

class ComandoLecturaConfiguracionEnvio(ComandoHolter):

    def armar_comando(self, payload=None):
        self._header = b'\xa5'
        self._type = b'\x61'
        self._payload = b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
        self._armar_paquete()


class ComandoEscrituraModoIdleEnvio(ComandoHolter):
    
    def armar_comando(self, payload=None):
        self._header = b'\xa5'
        self._type = b'\x81'
        self._payload = b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
        self._armar_paquete()


class ComandoEscrituraModoMonitoreoEnvio(ComandoHolter):
    
    def armar_comando(self, payload=None):
        self._header = b'\xa5'
        self._type = b'\x81'
        self._payload = b'\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00'
        self._armar_paquete()


class RespuestaHolter(metaclass=ABCMeta):
    
    PACKAGE_LENGTH = 13
    ANSWER_OK = b'\xa5\x0A\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xaf'

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
        for i in range(self.PACKAGE_LENGTH - 1):
            checksum ^= datos[i]
        return checksum

    def _desarmar_paquete(self, datos):

        if not (datos == None):
            checksum = self._obtener_checksum(datos).to_bytes(1, 'big')

            if (datos[-1].to_bytes(1, 'big') == checksum):
                self._header = datos[0]
                self._type = datos[1]
                self._payload = datos[2:12]
                self._checksum = checksum
                self._datos = datos
                print ("respuesta ok:", datos)

            else: print('Paquete erróneo')
        else: print ('Datos no recibidos')


class RespuestaHolterStatus(RespuestaHolter):

    def desarmar_respuesta(self, datos):
        self._desarmar_paquete(datos)
        return self._payload

    def guardar_estado(self):
        print (self._datos)
        return self._datos


class RespuestaHolterConfiguracion(RespuestaHolter):

    def desarmar_respuesta(self, datos):
        pass


class RespuestaHolterMemoria(RespuestaHolter):
    pass


class RespuestaHolterProduccion(RespuestaHolter):
    pass


class RespuestaHolterEGCMonitoreo(RespuestaHolter):

    def desarmar_respuesta(self, datos):
        channel_1 = []
        channel_2 = []
        channel_3 = []
        print ((len(datos)/self.PACKAGE_LENGTH))
        for i in range (0, int (len(datos)/self.PACKAGE_LENGTH)):
            self._desarmar_paquete(datos[i*self.PACKAGE_LENGTH:(i+1)*self.PACKAGE_LENGTH])
            channel_1.append(self._payload[:3])
            channel_2.append(self._payload[3:6])
            channel_3.append(self._payload[6:9])
        channels = [channel_1, channel_2, channel_3]
        return channels


class RespuestaHolterEvento(RespuestaHolter):
    pass


class RespuestaHolterEGC(RespuestaHolter):
    pass


class RespuestaHolterEscritiuraOK(RespuestaHolter):
    def desarmar_respuesta(self, datos):
        self._desarmar_paquete(datos)
        return self._datos == self.ANSWER_OK


class RespuestaHolterBorrado(RespuestaHolter):
    pass


class RespuestaHolterApagado(RespuestaHolter):
    def desarmar_respuesta(self, datos):
        pass
