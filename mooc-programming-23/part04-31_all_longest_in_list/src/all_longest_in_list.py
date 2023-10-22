# Write your solution here

def length_of_longest(lst):
    j = []
    for i in lst:
        j.append(len(i))
    return max(j)


def all_the_longest(lst):
    highest = length_of_longest(lst)
    k = []
    for i in lst:
        if len(i) == highest:
            k.append(i)
    return k