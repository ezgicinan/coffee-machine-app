#coffee.py
from abc import ABC, abstractmethod

class Coffee(ABC):
    @abstractmethod
    def prepare(self):
        pass
    def checkResource(self, currentStock) -> bool:
        pass