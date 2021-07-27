from datetime import datetime
from jesse import research
from pandas.plotting import register_matplotlib_converters

import matplotlib.pyplot as plt
import jesse.indicators as ta

register_matplotlib_converters()
research.init()

eth_candles = research.get_candles('Binance', 'ETH-USDT', '4h', '2019-07-28', '2019-09-28')
eth_sma_50 = ta.sma(eth_candles, 50, sequential=True)
eth_close = eth_candles[:, 2]

# convect timestamps into a format that is supported for plotting
times = []
for c in eth_candles:
    times.append(datetime.fromtimestamp(c[0] / 1000))

plt.figure(figsize=(15, 6))
plt.plot(times, eth_close, color='blue', label='ETH')
plt.plot(times, eth_sma_50, color='black', label='SMA 50')
plt.legend()
plt.show()
