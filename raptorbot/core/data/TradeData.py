from dataclasses import dataclass


@dataclass
class TradeData:
    eventTime: int
    symbol: str
    tradeId: int
    price: str
    quantity: str
    buyerOrderId: int
    sellerOrderId: int
    tradeTime: int
    isBuyerMarketMaker: bool # If isBuyerMarketMaker is true then that means a seller fulfilled a buy order. The buyer created the order and waited for someone to fulfill it.
    ignore: bool

    def __init__(self, data: dict, sourceBinance: bool):
        if (sourceBinance == True):
            # If this assertion fails, this means that the binance api updated.
            # Please update this mapping to the newest API version.
            assert(len(data.keys()) - 1 == 10)
            self.eventTime = data["E"]
            self.symbol = data["s"]
            self.tradeId = data["t"]
            self.price = data["p"]
            self.quantity = data["q"]
            self.buyerOrderId = data["b"]
            self.sellerOrderId = data["a"]
            self.tradeTime = data["T"]
            self.isBuyerMarketMaker = data["m"]
            self.ignore = data["M"]
