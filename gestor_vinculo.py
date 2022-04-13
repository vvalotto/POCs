
from comando import Invocador


class GestorVinculo:

    def __init__(self, invocador):
        self._invocador = invocador

    def obtener_holter(self, holter):
        holter.estado = self._invocador.ejecutar("leer_estado")
        self._invocador.ejecutar("leer_configuracion")

    def preparar_holter_para_monitoreo(self):
        self._invocador.ejecutar("poner_hora")
        self._invocador.ejecutar("poner_configuracion")

    def monitorear_holter(self):
        self._invocador.ejecutar("obtener_ecg_monitoreo")

    def parar_holter(self):
        self._invocador.ejecutar("parar_modo_holter")

    def preparar_holter_para_adquisicion(self,):
        self._invocador.ejecutar("poner_hora")
        self._invocador.ejecutar("poner_adquisicion")

    def preparar_holter_para_descargar(self):
        self._invocador.ejecutar("poner_hora")
        self._invocador.ejecutar("poner_descarga")

    def descargar_EGC(self):
        self._invocador.ejecutar("Descargar")

    def descargar_Eventos(self):
        self._invocador.ejecutar("pedir_eventos")
