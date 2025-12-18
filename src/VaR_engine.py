import pandas as pd
import numpy as np
from datetime import datetime
from scipy.stats import norm

class VaR_engine():

  def __init__(self):
    self.data = pd.DataFrame()
    self.returns = pd.Series()
  
  def download_prices(self):
    #User input: ticker and date range
    self.ticker = input('Ticker: ')
    self.start = input('Start date: ')
    self.end = input('End date: ')
    
    #date type modification to use in url
    self.start_mod = datetime.strptime(self.start, '%d-%m-%Y').strftime('%Y%m%d')
    self.end_mod = datetime.strptime(self.end, '%d-%m-%Y').strftime('%Y%m%d')

    url = f"https://stooq.pl/q/d/l/?s={self.ticker}&d1={self.start_mod}&d2={self.end_mod}&i=d"

    #downloading stock prices
    self.data = pd.read_csv(url)

  #log-returns calculation
  def calculate_returns(self):
    prices = self.data['Zamkniecie']
    self.returns = np.log(prices/prices.shift(1)).dropna()
  
  #parametric VaR calculation
  def parametric_var(self, conf_level):
    mu = np.mean(self.returns)
    sigma = np.std(self.returns)
    z_score = norm.ppf(conf_level)

    return mu - z_score*sigma

  #historical VaR calculation
  def historical_var(self, conf_level):
    return np.quantile(self.returns, 1-conf_level)
