from abc import ABC, abstractmethod

class ChatbotFeedbackRepository(ABC):

    @abstractmethod
    def giveChatbotFeedback(self, feedback):
        pass