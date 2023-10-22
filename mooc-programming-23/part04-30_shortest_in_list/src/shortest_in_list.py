# Write your solution here

def shortest(lst):
    j = []
    for i in lst:
        j.append(len(i))
    m = []
    for i in lst:
        if len(i) == min(j):
            m.append(i)
        else:
            pass
    return m[0]

