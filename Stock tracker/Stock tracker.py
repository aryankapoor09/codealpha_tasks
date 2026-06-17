stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "AMZN": 130,
    "MSFT": 320
}
total_investment = 0
investment_details = []
n = int(input("How many stocks do you want to add? "))
for i in range(n):
    stock_name = input("\nEnter stock name: ").upper()
    quantity = int(input("Enter quantity: "))
    if stock_name in stock_prices:
        price = stock_prices[stock_name]
        investment = price * quantity
        total_investment += investment

        investment_details.append(
            f"{stock_name} - Quantity: {quantity}, "
            f"Price: ${price}, Total: ${investment}"
        )
        print(f"Added {stock_name} investment: ${investment}")
    else:
        print("Stock not found!")
print("\n--- Investment Summary ---")
for detail in investment_details:
    print(detail)
print(f"\nTotal Investment Value: ${total_investment}")
save = input("\nDo you want to save the result to a file? (yes/no): ").lower()
if save == "yes":
    with open("investment_summary.txt", "w") as file:
        file.write("--- Investment Summary ---\n")

        for detail in investment_details:
            file.write(detail + "\n")

        file.write(f"\nTotal Investment Value: ${total_investment}")

    print("Results saved to investment_summary.txt")
