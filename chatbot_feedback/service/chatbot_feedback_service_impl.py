from chatbot_feedback.service.chatbot_feedback_service import ChatbotFeedbackService
from chatbot_feedback.repository.chatbot_feedback_repository_impl import ChatbotFeedbackRepositoryImpl

from fastapi import BackgroundTasks

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

    async def giveChatbotFeedback(self, *arg, **kwargs):

        userFeedback = {
            "finetuneId": arg[0],
            "prompt": arg[1],
            "response": arg[2],
            "feedback": arg[3],
            "betterResponse": arg[4]
        }

        return await self.__chatbotFeedbackRepository.giveChatbotFeedback(userFeedback)

    async def finetuneWithFeedback(self):
        return await self.__chatbotFeedbackRepository.finetuneWithFeedback(backgroundTasks=BackgroundTasks)