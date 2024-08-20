import os
import openai

from istp_test.repository.istp_test_repository import IstpTestRepository
from openai import OpenAI
from dotenv import load_dotenv


load_dotenv()

openaiApiKey = os.getenv('OPENAI_API_KEY')
if not openaiApiKey:
    raise ValueError('API Key가 준비되어 있지 않습니다.')

# fine-tuned model ID
model_istp = os.getenv('ISTP_TEST')

class IstpTestRepositoryImpl(IstpTestRepository):
    __instance = None

    client = OpenAI()
    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()

        return cls.__instance

    def generateText(self, userSendMessage):
        response = openai.ChatCompletion.create(
            model=model_istp,  # 파인튜닝된 모델 ID
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},  # 시스템 메시지
                {"role": "user", "content": userSendMessage},  # 사용자 입력
            ]
        )

        return response['choices'][0]['message']['content']