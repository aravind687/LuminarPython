num1=int(input("Enter mark of first subject"))
num2=int(input("Enter mark of second subject"))
num3=int(input("Enter mark of third subject"))
total=num1+num2+num3
print("total=",total)
if(total>145):
    print("grade is A+")
elif((total>140)&(total<=145)):
    print("grade is A")
elif((total>135)&(total<=140)):
    print("grade is B+")
elif((total>130)&(total<=135)):
    print("grade is B")
elif(total<= 30):
    print("failed")
















