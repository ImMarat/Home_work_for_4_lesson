import requests
from decimal import Decimal
from datetime import datetime

def currency_rates(valute_name):
    response = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')
    data = response.text

    valute_index = data.find(valute_name)
    if valute_index:
        return (Decimal(data[valute_index:(valute_index + data[valute_index:].find('</Value'))].split('<Value>')[-1].replace(',', '.')),
                response.headers['Date'])
    else:
        return None











