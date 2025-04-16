class QuoteDetailModel:
    def __init__(self, symbol: str, lastPrice: float, volume: float):
        self.symbol = symbol
        self.lastPrice = lastPrice
        self.volume = volume

    @classmethod
    def from_json(cls, api_data: dict) -> "QuoteDetailModel":
        return cls(
            symbol=api_data["symbol"],
            lastPrice=float(api_data["lastPrice"]),
            volume=float(api_data["volume"])
        )
