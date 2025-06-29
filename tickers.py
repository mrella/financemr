import pandas as pd
#### CONJUNTOS DE TICKERS
tickers_qqq =  ["AAPL","ABNB","ADBE","ADI","ADP","ADSK","AEP","AMAT","AMD","AMGN",
    "AMZN","ANSS","APP","ARM","ASML","AVGO","AXON","AZN","BIIB","BKNG",
    "BKR","CCEP","CDNS","CDW","CEG","CHTR","CMCSA","COST","CPRT","CRWD",
    "CSCO","CSGP","CSX","CTAS","CTSH","DASH","DDOG","DXCM","EA","EXC",
    "FANG","FAST","FTNT","GEHC","GFS","GILD","GOOG","GOOGL","HON","IDXX",
    "INTC","INTU","ISRG","KDP","KHC","KLAC","LIN","LRCX","LULU","MAR",
    "MCHP","MDLZ","MELI","META","MNST","MRVL","MSFT","MSTR","MU","NFLX",
    "NVDA","NXPI","ODFL","ON","ORLY","PANW","PAYX","PCAR","PDD","PEP",
    "PLTR","PYPL","QCOM","REGN","ROP","ROST","SBUX","SHOP","SNPS","TEAM",
    "TMUS","TSLA","TTD","TTWO","TXN","VRSK","VRTX","WBD","WDAY","XEL","ZS","QQQ"]
tickers_spy = pd.read_html('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')[0]['Symbol'].tolist() + ['SPY']
tickers_spy_qqq = tickers_spy + tickers_qqq
