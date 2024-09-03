import os
import json

import httpx
import openai

from openai import OpenAI
from dotenv import load_dotenv
from fastapi import HTTPException
from pydantic import BaseModel

from chatbot_feedback.repository.chatbot_feedback_repository import ChatbotFeedbackRepository

load_dotenv()

openaiApiKey = os.getenv('OPENAI_API_KEY')
if not openaiApiKey:
    raise ValueError('API Key가 준비되어 있지 않습니다.')

feedbackData = []

class Feedback(BaseModel):
    fineTuneId: str # game fine-tuning된 모델 아이디
    prompt: str # 헛소리 했을 때의 질문
    response: str # 헛소리한 답
    feedback: str # positive or negative
    betterResponse: str = None # 더 나은 답변 제안, 만약 positive로 찍혔다면 나은 답변이 필요 없으므로 None 설정

class ChatbotFeedbackRepositoryImpl(ChatbotFeedbackRepository):
    __instance = None
    client = OpenAI()

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

    def giveChatbotFeedback(self, feedback: Feedback):
        feedbackData.append(feedback.dict()) # feedback 데이터 내용을 feedbackData list에 추가
        print(f"feedbackData: {feedbackData}")
        return {"status": "Feedback received"}

    def saveTrainingData(self, trainingData, filename="training_data.jsonl"):
        with open(filename, "w") as file:
            for item in trainingData: # trainingData에 있는 것들을 모두 저장
                file.write(json.dumps(item) + "\n")