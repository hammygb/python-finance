# Yahoo Finance API
import yfinance as yf

# Ticker Symbol GAW.L is for a company called 'Games Workshop Group Plc'
gaw = yf.Ticker("GAW.L")

# get stock info
gaw.info

# show actions (dividends, splits)
gaw.actions

print(gaw.actions)
