from abc import ABC, abstractmethod


class IstpTestService(ABC):
    @abstractmethod
    def chatWithIstp(self, userSendMessage):
        pass