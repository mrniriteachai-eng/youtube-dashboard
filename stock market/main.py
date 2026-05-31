
# Stock Market Portfolio Simulator & Visualizer majale 

# Step 1: Simulated (Dummy) Data Ready Garne

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# 1. Date range ready garne (10 din ko lagi)
dates = pd.date_range(start="2026-05-01", periods=10)

# 2. NumPy use garera continuous dummy stock prices generate garne
# Hami sochum Apple ko suruko price $150, Google ko $2800, Bitcoin ko $60000 thiyo
apple_prices = [150, 152, 151, 155, 154, 158, 157, 160, 162, 165]
google_prices = [2800, 2810, 2795, 2820, 2830, 2815, 2840, 2860, 2850, 2880]
bitcoin_prices = [60000, 61000, 59500, 62000, 61500, 63000, 62500, 64000, 63800, 65000]

# 3. Pandas DataFrame (Table) ready garne
data = {
    'Apple': apple_prices,
    'Google': google_prices,
    'Bitcoin': bitcoin_prices
}
df = pd.DataFrame(data, index=dates)

print("--- Hami le banayeko Stock Price Table ---")
print(df)



# Step 2: Pandas use garera Daily Return calculate garne




# .pct_change() le hijo ko price sanga aaja ko price compare garera return nikalcha
daily_returns = df.pct_change()

# Suruko din ko return NaN (Null) hunchha kina ki tyo vanda agadi data chaina, tyo row lai delete garne
daily_returns = daily_returns.dropna()

print("\n--- Daily Percentage Change Table ---")
print(daily_returns)

# daily_returns= aajako price - hijo ko price / hijoko price

# for example 
# 151-150 / 150 = 0.01333(baneko 1.33% profit)



# Step 3: Portfolio Calculation (NumPy Weight Multiplier)




# Weights assign garne (Total add garda 1.0 or 100% huna parcha)
weights = np.array([0.4, 0.3, 0.3])

# Hami continuous single day portfolio return matrix nikalna column-wise multiply garchham
portfolio_daily_return = daily_returns.dot(weights)

# Dot Product Line (Matrix Multiplication)

# Dynamic Cumulative (Total sequential multiplication) return track garna formula lagau:

portfolio_cumulative_return = (1 + portfolio_daily_return).cumprod() - 1

# Kina lekheko?: Single single din ko daily return thahapaunu euta kura ho, tara hami lai main asset tracker maa k chahinchha? "Maile Day 1 maa lagako total Rs 100, aaja Day 10 block ma pugda total keti percent le badhyo?" Yeslai hami compounding or Cumulative Return vanchham.K kasari kaam garchha?: Python ko .cumprod() vaneko Cumulative Product ho. Yesle numbers lai multiply gardai compound interest jastai calculate garchha.1 + portfolio_daily_return: Suru maa 1 jodnu ko karan matrix percent values lai mathematical base structure dinu ho (e.g., $1 + 0.01 = 1.01$)..cumprod(): Yesle Day 1 ko return, Day 2 ko return sanga line cross multiply gardai sequential total wealth progression update track garchha.

print("\n--- Portfolio Cumulative Return Matrix (Total Profit/Loss Trend) ---")
print(portfolio_cumulative_return)


# Kina lekheko?: Stock market maa hami le sabaikhura maa barabar paisa haldainau. Sochum hami  sanga total $100$ Rupees thiyo. 
# Tapai le:40% ($40$ Rs) Apple maa halem 
#  0.430% ($30$ Rs) Google maa halem
# 0.330% ($30$ Rs) Bitcoin maa halem
# 0.3K kasari kaam garchha?:
#  Hami le NumPy use garera normal python list lai np.array() maa convert garyom, jasle garda mathematical calculations (Matrix Multiplication) garna computer lai ekdum fast safe ra easy hunchha.



# Step 4: Matplotlib use garera dashboard visuals display garne




# Figure structural size setup
plt.figure(figsize=(10, 5))

# Plotting individual line chart line
plt.plot(portfolio_cumulative_return, marker='o', color='purple', label='Mero Total Portfolio Return')

# Graph layout parameters optimization
plt.title('Stock Portfolio Growth Over 10 Days Tracking Line')
plt.xlabel('Dates')
plt.ylabel('Cumulative Profit Percentage')
plt.grid(True)
plt.legend()

# Graph terminal visualization trigger command
plt.show()