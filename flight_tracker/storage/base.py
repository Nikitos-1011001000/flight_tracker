from abc import ABC, abstractmethod
from src.models import Airplane


class BaseStorage(ABC):
    @abstractmethod
    def add(self, airplane: Airplane) -> None:
        pass

    @abstractmethod
    def get_by(self, **criteria):
        pass

    @abstractmethod
    def remove(self, **criteria) -> int:
        pass
