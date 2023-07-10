import math

# Simple Moving Average
def calculate_sma(stock_prices):
    total_weight = len(stock_prices)
    total_sum = sum(stock_prices)
    sma = total_sum / total_weight

    return sma


# Exponential Moving Average
def calculate_ema(closing_prices):
    total_weight = sum(math.exp(i) for i in range(len(closing_prices)))
    weighted_sum = sum(price * math.exp(i) for i, price in enumerate(closing_prices))
    ema = weighted_sum / total_weight

    return ema