from requests import Request, Session
import json
import datetime
import tkinter as tk
from tkinter import Canvas

url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
parameters = {
  'start':'1',
  'limit':'40',
  'convert':'USD'
}
headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': 'YOUR_KEY',
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
  #Affichage lignes de commande
  refresh(name, symbol, price, percent_change_24h, percent_change_7d)
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

  #Affichage graphique
  root = tk.Tk()
  root.title('Wallet')
  
  for i in range(len(name)):
    tk.Label(root, text=symbol[i], fg='#653FE2').grid(row=i, column=0)
    tk.Label(root, text=price[i]).grid(row=i, column=1)
    if percent_change_24h[i] < 0.00:
      tk.Label(root, text=percent_change_24h[i], fg='#FF0011').grid(row=i, column=2)
    else:
      tk.Label(root, text=percent_change_24h[i], fg='#12B600').grid(row=i, column=2)
    if percent_change_7d[i] < 0.00:
      tk.Label(root, text=percent_change_7d[i], fg='#FF0011').grid(row=i, column=3)
    else:
      tk.Label(root, text=percent_change_7d[i], fg='#12B600').grid(row=i, column=3)
  

  root.resizable(False, False)
  root.mainloop()
