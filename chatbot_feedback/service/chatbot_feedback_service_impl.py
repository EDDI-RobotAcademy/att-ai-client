from chatbot_feedback.service.chatbot_feedback_service import ChatbotFeedbackService
from chatbot_feedback.repository.chatbot_feedback_repository_impl import ChatbotFeedbackRepositoryImpl


class ChatbotFeedbackServiceImpl(ChatbotFeedbackService):

    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            cls.__instance.__chatbotFeedbackRepository = ChatbotFeedbackRepositoryImpl().getInstance()

        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()

        return cls.__instance

    async def giveChatbotFeedback(self, feedback):
        return await self.__chatbotFeedbackRepository.giveChatbotFeedback(feedback)