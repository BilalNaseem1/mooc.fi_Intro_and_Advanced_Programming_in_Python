# Write your solution here

def sum_of_positives(lst):
    sum = 0
    for i in lst:
        if i>0:
            sum+=i
        else:
            pass
    return sum

if __name__ == "__main__":
    result = sum_of_positives([1, -2, 3, -4, 5])
    print(result)