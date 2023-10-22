# Write your solution here

temp = int(input("Please type in a temperature (F):"))

temp_cel = ((temp - 32) * 5)/9

if temp_cel <0:
    print(f"{temp} degrees Fahrenheit equals {temp_cel} degrees Celsius\nBrr! It's cold in here!")
else:
    print(f"{temp} degrees Fahrenheit equals {temp_cel} degrees Celsius")