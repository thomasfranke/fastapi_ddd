import httpx
from fastapi_ddd.domain.repositories.quotes_repository import QuotesRepository
from fastapi_ddd.data.models.quote_detail_model import QuoteDetailModel
from fastapi_ddd.data.models.quote_summary_model import QuoteSummaryModel

class QuotesRepositoryImpl(QuotesRepository):
    def fetch_quote(self, quote: str) -> QuoteSummaryModel:
        url = f"https://api.binance.com/api/v3/ticker/price?symbol={quote}"
        response = httpx.get(url)
        data = response.json()

        return QuoteSummaryModel.from_json(data)

    def fetch_quotes(self) -> list[QuoteDetailModel]:
        url = "https://api.binance.com/api/v3/ticker/24hr"
        response = httpx.get(url)
        data = response.json()

        return [QuoteDetailModel.from_json(item) for item in data]

