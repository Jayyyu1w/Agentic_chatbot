from config import Config
from core.agent import Agent
from core.state import AgentState

if __name__ == "__main__":
    config = Config()
    print(config.llm_provider)
    agent = Agent("Test")
    graph = agent.build()
    state = AgentState(
        question="who are you?",
    )
    ans = graph.invoke(state)
    print(ans)