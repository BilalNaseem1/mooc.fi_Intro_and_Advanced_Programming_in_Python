print("Please type in integer numbers. Type in 0 to finish.")
num = None
i = 0
sum_n =0
p_n =0
n_n = 0

while num !=0:
    num = int(input("Number: "))
    if num != 0:
        i +=1
    else:
        pass
    if num >0:
        p_n +=1
    elif num <0:
        n_n +=1
    else:
        pass
    if num == 0:
        print(f"Numbers typed in {i}")
        print(f"The sum of the numbers is {sum_n}")
        print(f"The mean of the numbers is {sum_n/i}")
        print(f"Positive numbers {p_n}")
        print(f"Negative numbers {n_n}")
        break
    else:
        sum_n += num
else:
    print(f"Numbers typed in {i}")
    print(f"The sum of the numbers is {sum_n}")
    print(f"The mean of the numbers is {sum_n/i}")
    print(f"Positive numbers {p_n}")
    print(f"Negative numbers {n_n}")