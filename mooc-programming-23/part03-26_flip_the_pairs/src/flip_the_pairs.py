# Write your solution here
num = int(input("Please type in a number:"))
j = 0
x = []

for i in range(1, num+1):
    j+=1
    if j%2==0:
        print(i)
        x.append(i)
        print(i-1)
        x.append(i-1)
    
if num not in x:
    print(num)