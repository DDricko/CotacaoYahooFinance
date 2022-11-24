
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pandas_datareader.data as web

!pip install yfinance --upgrade --no-cache-dir

import yfinance as yf
yf.pdr_override()

litecoin = web.get_data_yahoo('LTC-USD')
litecoin.head()
litecoin.tail()
litecoin["Close"].plot(figsize=(22,8))