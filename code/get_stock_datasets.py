import yfinance as yf
from yahoo_fin.stock_info import get_data, tickers_sp500, tickers_nasdaq
import json

ticker_symbols_file = open('code\\ticker_symbols.txt','r')
ticker_symbols_string = ticker_symbols_file.read()
ticker_symbols = ticker_symbols_string.split(',')

print(ticker_symbols)

for ticker_symbol in ticker_symbols:
    data = get_data(ticker_symbol, start_date="06/25/2024", end_date="06/26/2024", index_as_date = True, interval = "1m")
    data.to_csv('code\\datasets\\output' + '_06252024_' + ticker_symbol + '.csv')