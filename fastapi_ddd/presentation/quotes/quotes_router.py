from fastapi import APIRouter
from fastapi_ddd.data.repositories.quotes_repository_impl import QuotesRepositoryImpl
from fastapi_ddd.domain.services.quotes_service import QuotesService
from fastapi_ddd.domain.entities.quote_summary_entity import QuoteSummaryEntity
from fastapi_ddd.domain.entities.quote_detail_entity import QuoteDetailEntity

router = APIRouter()
repo = QuotesRepositoryImpl()
service = QuotesService(repo)

@router.get("/quotes/{symbol}", response_model=QuoteSummaryEntity)
def get_quote(symbol: str):
    return service.get_quote(symbol)

@router.get("/quotes", response_model=list[QuoteDetailEntity])
def get_quotes():
    return service.get_quotes()
