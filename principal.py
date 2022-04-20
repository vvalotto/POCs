from gestor_vinculo import GestorVinculo
import configurador_vinculo
import time
from record_ECG import MonitorECG

monitor_ecg = MonitorECG()

invocador = configurador_vinculo.invocador
gestor = GestorVinculo(invocador)
gestor.obtener_status_holter()
time.sleep(3)
# gestor.parar_holter()
# time.sleep(3)
# gestor.poner_modo_monitoreo()
# gestor.monitorear_holter(monitor_ecg)
# gestor.parar_holter()
# gestor.obtener_configuracion_holter()

