# Write your solution here

def formatted(lst):
    st = []
    for i in lst:
        j = format(round(i, 2), ".2f")
        j = str(j)
        st.append(j)
    return st
