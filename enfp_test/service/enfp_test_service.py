from abc import ABC, abstractmethod


class EnfpTestService(ABC):
    @abstractmethod
    def chatWithEnfp(self, userSendMessage):
        pass