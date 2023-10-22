# Write your solution here

gift = int(input("Value of gift: "))

if gift in range(5000, 25001):
    lt = 100
    print(f"Amount of tax: {lt +(gift - 5000) * 0.08}")
elif gift in range(25001, 55001):
    lt = 1700
    print(f"Amount of tax: {lt +(gift - 25000) * 0.1}")
elif gift in range(55001, 200001):
    lt = 4700
    print(f"Amount of tax: {lt +(gift - 55000) * 0.12}")
elif gift in range(200001, 1000001):
    lt = 22100
    print(f"Amount of tax: {lt +(gift - 200000) * 0.15}")
elif gift >= 1000001:
    lt = 142100
    print(f"Amount of tax: {lt +(gift - 1000000) * 0.17}")
else:
    lt = 0
    print(f"No tax!")
