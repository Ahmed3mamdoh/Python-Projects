"""
Create a python function that takes 2 numbers x,y and prints 2 lists containing the odd and even numbers in
the x,y range.
"""


def odd_even_lists(x, y):
    odd_numbers = []
    even_numbers = []

    for num in range(x, y + 1):
        if num % 2 == 0:
            even_numbers.append(num)
        else:
            odd_numbers.append(num)

    return odd_numbers, even_numbers

x = int(input("Enter the first number in the range (x): "))
y = int(input("Enter the last number in the range (y): "))

odd_list, even_list = odd_even_lists(x, y)

print("Odd Numbers:", odd_list)
print("Even Numbers:", even_list)
