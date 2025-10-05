import csv

stock_prices = {
    "AAPL": 254.63,
    "TSLA": 444.72,
    "GOOGL": 243.10,
    "MSFT": 517.95,
    "AMZN": 219.57
}

portfolio = {}
total = 0

print("-"*60)
print("Welcome to Stock Portfolio Tracker")
print("Available Stocks:", ", ".join(stock_prices.keys()))
print("-"*60)

while True:

    stock = input("Enter stock symbol (or type 'done' to finish):").upper()

    if stock == "DONE":
     break
    if stock not in stock_prices:
        print("Stock not found! Choose from:", ", ".join(stock_prices.keys()))
        continue

    quantity = int(input("Enter the quantity of stock: "+ stock + ": "))    

    if stock in portfolio:
       
       portfolio[stock] += quantity
    else:
       portfolio[stock] = quantity

    print(quantity, "shares of", stock, "added")   

print("-"*40)
print("YOUR PORTFOLIO SUMMARY")
print("-"*40)

for stock in  portfolio:
   quantity = portfolio[stock]
   price = stock_prices[stock]
   value = quantity * price

   print(stock,":", quantity, "shares | value =", value)
   
   total += value

print("-"*40)
print("The total is:" ,total)
print("-"*40)

with open("Portfolio_Summary.csv", "w", newline="") as file:
   writer = csv.writer(file)
   writer.writerow(["Stock", "Quantity", "Value"])

   for stock in portfolio:
      quantity = portfolio[stock]
      price = stock_prices[stock]
      value = quantity * price
      writer.writerow([stock, quantity, value])

   writer.writerow([])
   writer.writerow(["Total", "", total])
