# QuantFinance

# Stock Price Analysis

This project analyzes historical stock prices using Python and the `yfinance` library. It calculates basic metrics such as mean, median, and standard deviation for stock closing prices and visualizes trends with Matplotlib.

## Features
- Fetch historical stock data with `yfinance`.
- Calculate key metrics (mean, median, standard deviation) using the closing price.
- Visualize closing prices and trends.

## Data Used
- Ticker: `AAPL` (Apple Inc.)
- Metrics:
  - **Mean Closing Price**: 150.34
  - **Median Closing Price**: 148.50
  - **Standard Deviation**: 12.45
 



### Short-Term (100 Bets)
- Some bettors make significant profits due to luck.
- Randomness plays a big role, and results vary widely.
   ![Volatility Analysis](images/myplot100.png)

### Medium-Term (1,000 Bets)
- The number of winners decreases as luck starts to balance out.
- The average outcome trends towards a loss due to the house edge.
  ![Final Outcome Distribution](images/final_outcomes.png)

### Long-Term (100,000 Bets)
- Almost all bettors lose money, as the house edge dominates.
- Only a very small number of bettors remain in profit, and even they barely break even.
