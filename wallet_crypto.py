from requests import Session
import json
import datetime
import time

url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
parameters = {
  'start':'1',
  'limit':'40',
  'convert':'USD'
}
headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': 'YOUR_API_KEY',
}

date = str(datetime.datetime.now())
name = []
symbol = []
price = []
percent_change_24h = []
percent_change_7d = []

def refresh(name, symbol, price, percent_change_24h, percent_change_7d, date):
    session = Session()
    session.headers.update(headers)
    response = session.get(url, params=parameters).json()
    print('Dernière update:', date[0:10], 'à:', date[11:16], '\n')

    for i in range(len(response['data'])):
        name.append(response['data'][i]['name'])
        symbol.append(response['data'][i]['symbol'])
        price.append(round(response['data'][i]['quote']['USD']['price'], 2))
        percent_change_24h.append(round(response['data'][i]['quote']['USD']['percent_change_24h'], 2))
        percent_change_7d.append(round(response['data'][i]['quote']['USD']['percent_change_7d'], 2))
        #print(response['data'][i], '\n')
    
    return name, symbol, price, percent_change_24h, percent_change_7d

#Affichage lignes de commande
if __name__ == "__main__":
  refresh(name, symbol, price, percent_change_24h, percent_change_7d, date)
  for i in range(len(name)):
      if percent_change_24h[i] < 0.00:
        if percent_change_7d[i] < 0.00:
          print('\033[95m', symbol[i], '\033[0m', price[i], 'USD /24h:', '\033[91m', percent_change_24h[i], '\033[0m', '%', '/7d:', '\033[91m', percent_change_7d[i], '\033[0m', '%')
        else:
            print('\033[95m', symbol[i], '\033[0m', price[i], 'USD /24h:', '\033[91m', percent_change_24h[i], '\033[0m', '%', '/7d:', '\033[92m', percent_change_7d[i], '\033[0m', '%')
      else:
        if percent_change_7d[i] < 0.00:
          print('\033[95m', symbol[i], '\033[0m', price[i], 'USD /24h:', '\033[92m', percent_change_24h[i], '\033[0m', '%', '/7d:', '\033[91m', percent_change_7d[i], '\033[0m', '%')
        else:
            print('\033[95m', symbol[i], '\033[0m', price[i], 'USD /24h:', '\033[92m', percent_change_24h[i], '\033[0m', '%', '/7d:', '\033[92m', percent_change_7d[i], '\033[0m', '%')
  time.sleep(60)
 
