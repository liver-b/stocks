import yfinance as yf
from yahoo_fin.stock_info import get_data
import json

data = get_data('AAPL', start_date="06/24/2024", end_date="06/29/2024", index_as_date = True, interval = "1m")
data.to_csv('output.csv')