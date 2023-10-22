# Write your solution here

def length_of_longest(lst):
    j = []
    for i in lst:
        j.append(len(i))
    return max(j)
