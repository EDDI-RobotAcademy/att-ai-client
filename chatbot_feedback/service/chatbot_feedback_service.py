from abc import ABC, abstractmethod


class ChatbotFeedbackService(ABC):
    @abstractmethod
    def giveChatbotFeedback(self, userSendMessage):
        pass