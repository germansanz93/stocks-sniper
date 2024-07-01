import os

import requests
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv('API_KEY')


def call_search(uri):
    with requests.Session() as s:
        resp = s.get(uri)
        container = resp.json()
        return container


def call_get(uri):
    headers = {
        'apikey': api_key,
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/100.0.4896.127 Safari/537.36'
    }

    payload = {
        'premiumNum': '100',
        'freeNum': '25',
        'languageId': 'en',
        'locale': 'en',
        'clientId': 'MDC',
        'benchmarkId': 'mstarorcat',
        'component': 'sal-components-mip-holdings',
        'version': '3.59.1'
    }

    with requests.Session() as s:
        s.headers.update(headers)
        resp = s.get(uri, params=payload)
        return resp.json()

def search_ticker(search):
    search_uri = f'https://www.morningstar.com/api/v2/search?query={search}'
    return call_get(search_uri)['components']['usSecurities']['payload']['results']

def call_morningstar_stock_id(exchange, ticker):
    stock_id_uri = f'https://www.morningstar.com/api/v2/stocks/{exchange}/{ticker}/quote'
    return call_get(stock_id_uri)


def call_morningstar_valuation(stock_code):
    valuation_uri = (
        f'https://api-global.morningstar.com/sal-service/v1/stock/valuation/v3/{stock_code}?languageId=en&locale=en'
        '&clientId=MDC&component=sal-valuation&version=4.30.0')
    return call_get(valuation_uri)
