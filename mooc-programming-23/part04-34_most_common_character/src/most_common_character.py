# Write your solution here

def most_common_character(string):
    lst = list(string)
    lst2 = []
    for i in lst:
        cnt  = lst.count(i)
        lst2.append(cnt)
    for i in lst:
        if lst.count(i) == max(lst2):
            break
    return i





if __name__ == "__main__":
    k = most_common_character("abcaa")
    print(k)