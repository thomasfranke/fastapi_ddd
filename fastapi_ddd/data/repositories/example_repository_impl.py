from fastapi_ddd.domain.entities.example_entity import Example
from fastapi_ddd.domain.repositories.example_repository import ExampleRepository

class ExampleRepositoryImpl(ExampleRepository):
    def get_example(self) -> Example:
        return Example(id=1, message="Hello from DDD + FastAPI")
