
#  lab 7 Self Assessment 

# 1. The first bug was that the total was being replaced
# instead of adding each sale. The correct fix was using
# the += operator. This helped me understand how important
# it is to check variables and how they change inside a loop.

# 2. The apply_discount(price, tier) function takes a price
# and a customer tier as inputs, then returns the price after
# applying the discount for that tier. Gold gets 15% off,
# silver gets 10% off, bronze gets 5% off, and other tiers
# get no discount. A colleague could use the function by
# providing a price and a tier

# 3. AI Disclosure: I used ChatGPT to simplify the lab
# instructions, review the code I had completed in class,
# and explain the debugging process so I could better
# understand the errors and how to fix them

# exersise 1

def calculate_tax(price, rate):
    return price * rate

#calling the function

tax1 = calculate_tax(100, 0.07)
tax2 = calculate_tax(250, 0.08)

print(f"Tax for $100 at 7%: ${tax1:.2f}")
print(f"Tax for $250 at 8%: ${tax2:.2f}")
print(f"Tax for $350 at 5%: ${calculate_tax(350, 0.05):.2f}")

# exercise 2

def apply_discount(price, tier):
    """Return the discounted price based on customer tier."""
    if tier == "gold":
        return price * 0.85      #15% off
    elif tier == "silver":
        return price * 0.90      #10% off
    elif tier == "bronze":
        return price * 0.95      #5% off
    else:
        return price             #0% off 

original_price = 200

for tier in ("gold", "silver", "bronze", "none"):
    print(f"{tier}: ${apply_discount(original_price, tier):.2f}")


# exercise 3

discounted_price = apply_discount(200, "gold")
print(f"After gold discount: ${discounted_price:.2f}")

tax = calculate_tax(discounted_price, 0.07)
print(f"After tax: ${discounted_price + tax:.2f}")

def final_price(price, discount_tier, tax_rate):
    discounted_price = apply_discount(price, discount_tier)
    tax = calculate_tax(discounted_price, tax_rate)
    return discounted_price + tax

print(f"final_price(200, 'gold', 0.07) = ${final_price(200, 'gold', 0.07):.2f}")

# exercise 4

orders = [(200, "gold"), (150, "silver"), (80, "bronze"), (500, "none")]
for price, tier in orders:
    total = final_price(price, tier, 0.07)
    print(f"Price: ${price} | Tier: {tier} | Total: ${total:.2f}")
print()



# exercise 5

# Bug 1: total = sale replaces the total each time
# Fix: Use += to add each sale to the running total
sales = [120, 80, 250, 175, 90]

total = 0
for sale in sales:
    total += sale
print(f"Total: ${total}")

# Bug 2: The for loop is missing a colon
# Fix: Add a colon at the end of the for statement
count = 0
for sale in sales:
    count += 1
print(f"Count: {count}")

# Bug 3: The condition allows i to reach len(sales)... which is outside the valid list indexes
# Fix: Use < instead of <=.
i = 0
while i < len(sales):
    print(sales[i])
    i += 1



# exercise 6


# A local variable only exists inside its function.
# The x inside double_it() is separate from the global x,
# so changing the local x does not change the global x

x = 100

def double_it():
    x = 999
    return x * 2

print(x)
print(double_it())
print(x)
