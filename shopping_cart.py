customer_name = input("Enter customer name: ")
item=[]
for i in range(3):
    while True:
        item_name = input("Enter item name: ")
        
        if len(item_name) > 0:
            break
        else:
            print("Invalid item name! Please enter a valid item name.")

    while True:
        try:
            item_price = float(input("Enter item price: "))
           
            if item_price > 0:
                break
            else:
                print("Invalid item price! Please enter a positive number.")
        except ValueError:
            print("Invalid input! Please enter a valid number.")
    item.append({"name": item_name, "price": item_price})

subtotal=0
for i in range(3):
    subtotal += item[i]["price"]

if subtotal >= 5000:
    discount = subtotal * 0.2
elif subtotal < 5000:
    discount = subtotal * 0.1
elif subtotal < 3000:
    discount = subtotal * 0.05
else:
    discount = 0

total_price = subtotal - discount
print(f"\nCustomer Name: {customer_name}\n")
for i in range(3):
    item_name = item[i]["name"]
    item_price = item[i]["price"]   
    print(f"Product {i+1}: {item_name}")
    print(f"Price: {item_price:.2f}\n")

print(f"Subtotal: {subtotal:.2f}")
print(f"Discount: {discount:.2f}")
print(f"Final Total: {total_price:.2f}")
