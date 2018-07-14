import requests
from bs4 import BeautifulSoup
from io import StringIO
import pandas as pd
import numpy as np

dateStr = '20180713'
req = requests.post('http://www.twse.com.tw/exchangeReport/MI_INDEX?response=csv&date=' + dateStr + '&type=ALL')


df = pd.read_csv(StringIO("\n".join([i.translate({ord(c): None for c in ' '}) 
    
for i in req.text.split('\n') 
if len(i.split('",')) == 17 and i[0] != '='])), header=0)

#print(df)

#選擇 本益比 < 15 的所有股票
df1 = df[pd.to_numeric(df['本益比'],errors='coerce')<15]

print(df1)
