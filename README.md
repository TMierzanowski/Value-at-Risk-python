# Value-at-Risk-python

A quantitative risk management tool implemented in Python. It calculates **Value at Risk (VaR)** for financial assets using parametric (Variance-Covariance) and historical methods.

## Features
* **Asset selection by the user:** Data retrieved from stooq.pl.
* **Log Returns Analysis:** Uses logarithmic returns for additivity and statistical properties.
* **Dual VaR Methodology:**
    * *Parametric VaR:* Assumes Normal Distribution ($\mu, \sigma^2$).
    * *Historical VaR:* Based on empirical quantiles.

## Mathematical Models

### 1. Log Returns
$$return_t = \ln\left(\frac{P_t}{P_{t-1}}\right)$$

### 2. Parametric VaR (Normal Distribution)
$$VaR_{\alpha} = \mu - \sigma \cdot Z_{\alpha}$$

Where $Z_{\alpha}$ is the quantile of the normal distribution for confidence level $\alpha$.

### 3. Historical VaR
$$VaR_{\alpha} = \text{Quantile}(returns, 1-\alpha)$$

### 4. Results
Results are presented in a positive value multiplied by the value of portfolio (100 000).
## How to Run

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
2. Run the computation:
   ```bash
   python main.py
3. Inputting Data

- **Ticker format:** `xxx.aa`  
  - `xxx` → ticker symbol  
  - `aa` → country code (e.g., `us`, `de`, `pl`)

  - **Examples:**  
    - `nvda.us`  
    - `pkn.pl`

- **Date format:** 'dd-mm-YYYY'
  -  **Example:** 01-07-2025
