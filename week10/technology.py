from abc import ABC, abstractmethod


class Technology(ABC):

    @abstractmethod
    def active(self):
        pass

    def deactivate(self):
        pass
