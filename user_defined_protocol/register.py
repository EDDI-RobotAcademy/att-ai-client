import os
import sys

from chatbot_feedback.service.chatbot_feedback_service_impl import ChatbotFeedbackServiceImpl
from chatbot_feedback.service.request.chatbot_feedback_request import ChatbotFeedbackRequest
from chatbot_feedback.service.request.finetune_with_feedback_request import FinetuneWithFeedbackRequest
from chatbot_feedback.service.response.chatbot_feedback_response import ChatbotFeedbackResponse
from chatbot_feedback.service.response.finetune_with_feedback_response import FinetuneWithFeedbackResponse
from enfp_test.service.enfp_test_service_impl import EnfpTestServiceImpl
from enfp_test.service.request.enfp_test_request import EnfpTestRequest
from enfp_test.service.response.enfp_test_response import EnfpTestResponse
from first_user_defined_function_domain.service.fudf_service_impl import FudfServiceImpl
from first_user_defined_function_domain.service.request.fudf_just_for_test_request import FudfJustForTestRequest
from first_user_defined_function_domain.service.response.fudf_just_for_test_response import FudfJustForTestResponse
from istp_test.service.istp_test_service_impl import IstpTestServiceImpl
from istp_test.service.request.istp_test_request import IstpTestRequest
from istp_test.service.response.istp_test_response import IstpTestResponse
from qna.service.qna_service_impl import QnaServiceImpl
from qna.service.request.qna_request import QnaRequest
from qna.service.response.qna_response import QnaResponse

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'template'))

from template.custom_protocol.service.custom_protocol_service_impl import CustomProtocolServiceImpl
from template.request_generator.request_class_map import RequestClassMap
from template.response_generator.response_class_map import ResponseClassMap

from user_defined_protocol.protocol import UserDefinedProtocolNumber


class UserDefinedProtocolRegister:

    @staticmethod
    def registerDefaultUserDefinedProtocol():
        customProtocolService = CustomProtocolServiceImpl.getInstance()
        firstUserDefinedFunctionService = FudfServiceImpl.getInstance()

        requestClassMapInstance = RequestClassMap.getInstance()
        requestClassMapInstance.addRequestClass(
            UserDefinedProtocolNumber.FIRST_USER_DEFINED_FUNCTION_FOR_TEST,
            FudfJustForTestRequest
        )

        responseClassMapInstance = ResponseClassMap.getInstance()
        responseClassMapInstance.addResponseClass(
            UserDefinedProtocolNumber.FIRST_USER_DEFINED_FUNCTION_FOR_TEST,
            FudfJustForTestResponse
        )

        customProtocolService.registerCustomProtocol(
            UserDefinedProtocolNumber.FIRST_USER_DEFINED_FUNCTION_FOR_TEST,
            firstUserDefinedFunctionService.justForTest
        )

	# 여러분의 사용자 정의형 프로토콜 등록 파트
    @staticmethod
    def registerIstpTestProtocol():
        customProtocolService = CustomProtocolServiceImpl.getInstance()
        IstpTestService = IstpTestServiceImpl.getInstance()

		# 여러분들이 구성한 것 (프로토콜과 request 등록)
        requestClassMapInstance = RequestClassMap.getInstance()
        requestClassMapInstance.addRequestClass(
            UserDefinedProtocolNumber.ATT_TEAM_ISTP_TEST,
            IstpTestRequest
        )

		# 여러분들이 구성한 것 (프로토콜과 response 등록)
        responseClassMapInstance = ResponseClassMap.getInstance()
        responseClassMapInstance.addResponseClass(
            UserDefinedProtocolNumber.ATT_TEAM_ISTP_TEST,
            IstpTestResponse
        )

		# 여러분들이 구성한 것 (프로토콜과 구동할 함수 등록)
        customProtocolService.registerCustomProtocol(
            UserDefinedProtocolNumber.ATT_TEAM_ISTP_TEST,
            IstpTestService.chatWithIstp
        )

    # ENFP Test
    @staticmethod
    def registerEnfpTestProtocol():
        customProtocolService = CustomProtocolServiceImpl.getInstance()
        EnfpTestService = EnfpTestServiceImpl.getInstance()

        # 여러분들이 구성한 것 (프로토콜과 request 등록)
        requestClassMapInstance = RequestClassMap.getInstance()
        requestClassMapInstance.addRequestClass(
            UserDefinedProtocolNumber.ATT_TEAM_ENFP_TEST,
            EnfpTestRequest
        )

        # 여러분들이 구성한 것 (프로토콜과 response 등록)
        responseClassMapInstance = ResponseClassMap.getInstance()
        responseClassMapInstance.addResponseClass(
            UserDefinedProtocolNumber.ATT_TEAM_ENFP_TEST,
            EnfpTestResponse
        )

        # 여러분들이 구성한 것 (프로토콜과 구동할 함수 등록)
        customProtocolService.registerCustomProtocol(
            UserDefinedProtocolNumber.ATT_TEAM_ENFP_TEST,
            EnfpTestService.chatWithEnfp
        )

    # Request Chatbot Feedback
    @staticmethod
    def registerChatbotFeedbackProtocol():
        customProtocolService = CustomProtocolServiceImpl.getInstance()
        ChatbotFeedbackService = ChatbotFeedbackServiceImpl.getInstance()

        # 여러분들이 구성한 것 (프로토콜과 request 등록)
        requestClassMapInstance = RequestClassMap.getInstance()
        requestClassMapInstance.addRequestClass(
            UserDefinedProtocolNumber.ATT_TEAM_CHATBOT_FEEDBACK,
            ChatbotFeedbackRequest
        )

        # 여러분들이 구성한 것 (프로토콜과 response 등록)
        responseClassMapInstance = ResponseClassMap.getInstance()
        responseClassMapInstance.addResponseClass(
            UserDefinedProtocolNumber.ATT_TEAM_CHATBOT_FEEDBACK,
            ChatbotFeedbackResponse
        )

        # 여러분들이 구성한 것 (프로토콜과 구동할 함수 등록)
        customProtocolService.registerCustomProtocol(
            UserDefinedProtocolNumber.ATT_TEAM_CHATBOT_FEEDBACK,
            ChatbotFeedbackService.giveChatbotFeedback
        )

    # FINETUNE_WITH_FEEDBACK 등록
    @staticmethod
    def registerFinetuneWithFeedbackProtocol():
        customProtocolService = CustomProtocolServiceImpl.getInstance()
        ChatbotFeedbackService = ChatbotFeedbackServiceImpl.getInstance()

        # 여러분들이 구성한 것 (프로토콜과 request 등록)
        requestClassMapInstance = RequestClassMap.getInstance()
        requestClassMapInstance.addRequestClass(
            UserDefinedProtocolNumber.ATT_TEAM_FINETUNE_WITH_FEEDBACK,
            FinetuneWithFeedbackRequest
        )

        # 여러분들이 구성한 것 (프로토콜과 response 등록)
        responseClassMapInstance = ResponseClassMap.getInstance()
        responseClassMapInstance.addResponseClass(
            UserDefinedProtocolNumber.ATT_TEAM_FINETUNE_WITH_FEEDBACK,
            FinetuneWithFeedbackResponse
        )

        # 여러분들이 구성한 것 (프로토콜과 구동할 함수 등록)
        customProtocolService.registerCustomProtocol(
            UserDefinedProtocolNumber.ATT_TEAM_FINETUNE_WITH_FEEDBACK,
            ChatbotFeedbackService.finetuneWithFeedback
        )

    # CHATBOT_DATE_QNA 등록
    @staticmethod
    def registerDateQnaProtocol():
        customProtocolService = CustomProtocolServiceImpl.getInstance()
        QnaService = QnaServiceImpl.getInstance()

        # 여러분들이 구성한 것 (프로토콜과 request 등록)
        requestClassMapInstance = RequestClassMap.getInstance()
        requestClassMapInstance.addRequestClass(
            UserDefinedProtocolNumber.ATT_TEAM_DATE_QNA,
            QnaRequest
        )

        # 여러분들이 구성한 것 (프로토콜과 response 등록)
        responseClassMapInstance = ResponseClassMap.getInstance()
        responseClassMapInstance.addResponseClass(
            UserDefinedProtocolNumber.ATT_TEAM_DATE_QNA,
            QnaResponse
        )

        # 여러분들이 구성한 것 (프로토콜과 구동할 함수 등록)
        customProtocolService.registerCustomProtocol(
            UserDefinedProtocolNumber.ATT_TEAM_DATE_QNA,
            QnaService.dateQuestion
        )


	# 초기 구동에서 호출하는 부분
    @staticmethod
    def registerUserDefinedProtocol():
		# 디폴트 구성
        UserDefinedProtocolRegister.registerDefaultUserDefinedProtocol()
	    # 여러분의 사용자 정의형 프로토콜 등록 파트
        UserDefinedProtocolRegister.registerIstpTestProtocol()
        # ENFP chatbot register
        UserDefinedProtocolRegister.registerEnfpTestProtocol()
        # Chatbot Feedback register
        UserDefinedProtocolRegister.registerChatbotFeedbackProtocol()
        # Finetune With Feedback register
        UserDefinedProtocolRegister.registerFinetuneWithFeedbackProtocol()
        # Date QNA register
        UserDefinedProtocolRegister.registerDateQnaProtocol()