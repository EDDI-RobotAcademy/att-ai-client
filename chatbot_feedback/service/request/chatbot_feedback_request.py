from template.request_generator.base_request import BaseRequest
from user_defined_protocol.protocol import UserDefinedProtocolNumber


class ChatbotFeedbackRequest(BaseRequest):
    def __init__(self, **kwargs):
		# 등록한 프로토콜 번호
        self.__protocolNumber = UserDefinedProtocolNumber.ATT_TEAM_CHATBOT_FEEDBACK.value
        self.parameterList = kwargs.get('data', [])

    def getProtocolNumber(self):
        return self.__protocolNumber

    def getParameterList(self):
        return tuple(self.parameterList)

    def toDictionary(self):
        return {
            "protocolNumber": self.__protocolNumber,
            "parameterList": self.parameterList
        }

    def __str__(self):
		# request 이름
        return f"ChatbotRequest(protocolNumber={self.__protocolNumber}, parameterList={self.parameterList})"