from abc import ABC, abstractmethod
from fastapi_ddd.domain.entities.quote_summary_entity import QuoteSummaryEntity
from fastapi_ddd.domain.entities.quote_detail_entity import QuoteDetailEntity

class QuotesRepository(ABC):
    @abstractmethod
    def fetch_quote(self, quote: str) -> QuoteSummaryEntity:
        pass
    
    @abstractmethod
    def fetch_quotes(self) -> list[QuoteDetailEntity]:
        pass