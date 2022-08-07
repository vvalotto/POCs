# This Python file uses the following encoding: utf-8
import os
from pathlib import Path
import sys
import time
#from PySide6.QtGui import QGuiApplication hola
from PySide6.QtQml import QQmlApplicationEngine
from PySide6.QtCore import QObject, QTimer, Slot, Signal, QPointF#, QTime
from PySide6.QtWidgets import QApplication
from PySide6.QtCharts import QAbstractSeries #, QDateTimeAxis

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
from vinculo_DTO import MonitoreoDTO



class Plotter(QObject):

    send = Signal(bool)
    _view_buffer_data = []
    _buffer_data = []


    def __init__(self):
        super().__init__()

        self._channel_1 = []
        self._ADCmax = 0xF30000
        self._Vref = 2.4
        self._new_data = []
        self.__generate_buffer_data()

    def data_update(self):
        self._new_data = []
        for i in range (0, len(self._channel_1)):
            dato_int = self._channel_1[i][0]*65536+self._channel_1[i][1]*256+self._channel_1[i][2]
            dato = ((dato_int/self._ADCmax-0.5)*2*self._Vref/3.5)*1000
            self._new_data.append(QPointF(i,dato))

    def __generate_buffer_data(self, time_view = 1600):
        self._buffer_data = [QPointF(i,0) for i in range(0,time_view)]

    def refresh_buffer(self):
        self._buffer_data = self._buffer_data[len(self._new_data):]
        self._buffer_data.extend(self._new_data)

        for point in range(len(self._buffer_data)):
            self._buffer_data[point].setX(point)

    def update_buffer_data(self):

        self._view_buffer_data = self._buffer_data
        self.send.emit(True)

    @Slot(QAbstractSeries)
    def get_series(self, series):
        series.replace(self._view_buffer_data)

    def change_time_axis(self):
        pass


class DeviceConnectorMode(QObject):
    global gestor
    global monitor_ecg

    def __init__(self, event) -> None:
        super().__init__()
        self._signal_to_connect = event
        self._flag = False

    @Slot(bool)
    def holter_connect(self, flag):
        self._flag = flag
        if flag:
            gestor.obtener_status_holter()
        else:
            gestor.parar_holter()

    @property
    def flag(self):
        return self._flag

    @Slot(bool)
    def monitor_mode(self, on_off):
        monitor_ecg.state = on_off
        if on_off:
            iniciar_monitoreo()   
        else:
            gestor.parar_holter()


""" Objeto graficador"""
event_con= Event()
ploter_1 = Plotter()
ploter_2 = Plotter()
ploter_3 = Plotter()
connector = DeviceConnectorMode(event_con)

""" Entidad ECG Monitoreo """ #--> debería ser el DTO
monitor_ecg = MonitorECG()

""" Subjet and Observer """

monitor_subjet = MonitoreoSubjet()
observer_a = ObserverMonitorDTO(monitor_ecg, ploter_1, ploter_2, ploter_3)

monitor_subjet.attach(observer_a)

""" Invocador """
link_usb = 'USB_CONNECTION'
# link_usb = 'DONGLE_CONNECTION'
MonitoreoDTO.link_type = link_usb

invocador = configurador_vinculo.init_invocator(link_usb)


""" Gestor de vínculo """

gestor = GestorVinculo(invocador)


def monitorear(monitor_ecg, lock_monitor,event_monitor):

    gestor.poner_modo_monitoreo()
    gestor.monitorear_holter(monitor_ecg, lock_monitor,event_monitor)
    # t_2.join()
    # print (t_2.is_alive())

def print_monitor(monitor_subjet,lock_monitor, event_monitor):
    while (monitor_ecg.state):
        event_monitor.wait()
        with lock_monitor:
            monitor_subjet.some_business_logic()
            event_monitor.clear()

def iniciar_monitoreo():
    
    """ Threading: evento y bloqueo """
    event_monitor = Event()
    lock_monitor = Lock()   
    t_1 = Thread(target=monitorear, args=(monitor_ecg, lock_monitor,event_monitor))
    t_2 = Thread(target=print_monitor, args=(monitor_subjet,lock_monitor, event_monitor))

    t_1.start()
    t_2.start()
    # global gestor
    # global monitor_ecg
    # global monitor_subjet
	# # time.sleep(3)
	# # gestor.parar_holter()
	# # gestor.desenlazar_holter()
    # # time.sleep(3)
    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    engine = QQmlApplicationEngine()
    engine.load(os.fspath(Path(__file__).resolve().parent / "monitor/main_monitor.qml"))

    engine.rootObjects()[0].setProperty('plotter', ploter_1)
    engine.rootObjects()[0].setProperty('plotter2', ploter_2)
    engine.rootObjects()[0].setProperty('plotter3', ploter_3)
    engine.rootObjects()[0].setProperty('connector', connector)
    
    if not engine.rootObjects():
        sys.exit(-1)
    sys.exit(app.exec())