from fastapi_ddd.domain.repositories.quotes_repository import QuotesRepository

class QuotesService:
    def __init__(self, repository: QuotesRepository):
        self.repository = repository

    def get_quote(self, symbol: str):
        return self.repository.fetch_quote(symbol)

    def get_all_quotes(self):
        return self.repository.fetch_quotes()
