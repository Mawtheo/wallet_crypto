from requests import Request, Session
import json
import datetime

url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
parameters = {
  'start':'1',
  'limit':'20',
  'convert':'USD'
}
headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': 'c081e4fd-22a2-44bc-b37d-af50780595ef',
}

name = []
symbol = []
price = []
percent_change_24h = []
percent_change_7d = []

def refresh(name, symbol, price, percent_change_24h, percent_change_7d):
    session = Session()
    session.headers.update(headers)
    response = session.get(url, params=parameters).json()
    date = str(datetime.datetime.now())
    print('Dernière update:', date[0:10], 'à:', date[11:16], '\n')

    for i in range(len(response['data'])):
        name.append(response['data'][i]['name'])
        symbol.append(response['data'][i]['symbol'])
        price.append(round(response['data'][i]['quote']['USD']['price'], 2))
        percent_change_24h.append(round(response['data'][i]['quote']['USD']['percent_change_24h'], 2))
        percent_change_7d.append(round(response['data'][i]['quote']['USD']['percent_change_7d'], 2))
        #print(response['data'][i], '\n')
    
    return name, symbol, price, percent_change_24h, percent_change_7d

if __name__ == "__main__":
  refresh(name, symbol, price, percent_change_24h, percent_change_7d)
  for i in range(len(name)):
     print(symbol[i], name[i], price[i], 'USD /24h:', percent_change_24h[i], '/7d:', percent_change_7d[i])
