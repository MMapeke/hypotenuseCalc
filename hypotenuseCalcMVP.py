import math

print("Welcome to the best calc EVER!!!")
print("--------------------------------")
print("")




check = False
while check == False:
    a = input("Input one side length - ")
    try:
        a = float(a)
        check = True
    except ValueError:
       print("That's not an number!")
   
check2 = False
while check2 == False:
    b = input("Input the other side length - ")
    try:
       b = float(b)
       check2 = True
    except ValueError:
       print("That's not an number")
   
def find_hypotenuse(a,b):
    sum1 = a*a
    sum2 = b*b
    sum3 = sum1 + sum2
    c = math.sqrt(sum3)
    return round(c,2)
    
print("The hypotenuse is about - " + str(find_hypotenuse(a,b)))

