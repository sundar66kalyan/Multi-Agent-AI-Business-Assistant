from abc import ABC
from abc import abstractmethod
from sqlalchemy.orm import Session


class BaseAgent(ABC):

    @property
    @abstractmethod
    def name(self):
        pass

    @abstractmethod
    def execute(
        self,
        message: str,
        db: Session = None
    ):
        pass