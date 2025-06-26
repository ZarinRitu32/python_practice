#1. largest number
'''
a = float(input("Enter the 1st one:"))
b = float(input("Enter the 2nd one:"))
c = float(input("Enter the 3rd one:"))
if a>b and a>c:
    print("a is the largest")

elif b>a and b>c:
    print("b is the largest")

else:
    print("c is the largest")    
'''
#2. user input of 3 frnd's cgpa , find out the lowest frnd and avg their cgpa

f1 = input("Enter the name of 1st friend:")
f2 = input("Enter the name of 2nd friend:")
f3 = input("Enter the name of 3rd friend:")

cg1 = float(input(f"Enter the cgpa of {f1}:")) # using placeholder
cg2 = float(input(f"Enter the cgpa of {f2}:"))
cg3 = float(input(f"Enter the cgpa of {f3}:"))

if cg1<cg2 and cg1<cg3:
    print(f"{f1} has the lowest cgpa and his cgpa is {cg1}")

elif cg2<cg1 and cg2<cg3:
      print(f"{f2} has the lowest cgpa and his cgpa is {cg2}")

else:
      print(f"{f3} has the lowest cgpa and his cgpa is {cg3}")


avg = (cg1 + cg2 + cg3)/3
print(avg)


