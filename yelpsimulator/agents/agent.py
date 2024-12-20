from abc import ABC, abstractmethod
from typing import Any
from ..tools.interaction_tool import InteractionTool

class Agent(ABC):
    def __init__(self):
        """
        Abstract base class for agents.
        """
        self.interaction_tool = None

    def set_interaction_tool(self, interaction_tool: InteractionTool):
        """
        Set the interaction tool for the agent.
        Args:
            interaction_tool: An instance of InteractionTool.
        """
        self.interaction_tool = interaction_tool

    @abstractmethod
    def insert_scenario(self, scenario):
        """Insert a scenario for the agent."""
        pass

    @abstractmethod
    def forward(self) -> Any:
        """Abstract forward method for evaluation."""
        pass