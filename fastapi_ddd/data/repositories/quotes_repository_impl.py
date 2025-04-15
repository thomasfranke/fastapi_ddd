import httpx
from fastapi_ddd.domain.repositories.quotes_repository import QuotesRepository
from fastapi_ddd.domain.entities.quote_summary_entity import QuoteSummaryEntity
from fastapi_ddd.domain.entities.quote_detail_entity import QuoteDetailEntity

class QuotesRepositoryImpl(QuotesRepository):
    def fetch_quote(self, quote: str) -> QuoteSummaryEntity:
        url = f"https://api.binance.com/api/v3/ticker/price?symbol={quote}"
        response = httpx.get(url)
        data = response.json()

        return QuoteSummaryEntity(
            symbol=data["symbol"],
            price=float(data["price"])
        )

    def fetch_quotes(self) -> list[QuoteDetailEntity]:
        url = "https://api.binance.com/api/v3/ticker/24hr"
        response = httpx.get(url)
        data = response.json()

        quotes = []
        for item in data:
            if "USDT" in item["symbol"]:  # Filtrando apenas pares com USDT
                quotes.append(QuoteDetailEntity(
                    symbol=item["symbol"],
                    price=float(item["lastPrice"]),
                    volume=float(item["volume"])
                ))

        return quotes
