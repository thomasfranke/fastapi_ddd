class QuoteSummaryModel:
    def __init__(self, symbol, price):
        self.symbol = symbol
        self.price = price

    @staticmethod
    def get(quote: str):
        return QuoteSummaryModel(symbol=quote, price=123.45)
