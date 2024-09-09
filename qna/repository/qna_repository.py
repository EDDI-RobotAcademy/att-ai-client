from abc import ABC, abstractmethod

class QnaRepository(ABC):

    @abstractmethod
    def dateQuestion(self, userSendMessage):
        pass