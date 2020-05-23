from dataclasses import dataclass


@dataclass
class DailyTickerData:
    eventTime: int
    symbol: str
    priceChange: str
    priceChangePercent: str
    weightedAveragePrice: str
    lastPrevious24HourWindowTrade: str
    lastPrice: str
    lastQuantity: str
    bestBidPrice: str
    bestBidQuantity: str
    bestAskPrice: str
    bestAskQuantity: str
    openPrice: str
    highPrice: str
    lowPrice: str
    totalTradedBaseAssetVolume: str
    totalTradedQuoteAssetVolume: str
    statisticsOpenTime: int
    statisticsCloseTime: int
    firstTradeID: int
    lastTradeId: int
    totalNumberOfTrades: int

    def __init__(self, data: dict, sourceBinance: bool):
        if (sourceBinance == True):
            # If this assertion fails, this means that the binance api updated.
            # Please update this mapping to the newest API version.
            assert(len(data.keys()) - 1 == 22)
            self.eventTime = data["E"]
            self.symbol = data["s"]
            self.priceChange = data["p"]
            self.priceChangePercent = data["P"]
            self.weightedAveragePrice = data["w"]
            self.lastPrevious24HourWindowTrade = data["x"]
            self.lastPrice = data["c"]
            self.lastQuantity = data["Q"]
            self.bestBidPrice = data["b"]
            self.bestBidQuantity = data["B"]
            self.bestAskPrice = data["a"]
            self.bestAskQuantity = data["A"]
            self.openPrice = data["o"]
            self.highPrice = data["h"]
            self.lowPrice = data["l"]
            self.totalTradedBaseAssetVolume = data["v"]
            self.totalTradedQuoteAssetVolume = data["q"]
            self.statisticsOpenTime = data["O"]
            self.statisticsCloseTime = data["C"]
            self.firstTradeID = data["F"]
            self.lastTradeId = data["L"]
            self.totalNumberOfTrades = data["n"]
