import datetime as dt
import pandas as pd

import typing
#import streamlit as st
import yfinance as yf
import matplotlib.pyplot as plt


def get_symbol_dict(symbol: str):
    return yf.Ticker(symbol)

def get_revenue(stock_info: dict):
    return stock_info.info['totalRevenue']

def get_market_cap(stock_info: dict):
    return stock_info.info['marketCap']

def price_to_earnings(stock_info: dict):
    return stock_info.info['trailingPE']

def price_to_sales(stock_info: dict):
    return stock_info.info['priceToSalesTrailing12Months']

#Todo: Generalize to more
def get_stock_data(sym_1: str, sym_2: str, start_date: str):
  sym_1_df = yf.download(sym_1, start=start_date)[['Adj Close']]
  sym_2_df = yf.download(sym_2, start=start_date)[['Adj Close']]
  dual_df = pd.merge(sym_1_df, 
                     sym_2_df,
                     left_index=True, 
                     right_index=True, 
                     suffixes=('_'+sym_1,'_'+sym_2))
  dual_df.columns = dual_df.columns.str.replace('Adj Close_', '')
  return dual_df
      
syms = ['GOOG', 'FB', 'UDMY', 'BOX','AAPL','AMZN','MSFT']

syms = ['SNOW', 'OKTA', 'MDB', 'AYX', 'AI', 'UBER', 'NFLX']

for sym in syms:
    sym_info = get_symbol_dict(sym)
    try:
        p_to_s = price_to_sales(sym_info)
        #p_to_e = price_to_earnings(sym_info) #TODO: Deal with negative earnings
    except:
        print(sym_info, 'Has missing data') 
        pass
    print('Price_to_Sales', sym, p_to_s)
    #print('Price_to_Earnings', sym, p_to_e)


# appendix
dual_df = get_stock_data("GOOG","BOX", start_date='2021-01-01')
sym_info.info['earningsGrowth']
plt.style.use('fivethirtyeight')
dual_df.div(dual_df.iloc[0]).plot(title = 'Performance relative to start date')
plt.show()
