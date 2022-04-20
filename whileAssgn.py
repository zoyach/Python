<<<<<<< HEAD
total = 0
item_num = 0

while True:
    
    item_price = float(input(f"Enter the price of the item{item_num}: "))
    if item_price < 1:
        break
    item_num += 1

    total += item_price
print(f"The Total number of items are {item_num}")
print(f"The total is {total}")
if total > 5000 or item_num >= 10:
    Discount = (15/100)*total
print(f"Your Discount is {round(Discount,2)}")
Gst = (17/100)*total
print(f"GST is {round(Gst,2)}  ")
Payable = total-Discount-Gst
print(f"Payable Amount: {Payable}")
=======
total = 0
item_num = 0

while True:
    
    item_price = float(input(f"Enter the price of the item{item_num}: "))
    if item_price < 1:
        break
    item_num += 1

    total += item_price
print(f"The Total number of items are {item_num}")
print(f"The total is {total}")
if total > 5000 or item_num >= 10:
    Discount = (15/100)*total
print(f"Your Discount is {round(Discount,2)}")
Gst = (17/100)*total
print(f"GST is {round(Gst,2)}  ")
Payable = total-Discount-Gst
print(f"Payable Amount: {Payable}")
>>>>>>> 5d2e7ad726176708578271049fb1a9fbc8877240
