import time
import numpy as np
import talib
from binance.client import Client

# Binance API credentials (leave empty for security; use environment variables or a config file)
API_KEY = ''
API_SECRET = ''

# Initialize Binance client
BASE_URL = 'https://www.binance.com/futures'
client = Client(API_KEY, API_SECRET, testnet=True, base_endpoint=BASE_URL)

# Configuration settings
SYMBOL = 'BTCUSDT'
QUANTITY = 0.1
FAST_PERIOD = 12
SLOW_PERIOD = 26
SIGNAL_PERIOD = 9
MACD_THRESHOLD = 0.0001
MACD_POSITIVE_PERIODS = 3
PNL_THRESHOLD = 0.3
TAKE_PROFIT_PCT = 0.2

# Variables to track position and trading signals
position = None
order = None
macd_positive_count = 0

while True:
    try:
        # Fetch current positions
        positions = client.futures_position_information()
        current_position = next((p for p in positions if p['symbol'] == SYMBOL), None)

        # Calculate PnL percentage if position exists
        if current_position:
            pnl = float(current_position['unRealizedProfit'])
            entry_price = float(current_position['entryPrice'])
            position_size = float(current_position['positionAmt'])

            if entry_price and position_size:
                initial_investment = abs(entry_price * position_size)
                pnl_percentage = (pnl / initial_investment) * 100 if initial_investment > 0 else 0
                print(f'Current PnL: {pnl:.2f}, PnL Percentage: {pnl_percentage:.2f}%')

        # Fetch historical kline data
        klines = client.futures_klines(symbol=SYMBOL, interval=Client.KLINE_INTERVAL_5MINUTE, limit=1000)
        closes = np.array([float(kline[4]) for kline in klines])

        # Calculate MACD
        macd, signal, hist = talib.MACD(closes, fastperiod=FAST_PERIOD, slowperiod=SLOW_PERIOD, signalperiod=SIGNAL_PERIOD)
        last_macd, last_signal, last_hist = macd[-1], signal[-1], hist[-1]

        # Buy signal: MACD crossover with threshold
        if macd[-1] > signal[-1] and macd[-2] < signal[-2]:
            macd_diff = last_macd - last_signal
            if macd_diff > MACD_THRESHOLD:
                macd_positive_count += 1
                if macd_positive_count >= MACD_POSITIVE_PERIODS and position is None:
                    order = client.futures_create_order(
                        symbol=SYMBOL,
                        side=Client.SIDE_BUY,
                        type=Client.ORDER_TYPE_MARKET,
                        quantity=QUANTITY,
                    )
                    print('Buy order executed:', order)
                    position = 'long'

        # Sell signal: MACD bearish crossover or profit target
        elif last_macd < last_signal and last_hist < 0 and position == 'long':
            order = client.futures_create_order(
                symbol=SYMBOL,
                side=Client.SIDE_SELL,
                type=Client.ORDER_TYPE_MARKET,
                quantity=QUANTITY,
            )
            print('Sell order executed:', order)
            position = None
            macd_positive_count = 0

        # Sleep to avoid rate limits
        time.sleep(30)

    except Exception as e:
        print(f'An error occurred: {e}')
