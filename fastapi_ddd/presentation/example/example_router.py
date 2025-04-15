from fastapi import APIRouter
from fastapi_ddd.data.repositories.example_repository_impl import ExampleRepositoryImpl
from fastapi_ddd.domain.entities.example_entity import Example

router = APIRouter()

@router.get("/example", response_model=Example)
def get_example():
    repo = ExampleRepositoryImpl()
    return repo.get_example()
