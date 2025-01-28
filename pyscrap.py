'''
PYSCRAP MAIN SCRIPT 
AUTHOUR: 
1. KALYAN RAPARTHI / [ qb ], kalyan.raparthi@hotmail.com, GitHub: kalyan-raparthi
'''

financial_urls = [
    # Stock Market Data
    "https://www.nasdaq.com",
    "https://www.nyse.com",
    "https://www.nseindia.com",
    "https://www.bseindia.com",
    "https://www.londonstockexchange.com",
    "https://www.hkex.com.hk",
    "https://www.asx.com.au",
    
    # Financial News
    "https://www.reuters.com/finance",
    "https://www.bloomberg.com",
    "https://www.cnbc.com",
    "https://www.ft.com",
    "https://www.economist.com",
    "https://www.forbes.com",
    "https://www.marketwatch.com",
    
    # Investment Tools and Research
    "https://www.morningstar.com",
    "https://www.zacks.com",
    "https://www.investopedia.com",
    "https://www.valuewalk.com",
    "https://seekingalpha.com",
    "https://www.fool.com",
    
    # Cryptocurrency Data
    "https://www.coingecko.com",
    "https://www.coinmarketcap.com",
    "https://www.blockchain.com",
    
    # Government and Regulatory Data
    "https://www.sec.gov",
    "https://www.rbi.org.in",
    "https://www.federalreserve.gov",
    
    # Financial APIs and Services
    "https://www.alphavantage.co",
    "https://www.quandl.com",
    "https://iexcloud.io",
    "https://polygon.io",
    "https://www.yahoofinanceapi.com",
    
    # Personal Finance and Portfolio Management
    "https://www.robinhood.com",
    "https://www.wealthfront.com",
    "https://www.mint.com",
    "https://www.personalcapital.com",
]

import http.client

url = "kalyan-raparthi.github.io"
con = http.client.HTTPSConnection(url)
con.request('GET', '/')

response  = con.getresponse()
print(response.read().decode('utf-8'))

con.close()

