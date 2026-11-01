# -+-+REFLECT+-+-
#
# 1. Changing lists was surprisingly easy and commands
# like append, remove, and sort were pretty simple.
# I was expecting it to be a more complicated process.
#
# 2. Python lists could track inventory for a business
# a lot easier than manually updating a spreadsheet
# every time something sells. A Python program could
# also do calculations automatically.



# inventory.py
# author -> Edwin Ross
# module 10 lab- inventory list manegement

# execise 1

print("--- Exercise 1: Build a list ---")

inventory = ["pen", "notebook", "stapler", "tape", "marker"]
print(inventory)
print(len(inventory))
      
# exercise 2

print("--- Exercise 2: Index Practice ---")
print(inventory[0])
print(inventory[-1])

middle = len(inventory) // 2
print(inventory[middle])

# exercise 3

print("--- Exercise 3: Slicing ---")

print(inventory[:3])
print(inventory[-2:])
print(inventory[::2])



# exercise 4

print("--- Exercise 4: Modifying the List ---")

inventory.append("envelope")
print(inventory)

inventory.remove("tape")
print(inventory)

inventory.sort()
print(inventory)


# exercise 5

print("--- Exercise 5: Tuple Comparison ---")

coords = (40.7128, -74.0060)

try:
    coords[0] = 99
except TypeError:
    print("Tuples cannot be changed, which makes them useful for storing coordinates.")

print(coords)


# exercise 6

print("--- Exercise 6: Iterating Over the List ---")
sales = [100, 250, 75, 480, 200]
total = sum(sales)
count = len(sales)
average = total / count
print(f"Total sales: {total}")
print(f"Count: {count}")
print(f"Average sales: {average}")
print(f"Best sales: {max(sales)}")
print(f"Worst sales: {min(sales)}")


best = sales[0]
worst = sales[0]
for amount in sales:
    if amount > best:
        best = amount
    if amount < worst:
        worst = amount

print(f"Best sale (loop): {best}")
print(f"Worst sale (loop): {worst}")



# exercise 7

print("--- Exercise 7: Accumulator Pattern ---")

prices = [9.99, 14.99, 4.99, 24.99, 1.99]
discounted = []

for price in prices:
    new_price = round(price * 0.90, 2)
    discounted.append(new_price)

print("Original prices:", prices)
print("Discounted prices:", discounted)



# exercise 8

print("--- Exercise 8: Filter Above Threshold ---")

sales = [340, 127, 589, 204, 467, 88, 731, 315, 62, 490]
high_sales = []

for amount in sales:
    if amount > 300:
        high_sales.append(amount)

print("High sales:", high_sales)
print("Count:", len(high_sales))
print("Average:", round(sum(high_sales) / len(high_sales), 2))





