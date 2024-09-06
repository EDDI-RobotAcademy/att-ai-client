from abc import ABC, abstractmethod


class QnaService(ABC):
    @abstractmethod
    def dateQuestion(self, userSendMessage):
        pass