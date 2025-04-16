from fastapi_ddd.domain.repositories.quotes_repository import QuotesRepository
from fastapi_ddd.domain.entities.quote_detail_entity import QuoteDetailEntity
from fastapi_ddd.domain.entities.quote_summary_entity import QuoteSummaryEntity

class QuotesService:
    def __init__(self, repository: QuotesRepository):
        self.repository = repository

    def get_quote(self, quote: str) -> QuoteSummaryEntity:
        model = self.repository.fetch_quote(quote)
        return QuoteSummaryEntity.from_model(model)

    def get_quotes(self) -> list[QuoteDetailEntity]:
        models = self.repository.fetch_quotes()
        return [QuoteDetailEntity.from_model(m) for m in models]
