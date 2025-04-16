class QuoteSummaryModel:
    def __init__(self, symbol: str, price: float):
        self.symbol = symbol
        self.price = price

    @classmethod
    def from_json(cls, api_data: dict) -> "QuoteSummaryModel":
        return cls(
            symbol=api_data["symbol"],
            price=float(api_data["price"]),
        )
