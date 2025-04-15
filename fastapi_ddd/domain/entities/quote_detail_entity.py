from pydantic import BaseModel

class QuoteDetailEntity(BaseModel):
    symbol: str
    price: float
    volume: float

    @classmethod
    def from_model(cls, model):
        return cls(symbol=model.symbol, price=model.price, volume=model.volume)
