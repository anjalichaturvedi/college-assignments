'''Calculate the splitting of the bill while taking input of price and quantity'''

def calculate_bill(menu, quantities, prices):
    total_bill = 0
    for i in range(len(menu)):
        total_bill += quantities[i] * prices[i]
    return total_bill

def split_bill(total_bill, num_friends):
    if num_friends <= 0:
        return "Invalid number of friends. Please enter a positive number."

    per_person_share = total_bill / num_friends
    return per_person_share

def main():
    num_items = int(input("Enter the number of items in the menu: "))
    menu = []
    quantities = []
    prices = []

    for i in range(num_items):
        item = input(f"Enter name for Item {i + 1}: ")
        quantity = int(input(f"Enter quantity for {item}: "))
        price = float(input(f"Enter price for {item}: ₹"))
        menu.append(item)
        quantities.append(quantity)
        prices.append(price)

    total_bill = calculate_bill(menu, quantities, prices)

    num_friends = int(input("Enter the number of friends: "))

    per_person_share = split_bill(total_bill, num_friends)

    print("\n--- Bill Summary ---")
    print(f"Total Bill: ₹{total_bill:.2f}")
    
    if num_friends > 0:
        print(f"Each person pays: ₹{per_person_share:.2f}")
    else:
        print("Invalid number of friends. Cannot split the bill.")

main()