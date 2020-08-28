import ctypes
import sys
import threading
import time
from threading import Thread
from time import sleep

from binance.client import Client
from binance.enums import *
from binance.websockets import BinanceSocketManager

from core.Config import Config
from core.data.DailyTickerData import DailyTickerData
from core.data.TradeData import TradeData
from core.ForceCloseableThread import ForceCloseableThread
from plotting.RealtimePlot import RealtimePlot

config = Config()

client = Client(config["exchanges"]["binance"]["api_key"], config["exchanges"]["binance"]["api_secret"])
bm = BinanceSocketManager(client)

plot = RealtimePlot('Binance: BTC-USDT')

threads = []

def todo_make_this_call_a_strategy(event):
    print("Thread starting for event: {}, length of previous trades: {}".format(event[0], len(event[1])))
    while True: 
        break # pass

last_exchange_trades = []

def process_binance_message(msg):
    global threads
    global last_exchange_trades

    if msg['e'] == 'error':
        # close and restart the socket
        bm.stop_socket(conn_key1)
        conn_key1 = bm.start_trade_socket('BTCUSDT', process_binance_message) # returns "trade" objects
        bm.stop_socket(conn_key2)
        conn_key2 = bm.start_symbol_ticker_socket('BTCUSDT', process_binance_message) # returns "24hrTicker" objects
        bm.stop_socket(conn_key3)
        conn_key3 = bm.start_user_socket(process_binance_message)
    else:
        # process message normally
        if msg['e'] == "24hrTicker":
            dailyTickerData = DailyTickerData(msg, True)
            # print("Weighted price: {}".format(dailyTickerData.weightedAveragePrice))
        elif msg['e'] == "trade":
            tradeData = TradeData(msg, True)
            plot.add_new_datapoint(tradeData.eventTime, tradeData.price)

            number_of_trading_voting_threads = config["trading"]["number_of_threads"]

            if len(threads) >= number_of_trading_voting_threads:
                thread = threads[0]
                if thread is not None and thread.isAlive() == True:
                    thread.forcefully_close()
                    thread.join()
                thread = None

            thread = ForceCloseableThread(todo_make_this_call_a_strategy, tradeData, last_exchange_trades)
            thread.start()
            threads.append(thread)
            threads = threads[-number_of_trading_voting_threads:]
            last_exchange_trades.append(tradeData)
        else:
            print("message type: {}".format(msg['e']))
            print(msg)

conn_key1 = bm.start_trade_socket('BTCUSDT', process_binance_message) # returns "trade" objects
conn_key2 = bm.start_symbol_ticker_socket('BTCUSDT', process_binance_message) # returns "24hrTicker" objects
conn_key3 = bm.start_user_socket(process_binance_message)


# test some stuff. todo remove this.
info = client.get_account()
status = client.get_account_status()
fees = client.get_trade_fee()
fee = client.get_trade_fee(symbol='BTCUSDT')
details = client.get_asset_details()

# start any sockets here, i.e a trade socket
# then start the socket manager
bm.start()
plot.start()
