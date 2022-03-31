from abc import ABCMeta, abstractmethod


class ComandoHolter(metaclass=ABCMeta):
    LARGO_PAQUETE = 12

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
    def armar_comando(self):
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


class ComandoLecturaStatusEnvio(ComandoHolter):

    def armar_comando(self):
        self._header = b'\xa5'
        self._type = b'\x61'
        self._payload = b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
        self._armar_paquete()


class ComandoLecturaConfiguracionEnvio(ComandoHolter):

    def armar_comando(self):
        self._header = b'\a5'
        self._type = b'\62'
        self._payload = b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
        self._armar_paquete()


if __name__ == '__main__':
    print(ComandoLecturaStatusEnvio().paquete)

    mi_comando = ComandoLecturaConfiguracionEnvio()
    mi_comando.armar_comando()
    print(mi_comando.paquete)