from qna.repository.qna_repository_impl import QnaRepositoryImpl
from qna.service.qna_service import QnaService

class QnaServiceImpl(QnaService):

    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            cls.__instance.__QnaRepository = QnaRepositoryImpl.getInstance()

        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()

        return cls.__instance

    async def dateQuestion(self, userSendMessage):
        return await self.__QnaRepository.dateQuestion(userSendMessage)