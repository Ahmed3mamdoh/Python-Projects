"""
Create a function that takes x,y and prints all the number that can be divided by y from x to 100
"""
def numbers_can_be_divided_by_y_from_x_to_100(x , y):
    if y== 0 :
        print ("Cannot divide by zero.")
        return
    if x > 100 :
        print (" the value X should be less than or equal to 100")
        return
    for numbers in range(x , 101):
        if numbers % y == 0:
            print(numbers)    
x = (int(input("Enter the X Value :")))
y = (int(input("Enter the Y Value :")))
print(f"All numbers that can be divided by {y} from {x} to 100 Are :")
numbers = numbers_can_be_divided_by_y_from_x_to_100(x , y)