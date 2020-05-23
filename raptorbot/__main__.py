import json
import sys

from binance.client import Client
from binance.websockets import BinanceSocketManager

from core.data.DailyTickerData import DailyTickerData
from core.data.TradeData import TradeData

with open("config.json") as jsonConfigFile:
    config = json.load(jsonConfigFile)

client = Client(config["exchanges"]["binance"]["api_key"], config["exchanges"]["binance"]["api_secret"])
bm = BinanceSocketManager(client)


def process_message(msg):
    if msg['e'] == 'error':
        # close and restart the socket
        bm.stop_socket(conn_key1)
        conn_key1 = bm.start_trade_socket('BTCUSDT', process_message)
        bm.stop_socket(conn_key2)
        conn_key2 = bm.start_symbol_ticker_socket('BTCUSDT', process_message)
    else:
        # process message normally
        if msg['e'] == "24hrTicker":
            dailyTickerData = DailyTickerData(msg, True)
            print("Weighted price: {}".format(dailyTickerData.weightedAveragePrice))
        elif msg['e'] == "trade":
            tradeData = TradeData(msg, True)
            print("Someone bought {} for price {}".format(tradeData.quantity, tradeData.price))
        else:
            print("message type: {}".format(msg['e']))
            print(msg)


    # do something

conn_key1 = bm.start_trade_socket('BTCUSDT', process_message)
conn_key2 = bm.start_symbol_ticker_socket('BTCUSDT', process_message)

# start any sockets here, i.e a trade socket
# then start the socket manager
bm.start()
