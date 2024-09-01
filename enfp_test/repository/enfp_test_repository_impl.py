import os

import httpx
import openai
import nltk

from openai import OpenAI
from dotenv import load_dotenv
from fastapi import HTTPException
from nltk import sent_tokenize

from enfp_test.repository.enfp_test_repository import EnfpTestRepository

load_dotenv()
nltk.download('punkt_tab') # 문장 분리를 위한 라이브러리

openaiApiKey = os.getenv('OPENAI_API_KEY')
if not openaiApiKey:
    raise ValueError('API Key가 준비되어 있지 않습니다.')

# fine-tuned model ID
model_enfp = os.getenv('ENFP_TEST')


class EnfpTestRepositoryImpl(EnfpTestRepository):
    __instance = None
    client = OpenAI()

    headers = {
        'Authorization': f'Bearer {openaiApiKey}',
        'Content-Type': 'application/json',
    }

    conversation_history = [
        {"role": "system", "content": "You are a helpful assistant."}
    ]

    OPENAI_CHAT_COMPLETIONS_URL = "https://api.openai.com/v1/chat/completions"

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()

        return cls.__instance

    async def generateText(self, userSendMessage):

        # 사용자 메시지를 대화 히스토리에 추가
        self.conversation_history.append({"role": "user", "content": userSendMessage})

        # # 대화 히스토리가 너무 길어지면 일부를 제거 (예: 최근 10개의 메시지만 유지)
        # if len(self.conversation_history) > 11:  # system 메시지 + 최근 10개
        #     self.conversation_history = self.conversation_history[:1] + self.conversation_history[-10:]

        data = {
            'model': model_enfp,
            'messages': self.conversation_history,
            'max_tokens': 256,
            'temperature': 1.0,
        }

        # api에 추론 요청을 보내는 부분
        async with httpx.AsyncClient(timeout=10000) as client:
            try:
                # 우리가 service, repository에서 처리했던 부분을 여기서 딸깍으로 처리해버림
                response = await client.post(self.OPENAI_CHAT_COMPLETIONS_URL, headers=self.headers, json=data)
                response.raise_for_status()

                generatedText = response.json()['choices'][0]['message']['content'].strip()

                # AI의 응답을 대화 히스토리에 추가
                # self.conversation_history.append({"role": "assistant", "content": generatedText})

                # return {"generatedText": generatedText}  # dict 형식으로 반환해주어야 함

                # NLTK를 사용하여 텍스트를 문장 단위로 나누기
                sentences = sent_tokenize(generatedText)

                # AI의 응답을 대화 히스토리에 문장 단위로 추가
                for sentence in sentences:
                    self.conversation_history.append({"role": "assistant", "content": sentence})

                # 문장 단위로 나누어진 리스트 형식으로 반환
                return {"generatedText": sentences}  # dict 형식으로 반환

            except httpx.HTTPStatusError as e:
                print(f"HTTP Error: {str(e)}")
                print(f"Status Code: {e.response.status_code}")
                print(f"Response Text: {e.response.text}")
                raise HTTPException(status_code=e.response.status_code, detail=f"HTTP Error: {e}")

            except (httpx.RequestError, ValueError) as e:
                print(f"Request Error: {e}")
                raise HTTPException(status_code=500, detail=f"Request Error: {e}")
