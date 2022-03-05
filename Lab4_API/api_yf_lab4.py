import requests
import sys

#python3 api_yf_lab4.py orcl,tsla,msft,xy,notreal

url = "https://yfapi.net/v6/finance/quote"

args = sys.argv[1]
#querystring = {"symbols":"AAPL,BTC-USD,EURUSD=X"}
querystring = {"symbols":args}

input_stocks = args.split(",")
input_stocks = [s.lower() for s in input_stocks]

headers = {
    'x-api-key': "fFrf8tHwyk9Lc8pNS6x197RU4LATnwBWJcCxhiJe"
    }

response = requests.request("GET", url, headers=headers, params=querystring)
response_json = response.json();

stocks = response_json['quoteResponse']['result']

data_to_get = ['symbol', 'longName', 'regularMarketPrice']
for s in stocks:
    for key in data_to_get:
        if(key in s):
            print(s[key], end = " / ")
            if(key == 'symbol'):
                input_stocks.remove(s[key].lower())
        else:
            print("NOT FOUND", end =" / ")
    print()
    
for i in input_stocks:
    print(i, " NOT FOUND IN API")
