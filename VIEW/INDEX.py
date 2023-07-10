import json
from finvizfinance.screener.overview import Overview

# The sector divisions that will be screened
sectors = ['Basic Materials',
           'Communication Services',
           'Consumer Cyclical',
           'Consumer Defensive',
           'Energy',
           'Financial',
           'Healthcare',
           'Industrials',
           'Real Estate',
           'Technology',
           'Utilities']

# The market capitalization divisions that will be screened
market_caps = ['+Large (over $10bln)',
               'Mid ($2bln to $10bln)',
               'Small ($300mln to $2bln)',
               'Micro ($50mln to $300mln)',
               'Nano (under $50mln)']

# A structure that represents a partition of the index
slice = {
        "Sector": "",
        "Market Cap": "",
        "Tickers": []}

# A structure that holds a list of all tickers in the index and all index slices
index = {
        "Tickers": [],
        "Slices": []
        }


# Returns a list of all tickers in the index and all index slices
def generate_index():
    screener = Overview()
    index_tickers = []

    for sector in sectors:
        for market_cap in market_caps:
            # set filters and screen for corresponding stocks
            filters = {'Country': 'USA', 'Sector': sector, 'Market Cap.': market_cap}
            screener.set_filter(filters_dict=filters)
            tickers = screener.screener_view()['Ticker\n\n'].tolist()

            # create an instance of the slice structure
            index_slice = slice.copy()
            index_slice["Sector"] = sector
            index_slice["Market Cap"] = market_cap
            index_slice["Tickers"] = tickers

            # add slice to index struct and update list of tickers
            index["Slices"].append(index_slice)
            index_tickers.extend(tickers)

    # add list of tickers to index structure
    index["Tickers"] = index_tickers

    return index


# Saves index structure as JSON file
def generate_index_file(index_struct):
    with open("index.json", "w") as file:
        json.dump(index_struct, file, indent=5)


if __name__ == "__main__":
    index = generate_index()
    generate_index_file(index)


