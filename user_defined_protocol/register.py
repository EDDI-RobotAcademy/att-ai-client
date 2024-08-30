import os
import sys

from enfp_test.service.enfp_test_service_impl import EnfpTestServiceImpl
from enfp_test.service.request.enfp_test_request import EnfpTestRequest
from enfp_test.service.response.enfp_test_response import EnfpTestResponse
from first_user_defined_function_domain.service.fudf_service_impl import FudfServiceImpl
from first_user_defined_function_domain.service.request.fudf_just_for_test_request import FudfJustForTestRequest
from first_user_defined_function_domain.service.response.fudf_just_for_test_response import FudfJustForTestResponse
from istp_test.service.istp_test_service_impl import IstpTestServiceImpl
from istp_test.service.request.istp_test_request import IstpTestRequest
from istp_test.service.response.istp_test_response import IstpTestResponse

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

	# 초기 구동에서 호출하는 부분
    @staticmethod
    def registerUserDefinedProtocol():
		# 디폴트 구성
        UserDefinedProtocolRegister.registerDefaultUserDefinedProtocol()
	    # 여러분의 사용자 정의형 프로토콜 등록 파트
        UserDefinedProtocolRegister.registerIstpTestProtocol()
        # ENFP chatbot register
        UserDefinedProtocolRegister.registerEnfpTestProtocol()