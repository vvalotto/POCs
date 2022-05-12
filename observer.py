from __future__ import annotations
from abc import ABC, abstractmethod
from random import randrange
from typing import List



class AbsSubjet(ABC):

    """ Tema """

    @abstractmethod
    def attach(self, observer : AbsObserver)-> None:
        """ Incorporar Observador """
        pass

    @abstractmethod
    def detach(self,observer : AbsObserver)-> None:
        """ Eliminar Observador """
        pass

    @abstractmethod
    def notify(self) -> None:
        """ Notificador de cambio """
        pass


class AbsObserver(ABC):
    """ Observador """

    @abstractmethod
    def update(self, subjet : AbsSubjet)-> None:
        pass


class MonitoreoSubjet(AbsSubjet):

    _state: int = None 

    _observers: List[AbsObserver] = []

    def attach(self, observer : AbsObserver):
        print("Subject: Attached an observer.")
        self._observers.append(observer)      
    
    def detach(self, observer : AbsObserver):
        self._observers.remove(observer)

    def notify(self):
        print("Subject: Notifying observers...")
        for observer in self._observers:
            observer.update(self)

    def some_business_logic(self) -> None:
        """
        Usually, the subscription logic is only a fraction of what a Subject can
        really do. Subjects commonly hold some important business logic, that
        triggers a notification method whenever something important is about to
        happen (or after it).
        """

        # print("\nSubject: I'm doing something important.")
        # self._state = randrange(0, 10)

        # print(f"Subject: My state has just changed to: {self._state}")
        self._state = 1
        self.notify()


class ObserverMonitorDOT(AbsObserver):
    def __init__(self,objet_monitor) -> None:
        self._ecg_monitor = objet_monitor


    def update(self, subject: MonitoreoSubjet) -> None:
        print("ConcreteObserverA: Reacted to the event")
        print ('Vincular con el presentador')
        print ('OBSERVADOR')
        print (self._ecg_monitor._channel_1)
        print (self._ecg_monitor._channel_2)
        print (self._ecg_monitor._channel_3)
        
        # if subject._state < 3:
        #     print("ConcreteObserverA: Reacted to the event")



# if __name__ == "__main__":
#     # The client code.

#     subject = MonitoreoSubjet()

#     observer_a = ObserverMonitorDOT()
#     subject.attach(observer_a)

#     subject.some_business_logic()
#     subject.some_business_logic()

#     subject.some_business_logic()


#     subject.detach(observer_a)

#     subject.some_business_logic()