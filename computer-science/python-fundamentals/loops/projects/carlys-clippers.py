# Starting code.
hairstyles = [
    "bouffant",
    "pixie",
    "dreadlocks",
    "crew",
    "bowl",
    "bob",
    "mohawk",
    "flattop",
]

prices = [30, 25, 40, 20, 20, 35, 50, 35]

last_week = [2, 3, 5, 8, 4, 4, 6, 2]

# Iteration 1.
total_price = 0

# Iteration 2.
for price in prices:
    total_price += price

# Iteration 3.
average_price = total_price / len(prices)

# Iteration 4.
print("Average Haircut Price: " + str(average_price))

# Iteration 5 and 6.
new_prices = [price - 5 for price in prices]
print(new_prices)

# Iteration 7, 8, and 9.
total_revenue = 0

for i in range(len(hairstyles)):
    total_revenue += prices[i] * last_week[i]

# Iteration 10.
print("Total Revenue: " + str(total_revenue))

# Iteration 11.
average_daily_revenue = total_revenue / 7
print(average_daily_revenue)

# Iteration 12.
cuts_under_30 = [price for price in prices if price < 30]
print(cuts_under_30)
