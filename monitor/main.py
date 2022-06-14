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


class DeviceConnector(QObject):

    def __init__(self, event) -> None:
        super().__init__()
        self._signal_to_connect = event
    
    @Slot(bool)
    def holter_connect(self, flag):
        if flag:
            self._signal_to_connect.set()          


class show_monitor():
    def __init__(self, plotter: Plotter, connector: DeviceConnector) -> None:
        self.plot = plotter
        self._connector = connector

    def main(self):
        app = QApplication(sys.argv)
        engine = QQmlApplicationEngine()
        engine.load(os.fspath(Path(__file__).resolve().parent / "main_monitor.qml"))

        # plot = Plotter()
        engine.rootObjects()[0].setProperty('connector', self._connector)
        engine.rootObjects()[0].setProperty('plotter', self.plot)

        if not engine.rootObjects():
            sys.exit(-1)
        sys.exit(app.exec())

# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     engine = QQmlApplicationEngine()
#     engine.load(os.fspath(Path(__file__).resolve().parent / "main_monitor.qml"))

#     plot = Plotter()
#     engine.rootObjects()[0].setProperty('plotter', plot)

#     if not engine.rootObjects():
#         sys.exit(-1)
#     sys.exit(app.exec())
