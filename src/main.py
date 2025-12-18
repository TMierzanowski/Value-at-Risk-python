from src.VaR_engine import VaR_engine

def main():
  conf_level = 0.95 #or = 0.99
  V = 100000 #value of porfolio

  stock = VaR_engine()
  stock.download_prices()
  stock.calculate_returns()
  par_var = stock.parametric_var(conf_level)
  hist_var = stock.historical_var(conf_level)

  print(f'---Value at Risk (VaR) calculation---')
  print(f'Ticker: {stock.ticker}')
  print(f'Period: {stock.start} - {stock.end}')
  print(f'\nAssuming capital {V} and confidence level {conf_level}')
  print(f'Parametric VaR: {-V*par_var}')
  print(f'Historical VaR: {-V*hist_var}')

if __name__ == "__main__":
  main()
