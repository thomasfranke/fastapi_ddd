from pydantic import BaseModel

class QuoteSummaryEntity(BaseModel):
    symbol: str
    price: float

    @classmethod
    def from_model(cls, model):
        return cls(symbol=model.symbol, price=model.price)
