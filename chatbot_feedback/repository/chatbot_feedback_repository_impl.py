import os
import json

import httpx
import openai

from openai import OpenAI
from dotenv import load_dotenv
from fastapi import HTTPException, BackgroundTasks

from chatbot_feedback.repository.chatbot_feedback_repository import ChatbotFeedbackRepository

load_dotenv()

openaiApiKey = os.getenv('OPENAI_API_KEY')
if not openaiApiKey:
    raise ValueError('API Key가 준비되어 있지 않습니다.')

class ChatbotFeedbackRepositoryImpl(ChatbotFeedbackRepository):
    __instance = None
    client = OpenAI()
    file_path = "feedbackData.jsonl"
    training_file_path = "trainingData.jsonl"

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

    async def giveChatbotFeedback(self, feedback):
        feedback_json = json.dumps(feedback)

        with open(self.file_path, "a") as file:
            file.write(feedback_json + "\n")  # JSONL 형식에 맞게 각 JSON 객체를 한 줄로 추가

        return {"status": "Feedback received"}

    def saveTrainingData(self, trainingData, filename="training_data.jsonl"):
        with open(filename, "w") as file:
            for item in trainingData: # trainingData에 있는 것들을 모두 저장
                file.write(json.dumps(item) + "\n")

    def processFeedback(self):
        # 피드백 데이터를 읽고 처리합니다.
        training_data = []

        try:
            # trainingData.jsonl 파일을 읽어서 기존의 훈련 데이터를 가져옵니다.
            if os.path.exists(self.training_file_path):
                with open(self.training_file_path, "r") as file:
                    for line in file:
                        training_data.append(json.loads(line.strip()))

            # feedbackData.jsonl 파일을 읽어서 피드백을 처리합니다.
            if os.path.exists(self.file_path):
                with open(self.file_path, "r") as file:
                    for line in file:
                        item = json.loads(line.strip())  # JSONL 형식에서 각 줄을 JSON으로 변환
                        if item.get('feedback') == 'negative':
                            # 부정적인 피드백에 대한 개선된 응답을 수집
                            betterResponse = item.get('betterResponse')
                            if not betterResponse:  # 부정적인 피드백이 왔는데, 나은 답변이 없는 상태
                                betterResponse = f"이것은 잘못된 답변입니다: {item.get('response')}"

                            newTrainingExample = {
                                "messages": [
                                    {"role": "system", "content": "너의 MBTI는 ENFP야. 너는 현재 상대방과 이성으로서 알아가는 대화를 나누고 있어. 그리고 너는 사람처럼 대답해야 해."},
                                    {"role": "user", "content": item['prompt']},
                                    {"role": "assistant", "content": betterResponse}
                                ]
                            }

                            # 새로운 훈련 데이터를 training_data에 추가합니다.
                            training_data.append(newTrainingExample)

                # 업데이트된 training_data를 파일에 저장합니다.
                self.saveTrainingData(training_data, self.training_file_path)

        except FileNotFoundError:
            print(f"File {self.file_path} not found.")
        except json.JSONDecodeError as e:
            print(f"JSON decode error: {e}")
        except Exception as e:
            print(f"An error occurred: {e}")

    # 파인튜닝을 시작하는 함수
    def startFineTuning(self):
        # self.saveTrainingData(trainingData) #굳이 한번 더 저장?

        # filePath = "training_data.jsonl"
        # 모델의 행동을 좀 더 customize시킨다.
        with open(self.training_file_path, "rb") as file:
            # file을 읽어서 finetuning 목적으로 생성
            response = openai.files.create(file=file, purpose='fine-tune')

        fileId = response.id
        print(f"fileId : {fileId}") # file-KpJNowG2u7qG7tIsj3CUdqPC => 이게 뭐지?
        fineTuneResponse = openai.fine_tuning.jobs.create(
            training_file=fileId,
            model="ft:gpt-4o-mini-2024-07-18:personal:enfp-100q:A2J6RGik",
            # hyperparameters에서 세부사항 조정 가능
            hyperparameters={
                "n_epochs": 10  # default는 5번임
            }
        )
        return fineTuneResponse.id

    def checkFineTuneStatus(self, fineTuneId):
            statusResponse = openai.fine_tuning.jobs.retrieve(fineTuneId)
            status = statusResponse.status
            print(f"Fine-tuning status for {fineTuneId}: {status}")

    async def finetuneWithFeedback(self, backgroundTasks: BackgroundTasks):
        self.processFeedback()  # 피드백을 처리하여 새로운 훈련 데이터를 생성
        # print(f"finetuneWithFeedback traing data에 추가 까지 완료")
        newFineTuneId = self.startFineTuning()  # 새로운 데이터로 모델을 미세 조정
        print(f"newFineTuneId : {newFineTuneId}")

        self.checkFineTuneStatus(fineTuneId=newFineTuneId)
        # backgroundTasks.add_task(self.checkFineTuneStatus,newFineTuneId) # 튜닝 id를 기반으로 파인 튜닝이 잘 되었는지 check하기
        return {"status": "Fine-tuning started with feedback", "fineTuneId": newFineTuneId}