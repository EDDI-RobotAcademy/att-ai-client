from abc import ABC, abstractmethod

class EnfpTestRepository(ABC):

    @abstractmethod
    def generateText(self, userSendMessage):
        pass