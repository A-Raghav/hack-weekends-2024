from crewai import Task
from crewai.project import task
from src.agents import ZenithAgents


class ZenithTasks(ZenithAgents):
    @task
    def answer_question_task_1(self) -> Task:
        return Task(
            config=self.tasks_config["answer_question_task_1"],
            agent=self.qna_expert(),
        )

    @task
    def answer_question_task_2(self) -> Task:
        return Task(
            config=self.tasks_config["answer_question_task_2"],
            agent=self.qna_expert(),
        )

    @task
    def answer_question_task_3(self) -> Task:
        return Task(
            config=self.tasks_config["answer_question_task_3"],
            agent=self.qna_expert(),
        )

    @task
    def content_writing_task(self) -> Task:
        return Task(
            config=self.tasks_config["content_writing_task"],
            agent=self.content_writer(),
            context=[
                self.answer_question_task_1(),
                self.answer_question_task_2(),
                self.answer_question_task_3(),
            ]
        )
