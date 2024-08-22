from abc import ABC, abstractmethod

class IstpTestRepository(ABC):

    @abstractmethod
    def generateText(self, userSendMessage):
        pass