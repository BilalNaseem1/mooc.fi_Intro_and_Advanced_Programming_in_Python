# Write your solution here
hwage = float(input("Hourly wage:"))
hwork = float(input("Hours worked::"))
day = input("Day of the week:")

if day == "Sunday":
    print(f"Daily wages: {2 * hwage * hwork} euros")
else:
    print(f"Daily wages: {hwage * hwork} euros")