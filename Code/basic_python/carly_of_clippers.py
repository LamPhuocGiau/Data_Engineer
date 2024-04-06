hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]
print("Name of the cuts: " + str(hairstyles))
prices = [30, 25, 40, 20, 20, 35, 50, 35]
print("Prices: " + str(prices))
last_week = [2, 3, 5, 8, 4, 4, 6, 2]
print("Number of purchases in last week: " + str(last_week))
total_price = 0
for price in prices:
  total_price += price
print("Total price: ", total_price)
average_price = total_price / len(prices)
print ("Average haircut price: ",average_price)
new_prices = [price - 5 for price in prices]
print("New price cut-off 5: ", new_prices)
total_revenue = 0
for i in range(len(hairstyles)):
  total_revenue += prices[i] * last_week[i]
print ("Total revenue in last week: ", total_revenue)
average_daily_revenue = total_revenue / 7
print("Average daily revenue: ", average_daily_revenue)
cuts_under_30 = [hairstyles[i] for i in range(len(new_prices)) if new_prices[i] < 30]
print("Advertising for hairstyles under 30: " + str(cuts_under_30))

