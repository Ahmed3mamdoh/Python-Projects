"""
Create a python function that takes 2 numbers x, y and prints the multiplication table from x to y
"""
def mult_from_x_to_y(x,y):
    for i in range (x,y+1):
        print (f"Multiplication table for {i}")
        for j in range (1,13):
            result = i * j
            print(f"{i} * {j} = {result}")
            print()
try:
    x = int(input("Enter the first number: "))
    y = int(input("Enter the secound number: "))
except ValueError:
    print("Invalid input. Please enter valid integers for x and y.")
else:
    mult_from_x_to_y(x,y)