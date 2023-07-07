from metrics import calculate_sma, calculate_ema

prices = [70, 102, 105, 102, 107, 110, 105, 103, 104, 110, 101, 102, 105, 102, 107, 110, 105, 103, 110, 110]

def test_calculate_sma():
    sma = calculate_sma(prices)
    print("SMA: " + str(sma))

def test_calculate_ema():
    ema = calculate_ema(prices)
    print("EMA: " + str(ema))




if __name__ == "__main__":
    test_calculate_sma()
    test_calculate_ema()
