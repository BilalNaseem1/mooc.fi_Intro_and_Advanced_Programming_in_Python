# Write your solution here
s = 0
limit = int(input("Limit: "))
i=0
sent = ""

while s <limit:
    i+=1
    s +=i
    if s <limit:
        sent += str(i) + " + "
    else:
        sent += str(i) + " = "

print("The consecutive sum:", sent + str(s))