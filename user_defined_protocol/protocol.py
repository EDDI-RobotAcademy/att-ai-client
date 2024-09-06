from enum import Enum


class UserDefinedProtocolNumber(Enum):
    # 예약된 정보 (1, 2, 11, 12, 13, 21) 을 제외하고 사용하도록 함

    # 추가된 프로토콜 for ISTP test
    ATT_TEAM_ISTP_TEST = 7
    # 추가된 프로토콜 for ENFP test
    ATT_TEAM_ENFP_TEST = 8
    # 추가된 프로토콜 for Chatbot Feedback
    ATT_TEAM_CHATBOT_FEEDBACK = 9
    # 추가된 프로토콜 for Chatbot Finetune With Feedback
    ATT_TEAM_FINETUNE_WITH_FEEDBACK = 10
    # 추가된 프로토콜 for Chatbot Date QnA
    ATT_TEAM_DATE_QNA = 22

    # 기존에 있던 테스트용 프로토콜
    FIRST_USER_DEFINED_FUNCTION_FOR_TEST = 5

    @classmethod
    def hasValue(cls, value):
        return any(value == item.value for item in cls)
