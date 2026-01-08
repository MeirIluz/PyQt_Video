from abc import ABC, abstractmethod


class IExampleManager(ABC):

    @abstractmethod
    def start(self):
        pass
