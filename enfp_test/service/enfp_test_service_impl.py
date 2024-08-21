from enfp_test.repository.enfp_test_repository_impl import EnfpTestRepositoryImpl
from enfp_test.service.enfp_test_service import EnfpTestService


class EnfpTestServiceImpl(EnfpTestService):

    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            cls.__instance.__enfpTestRepository = EnfpTestRepositoryImpl().getInstance()

        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()

        return cls.__instance

    async def chatWithEnfp(self, userSendMessage):
        return await self.__enfpTestRepository.generateText(userSendMessage)
