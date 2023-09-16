"""
Create a python function that takes 2 numbers x,y and prints all the numbers between 1 and 100 than can
be divided on x,y
"""
def divisible_by_x_and_y(x, y):
    print(f"All Numbers between 1 and 100 divisible by both {x} and {y}:")
    for number in range(1, 101):
        if number % x == 0 and number % y == 0:
            print(number)
            
x = int(input("Enter the value of x: "))
y = int(input("Enter the value of y: "))
divisible_by_x_and_y(x, y)