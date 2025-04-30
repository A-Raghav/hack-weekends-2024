import yaml
from pathlib import Path
from crewai import Agent
from crewai.project import agent
from langchain_openai import AzureChatOpenAI


root = Path().absolute()
config_dir = root / "src/config"


class ZenithAgents:
    """Data Zenith Agents

    This class contains all Agents that form the Crew required to perform
    question-answering. The goal and backstory of the agents are defined
    in `src/config/agents.yaml`."""

    def __init__(self, llm: AzureChatOpenAI) -> None:
        self.agents_config = yaml.safe_load(open(config_dir / "agents.yaml"))
        self.tasks_config = yaml.safe_load(open(config_dir / "tasks.yaml"))
        self.llm = llm

    @agent
    def qna_expert(self) -> Agent:
        return Agent(
            config=self.agents_config["qna_expert"],
            llm=self.llm,
        )

    @agent
    def content_writer(self) -> Agent:
        return Agent(
            config=self.agents_config["content_writer"],
            llm=self.llm,
        )
