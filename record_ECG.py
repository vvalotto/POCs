from abc import ABCMeta, abstractmethod


class AbsECG(metaclass=ABCMeta):
    
    def __init__(self): #,datos):
        
        # self._datos = datos
        self._channel_1 = []
        self._channel_2 = []
        self._channel_3 = []

    abstractmethod    
    def separar_datos_canal(self):
        pass
    
    abstractmethod
    def almacenar_datos(self):
        pass


class RegistroECG(AbsECG):
    pass


class EventosECG(AbsECG):
    pass


class MonitorECG(AbsECG):
    state = True
    def separar_datos_canal(self):
        self._canal_1 = self._datos [2:5]
        self._canal_2 = self.datos [5:8]
        self._canal_3 = self.datos [8:11]