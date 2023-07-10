from finvizfinance.screener.overview import Overview
foverview = Overview()
filters_dict = {'Exchange':'AMEX','Sector':'Basic Materials'}
foverview.set_filter(filters_dict=filters_dict)
tickers = foverview.screener_view()['Ticker\n\n'].tolist()

print(tickers)