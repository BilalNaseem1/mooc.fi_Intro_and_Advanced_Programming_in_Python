# Initialize the list
my_list = [1, 2, 3, 4, 5]

while True:
    # Ask the user for an index
    index = int(input("Index: "))
    
    # Check if the user wants to exit the loop
    if index == -1:
        break
    
    # Ask the user for a new value
    new_value = int(input("New value: "))
    
    # Replace the value at the given index
    my_list[index] = new_value
    
    # Print the updated list
    print(my_list)
