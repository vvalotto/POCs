
from comando import Invocador


class GestorVinculo:

    def __init__(self, invocador):
        self._invocador = invocador

    def obtener_holter(self):
        self._invocador.ejecutar("leer_estado")
        self._invocador.ejecutar("leer_configuracion")

    def preparar_holter_para_monitoreo(self):
        self._invocador.ejecutar("poner_hora")
        self._invocador.ejecutar("poner_configuracion")

    def monitorear_holter(self):
        self._invocador.ejecutar("obtener_ecg_monitoreo")

    def parar_holter(self):
        self._invocador.ejecutar("parar_modo_holter")