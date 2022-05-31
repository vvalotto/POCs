# from multiprocessing import Event
# from multiprocessing import connection
from gestor_vinculo import GestorVinculo
import configurador_vinculo
import time
from record_ECG import MonitorECG

# monitor_ecg = MonitorECG()

# invocador = configurador_vinculo.invocador
# gestor = GestorVinculo(invocador)
# gestor.obtener_status_holter()
# time.sleep(3)
# gestor.parar_holter()
# time.sleep(3)
# gestor.poner_modo_monitoreo()
# gestor.monitorear_holter(monitor_ecg, monitor_subjet)
# print ('MONITOR ECG', monitor_ecg._channel_1)
# # # time.sleep(2)
# gestor.parar_holter()
# # time.sleep(2)
# gestor.obtener_configuracion_holter()

""" Implementación Patrón observer y Threding para caso de Monitoreo """
from observer import *
from threading import Thread
from threading import Lock
from threading import Event
from plot import main
from vinculo_DTO import MonitoreoDTO

""" Objeto graficador"""
ploter = main.Plotter()
show = main.show_monitor(ploter)

""" Entidad ECG Monitoreo """ #--> debería ser el DTO
monitor_ecg = MonitorECG()

""" Subjet and Observer """

monitor_subjet = MonitoreoSubjet()
observer_a = ObserverMonitorDTO(monitor_ecg, ploter)

monitor_subjet.attach(observer_a)

""" Invocador """
link_usb = 'USB_CONNECTION'

MonitoreoDTO.link_type = link_usb

invocador = configurador_vinculo.init_invocator(link_usb)


""" Gestor de vínculo """

gestor = GestorVinculo(invocador)
# gestor.obtener_status_holter()
# time.sleep(3)
gestor.parar_holter()
time.sleep(3)
""" Threading: evento y bloqueo """
event_monitor = Event()
lock_monitor = Lock()

def monitorear(monitor_ecg, lock_monitor,event_monitor):
        gestor.poner_modo_monitoreo()
        gestor.monitorear_holter(monitor_ecg, lock_monitor,event_monitor)
        gestor.parar_holter()
        print (t_2.is_alive())
        print (t_1.is_alive())
        

def print_monitor(monitor_subjet,lock_monitor, event_monitor):

        while (True):
                event_monitor.wait()
                print (event_monitor.is_set())
                with lock_monitor:
                        monitor_subjet.some_business_logic()
                        event_monitor.clear()
                        print (event_monitor.is_set())

t_1 = Thread(target=monitorear, args=(monitor_ecg, lock_monitor,event_monitor))

t_2 = Thread(target=print_monitor, args=(monitor_subjet,lock_monitor, event_monitor))
t_1.start()
t_2.start()


show.main()
t_1.join()
t_2.join()
print (t_2.is_alive())



