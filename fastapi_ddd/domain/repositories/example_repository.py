from abc import ABC, abstractmethod
from fastapi_ddd.domain.entities.example_entity import Example

class ExampleRepository(ABC):
    @abstractmethod
    def get_example(self) -> Example:
        pass
