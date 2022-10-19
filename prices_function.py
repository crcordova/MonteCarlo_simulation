import pandas as pd
import requests
import datetime

def get_historic_data(from_sym='BTC', to_sym='USD', timeframe = 'day', limit=2000, aggregation=1, exchange=''):
    #timeframe = ['day', 'minute', 'hour']
    url = 'https://min-api.cryptocompare.com/data/v2/histo'
    url += timeframe
    
    parameters = {'fsym': from_sym,
                  'tsym': to_sym,
                  'limit': limit,
                  'aggregate': aggregation}
    if exchange:
        print('exchange: ', exchange)
        parameters['e'] = exchange    
    
    print('baseurl: ', url) 
    print('timeframe: ', timeframe)
    print('parameters: ', parameters)

    response = requests.get(url, params=parameters)   
    
    data = response.json()['Data']['Data'] 
    df = pd.DataFrame(data)
    df['time'] = df['time'].apply(lambda x: datetime.datetime.fromtimestamp(x))
    return df.set_index('time')