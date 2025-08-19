# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 2700,
    "AMZN": 3300,
    "MSFT": 300
}

# Dictionary to store user portfolio
portfolio = {}

print("Enter your stock holdings. Type 'done' when finished.")

# Input loop
while True:
    stock = input("Enter stock symbol (e.g., AAPL): ").upper()
    if stock == 'DONE':
        break
    if stock not in stock_prices:
        print("Stock not found in the price list. Try again.")
        continue
    try:
        quantity = int(input(f"Enter quantity of {stock}: "))
        portfolio[stock] = portfolio.get(stock, 0) + quantity
    except ValueError:
        print("Please enter a valid number.")

# Calculate total investment
total_investment = 0
print("\nYour Portfolio:")
for stock, qty in portfolio.items():
    price = stock_prices[stock]
    value = price * qty
    total_investment += value
    print(f"{stock}: {qty} shares × ${price} = ${value}")

print(f"\nTotal Investment Value: ${total_investment}")

# Optional file save
save = input("Would you like to save this summary to a file? (yes/no): ").lower()
if save == 'yes':
    filename = input("Enter filename (with .txt or .csv extension): ")
    with open(filename, 'w') as f:
        f.write("Stock,Quantity,Price,Value\n")
        for stock, qty in portfolio.items():
            price = stock_prices[stock]
            value = price * qty
            f.write(f"{stock},{qty},{price},{value}\n")
        f.write(f"\nTotal Investment Value: ${total_investment}")
    print(f"Portfolio saved to '{filename}'.")

