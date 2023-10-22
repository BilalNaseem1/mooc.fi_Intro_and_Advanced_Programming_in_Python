# Write your solution here

num = int(input("Please type in a number:"))
x = []

k = 1
p=0
if num>0:
    for i in range(1, num+1):
        x.append(i)
    

    for j in range(0, len(x)):
        print(x[j])
        p +=1
        if p == num:
            break
        print(x[-k])
        p +=1
        k+=1
        if p == num:
            break


        
