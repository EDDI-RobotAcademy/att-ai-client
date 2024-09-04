from abc import ABC, abstractmethod


class ChatbotFeedbackService(ABC):
    @abstractmethod
    def giveChatbotFeedback(self, userSendMessage):
        pass

    @abstractmethod
    def finetuneWithFeedback(self):
        pass