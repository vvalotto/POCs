from zmq import EVENT_CLOSE_FAILED
from gestor_vinculo import GestorVinculo
import configurador_vinculo
import time
from record_ECG import MonitorECG


""" Implementación Patrón observer y Threding para caso de Monitoreo """
from observer import *
from threading import Thread
from threading import Lock
from threading import Event
from monitor import main
from vinculo_DTO import MonitoreoDTO

""" Objeto graficador"""
event_con= Event()
ploter = main.Plotter()
connector = main.DeviceConnector(event_con)

show = main.show_monitor(ploter, connector)
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

def iniciar_monitoreo():
	global ploter
	global gestor
	global monitor_ecg
	global monitor_subjet
	# time.sleep(3)
	# gestor.parar_holter()
	# gestor.desenlazar_holter()
	time.sleep(3)

	""" Threading: evento y bloqueo """
	event_monitor = Event()
	lock_monitor = Lock()

	def monitorear(monitor_ecg, lock_monitor,event_monitor):
		gestor.poner_modo_monitoreo()
		gestor.monitorear_holter(monitor_ecg, lock_monitor,event_monitor)
		gestor.parar_holter()
        

	def print_monitor(monitor_subjet,lock_monitor, event_monitor):
		while (True):
			event_monitor.wait()
			# print (event_monitor.is_set())
			with lock_monitor:
				monitor_subjet.some_business_logic()
				event_monitor.clear()
				# print (event_monitor.is_set())

	t_1 = Thread(target=monitorear, args=(monitor_ecg, lock_monitor,event_monitor))

	t_2 = Thread(target=print_monitor, args=(monitor_subjet,lock_monitor, event_monitor))
	t_1.start()
	t_2.start()

def connect_holter(event_con):
	global gestor
	event_con.wait()
	gestor.obtener_status_holter()

def show_graph():
	global show
	show.main()



	
t_show = Thread(target = show_graph)
# t_connect = Thread(target = show.main, args = (event_con))
t_show.start()
# t_connect.start()

# iniciar_monitoreo()
# show.main()