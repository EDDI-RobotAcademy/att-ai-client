from istp_test.repository.istp_test_respository_impl import IstpTestRepositoryImpl
from istp_test.service.istp_test_service import IstpTestService

class IstpTestServiceImpl(IstpTestService):

    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            cls.__instance.__IstpTestRepository = IstpTestRepositoryImpl.getInstance()

        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()

        return cls.__instance

    def chatWithIstp(self, userSendMessage):
        return self.__IstpTestRepository.generateText(userSendMessage)