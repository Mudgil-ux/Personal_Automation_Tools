name = input("Hi! I am Wall-E. What's your name? ")
available_items = {
    "Apple": 40, "Banana": 20, "Milk": 55, 
    "Bread": 35, "Eggs": 80, "Chocolate": 100
}

cart = []
print(f"\nWelcome {name}! Type 'done' to finish shopping.\nAvailable: {', '.join(available_items.keys())}")

while True:
    add = input("Add item to cart: ").capitalize()
    if add == "Done":
        break
    if add in available_items:
        cart.append(add)
        print(f"Added {add}!")
    else:
        print(f"Sorry! {add} is not in stock.")

total = sum(available_items[item] for item in cart)

print("\n" + "="*30)
print(f"{name.upper()}'S FINAL BILL")
print("="*30)
for item in set(cart):
    count = cart.count(item)
    print(f"{item} x{count} - Rs. {available_items[item] * count}")
print("-" * 30)
print(f"TOTAL AMOUNT: Rs. {total}")
print("="*30)
