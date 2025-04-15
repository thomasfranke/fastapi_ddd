class QuoteDetailModel:
    def __init__(self, symbol, price, volume):
        self.symbol = symbol
        self.price = price
        self.volume = volume

    @staticmethod
    def all():
        return [
            QuoteDetailModel(symbol="BTC", price=123.45, volume=1000),
            QuoteDetailModel(symbol="ETH", price=234.56, volume=2000),
        ]
