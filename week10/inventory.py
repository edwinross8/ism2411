# inventory.py
# author -> Edwin Ross
# module 10 lab- inventory list manegement

# execise 1

print("--- Exercise 1: Build a list ---")

inventory = ("pen", "notebook", "stapler", "tape", "marker")
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

print(inventory)

inventory.remove("tape")
print(inventory)

inventory.sort()
print(inventory)







# reflection
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#