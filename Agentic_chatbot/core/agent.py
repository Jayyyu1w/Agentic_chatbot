from langgraph.graph import StateGraph, START, END
from .state import AgentState
from tools.search import SearchTool


class Agent:
    """
    聊天代理
    """
    def __init__(self, name: str):
        self.name = name
        self.state_graph = StateGraph(AgentState)
        # TODO: 流程開發完後需要串接LLM
        self.llm = None

    def _generate(self, state):
        """
        Generate answer

        Args:
            state (messages): The current state

        Returns:
             dict: The updated state with re-phrased question
        """
        print("---GENERATE---")
        question = state.question

        print("question:", question)

        return {"question": question, "generation": "123"}
    

    def build(self):
        self.state_graph.add_node("generation", self._generate)
        self.state_graph.add_edge(
            START,
            "generation"
        )
        self.state_graph.add_edge(
            "generation",
            END
        )

        graph = self.state_graph.compile()

        return graph