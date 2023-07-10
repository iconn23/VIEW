import yfinance as yf


def get_historical_data(ticker):
    stock = yf.Ticker(ticker)
    historical_data = stock.history(period="1mo")
    return historical_data
