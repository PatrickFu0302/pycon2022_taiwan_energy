import pandas as pd
import numpy as np
import datetime
import requests
import os
import urllib

path_data = r'C:\Users\patri\Taipower\data\forecast'
date = datetime.datetime.now().strftime('%Y%m%d')

url_weekly_load = 'https://www.taipower.com.tw/d006/loadGraph/loadGraph/data/reserve_forecast.txt'
weekly_load_pred = pd.read_csv(url_weekly_load, encoding='big5',header=None)
weekly_load_pred = weekly_load_pred.dropna()
weekly_load_pred.to_csv(os.path.join(path_data, date+'_weekly_load_pred.csv'), encoding='utf8', index=False)

url_monthly_load = 'https://www.taipower.com.tw/d006/loadGraph/loadGraph/data/reserve_forecast_month.txt'
monthly_load_pred = pd.read_csv(url_monthly_load,header=None)
monthly_load_pred = monthly_load_pred.dropna()
monthly_load_pred.to_csv(os.path.join(path_data, date+'_monthly_load_pred.csv'), encoding='utf8', index=False)

url_weather = 'https://www.cwb.gov.tw/V8/C/W/County/MOD/wf7dayNC_NCSEI/ALL_Week.html'
r = requests.get(url_weather)
weatehr_pred = pd.read_html(r.text)[0]
weatehr_pred.columns = weatehr_pred.columns.str.split('星期',expand=True).get_level_values(0)
weatehr_pred = weatehr_pred.melt(id_vars=['縣市', '時間'], var_name='Date')
weatehr_pred['Date'] = pd.to_datetime(str(datetime.datetime.now().year)+'/'+weatehr_pred['Date'])
weatehr_pred['Temperature_low'] = weatehr_pred['value'].str.split(' |-',expand=True).iloc[:, 0].astype('float')
weatehr_pred['Temperature_high'] = weatehr_pred['value'].str.split(' |-',expand=True).iloc[:, 1].astype('float')
weatehr_pred = weatehr_pred.drop('value',axis=1)
weatehr_pred.to_csv(os.path.join(path_data, date+'_daily_weather_pred.csv'), encoding='utf8', index=False)

url_weather_zip = 'https://opendata.cwb.gov.tw/fileapi/v1/opendataapi/F-D0047-093?Authorization=rdec-key-123-45678-011121314&format=ZIP'
urllib.request.urlretrieve(url_weather_zip, os.path.join(path_data, date+'_weather.zip'))
