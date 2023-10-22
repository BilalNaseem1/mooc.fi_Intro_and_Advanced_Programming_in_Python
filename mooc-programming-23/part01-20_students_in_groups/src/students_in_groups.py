# Write your solution here
students = int(input("How many students on the course?"))
g_size = int(input("Desired group size?"))

num_groups = students / g_size

if num_groups%2 == 0:
    print(f"Number of groups formed: {num_groups}")
else:
    print(f"Number of groups formed: {(students // g_size) + 1}")