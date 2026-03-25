from crewai import Agent, Crew, Process, Task , LLM
from crewai.project import CrewBase, agent, crew, task 
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List
import os

groq_llm = LLM(
    model="groq/llama-3.3-70b-versatile",
    api_key=os.getenv("GROQ_API_KEY")
)

#define the class fro our crew 
@CrewBase
class DemoCrew():

    agents: List[BaseAgent]
    tasks: List[Task]

    #define the paths of config files 
    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"

    # agents (order of task defination dosent matters here )
    @agent
    def report_genarator(self) -> Agent:
        return Agent(
            config=self.agents_config["report_genarator"],
            llm=groq_llm
        )
    
    @agent
    def blog_writer(self) -> Agent:
        return Agent(
            config=self.agents_config["blog_writer"],
            llm=groq_llm
        )
    
    # Tasks (order of task defination matters here )
    @task
    def report_task(self) -> Task:
        return Task(
            config=self.tasks_config["report_task"],
            llm=groq_llm
        )
    @task
    def blog_writing_task(self) -> Task:
        return Task(
            config=self.tasks_config["blog_writing_task"],
            llm=groq_llm,
            output_file="blogs/blog.md"
        )

    # Crew 
    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True
        )

