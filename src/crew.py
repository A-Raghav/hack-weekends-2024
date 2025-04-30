import os
from typing import Dict
from langchain_openai import AzureChatOpenAI
from src.agents import ZenithAgents
from src.tasks import ZenithTasks
from crewai import Crew
from crewai.process import Process


class ZenithCrew:
    def __init__(self) -> None:
        self.llm = self._create_llm()
        self.agents = self._create_agents()
        self.tasks = self._create_tasks()
        self.crew = self._create_crew()

    def _create_llm(self) -> AzureChatOpenAI:
        return AzureChatOpenAI(
            azure_deployment="gpt4o",
            openai_api_type="azure",
            openai_api_version="2024-02-01",
            api_key=os.getenv("OPENAI_API_KEY"),
            azure_endpoint=os.getenv("OPENAI_ENDPOINT"),
            temperature=0.75,
        )

    def _create_agents(self) -> ZenithAgents:
        return ZenithAgents(llm=self.llm)

    def _create_tasks(self) -> ZenithTasks:
        return ZenithTasks(llm=self.llm)

    def _create_crew(self) -> Crew:
        return Crew(
            agents=[
                self.agents.qna_expert(),
                self.agents.content_writer(),
            ],
            process=Process.sequential,
            verbose=0,
        )

    def run(self, inputs: Dict):
        self.crew.tasks = [
            self.tasks.answer_question_task_1(),
            self.tasks.answer_question_task_2(),
            self.tasks.answer_question_task_3(),
            self.tasks.content_writing_task(),
            
        ]
        result = self.crew.kickoff(inputs=inputs)
        return result
