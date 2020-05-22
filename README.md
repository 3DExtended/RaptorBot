# Welcome to RaptorBot v0.0.0

This repository includes a trading bot written in Python 3. 
At the moment, this is NOT **WORKING**, which means that this repository might be useless to you.

 
The plan for this repository is the following:
We want to create a trading bot, which is capable of trading crypto currencies on the exchange [Binance](https://www.binance.com/). It should offer a set of features that makes implementing a new strategy seemless and handle all the required communication details for you. It also should offer a set of technical analysis tools such as RSI or MA. However, the first goal for this project is a tool which allows you to watch your current assets on [Binance](https://www.binance.com/).

# Features

All the features currently implemented can be found here:

 - Nothing is implemented... 
 
 # Roadmap
 
 The list of things to implement for this bot is pretty long. This is not a complete list of things we might want but instead focuses on the long time goals only. If you want to see a complete list of features that are planned, please visit the project page of this repository.
 
  - Asset monitoring on [Binance](https://www.binance.com/).
  The plan here is, to provide a CLI tool for monitoring your assets both as a current itself and the estimated worth of each asset in a selectable base currency. 
  - Manual trading of assets.
  We want a tool that allows us to make real transactions using the [Binance](https://www.binance.com/) exchange in a manual manner. This means, that our tool has to parse CLI commands and translate them into buy or sell commands for different crypto coins. 
  - Automated tranding based on strategies
  We want the ability to write a strategy, which determines when to sell or to buy based which asset.
  - Backtest a given strategy
  - Automated Generic Strategy optimizer 
  
# Disclaimer

- RaptorBot is **NOT** a sure-fire profit machine. **Use it AT YOUR OWN RISK!!!**
- Crypto-Currencies are still an experiment. There is no gurantee that it will exist forever. Therefore, RaptorBot is also an experiment which also can fail at any time!
- Never leave the bot unmonitored for too long. The bot is only as good as your strategy which could fail at any time!
- None of the provided strategies will perform as you want! You have to make modifications to at least the parameters to find the settings that work for you!
