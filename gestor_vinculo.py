import time
from comando import Invocador


class GestorVinculo:

    def __init__(self, invocador):
        self._invocador = invocador

    def obtener_status_holter(self):
        a = self._invocador.ejecutar("leer_estado")

    def obtener_configuracion_holter(self):
        self._invocador.ejecutar("leer_configuracion")

    def preparar_holter_para_monitoreo(self):
        self._invocador.ejecutar("poner_hora")
        self._invocador.ejecutar("poner_configuracion")

    def poner_modo_monitoreo(self):
        confirmacion = self._invocador.ejecutar("poner_modo_monitoreo")
        print ('Poner modo monitoreo: ', confirmacion)

    def monitorear_holter(self, monitor_ecg):
        timeout = time.time()+1
        while (time.time() < timeout and monitor_ecg.state):
            channels = self._invocador.ejecutar("obtener_ecg_monitoreo")
            monitor_ecg.channel_1 = channels[0]
            monitor_ecg.channel_2 = channels[1]
            monitor_ecg.channel_3 = channels[2]

    def parar_holter(self): # modo IDLE
        self._invocador.ejecutar("parar_modo_holter")

    def desenlazar_holter(self):
        self._invocador.ejecutar("desenlazar_holter")