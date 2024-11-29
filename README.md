Binance Futures Trading Bot
===========================

This is a Python-based Binance Futures trading bot that uses the MACD (Moving Average Convergence Divergence) indicator to generate buy and sell signals. The bot connects to Binance's futures API, evaluates market conditions, and places orders automatically.

Features
--------

-   Technical Analysis: Implements the MACD indicator to identify potential trading opportunities.
-   PnL Tracking: Monitors unrealized profits/losses and calculates percentage changes for active positions.
-   Configurable Settings: Customize key parameters such as trading symbol, MACD thresholds, position size, and more.
-   Error Handling: Graceful handling of API and runtime errors to ensure the bot remains operational.
-   Real-Time Trading: Fetches live market data and places orders on the Binance Futures platform.

Requirements
------------

-   Python 3.7 or higher
-   A Binance Futures account
-   Binance API Key and Secret
-   Installed Python libraries:
    -   `binance`
    -   `numpy`
    -   `talib`

Setup Instructions
------------------

1.  Clone the Repository:

    bash

    Copy code

    `git clone https://github.com/yourusername/binance-futures-bot.git
    cd binance-futures-bot`

2.  Install Dependencies: Install the required Python libraries using `pip`:

    bash

    Copy code

    `pip install python-binance numpy TA-Lib`

    > Note: To install TA-Lib, you may need additional build tools for your operating system. Follow [TA-Lib installation instructions](https://github.com/mrjbq7/ta-lib#installation).

3.  Set Up API Credentials:

    -   Obtain your Binance API Key and Secret from the Binance Dashboard.
    -   Replace the placeholders `API_KEY` and `API_SECRET` in the script with your credentials.
    -   Alternatively, use environment variables or a config file for enhanced security.
4.  Configure Parameters: Adjust the following settings in the script as needed:

    -   `SYMBOL`: The trading pair, e.g., `BTCUSDT`.
    -   `QUANTITY`: The position size for each trade.
    -   `FAST_PERIOD`, `SLOW_PERIOD`, `SIGNAL_PERIOD`: Parameters for the MACD indicator.
    -   `MACD_THRESHOLD`: The minimum MACD difference to trigger a buy signal.
5.  Run the Bot: Execute the script:

    bash

    Copy code

    `python main.py`

How It Works
------------

1.  The bot fetches historical price data (candlesticks) for the configured symbol.
2.  It calculates the MACD, Signal Line, and Histogram using the `talib` library.
3.  Based on the MACD crossover strategy:
    -   Buy: If MACD crosses above the Signal Line and exceeds the threshold for consecutive periods.
    -   Sell: If MACD crosses below the Signal Line or the histogram turns negative while in a long position.
4.  It tracks and prints your position's unrealized PnL and percentage change.

Disclaimer
----------

This bot is provided for educational purposes only. Use it at your own risk. Cryptocurrency trading involves significant financial risk, and you should consult with a financial advisor before engaging in trading activities.

Contributions
-------------

Contributions are welcome! Feel free to fork the repository, make improvements, and submit a pull request.

License
-------

This project is licensed under the MIT License.
