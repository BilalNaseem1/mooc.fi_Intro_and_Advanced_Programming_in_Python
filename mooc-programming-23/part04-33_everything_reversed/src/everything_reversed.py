# Write your solution here

def item_reverse(lst):
    n = []
    for i in lst:
        i = i[::-1]
        n.append(i)
    return n

def everything_reversed(lst):
    lst = item_reverse(lst)
    lst = lst[::-1]
    return lst


if __name__ == "__main__":
    k = everything_reversed(["abc", "yahoo"])
    print(k)

