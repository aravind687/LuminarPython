type=int(input("1.Cotton\n2.Silk\n3.Linen\nselect type of cloth:"))
amount=int(input("Enter purchase amount:"))
if(type==1):
    if(amount>20000):
        discount=amount*(10/100)
    elif((amount>15000)&(amount<=20000)):
        discount=amount*(9/100)
    elif((amount>14000)&(amount<=15000)):
        discount=amount*(7/100)
    else:
        discount=amount*(2/100)
elif(type==2):
    if(amount>20000):
        discount=amount*(15/100)
    elif((amount>15000)&(amount<=20000)):
        discount=amount*(10/100)
    elif((amount>14000)&(amount<=15000)):
        discount=amount*(9/100)
    else:
        discount=amount*(5/100)
else:
    if(amount>20000):
        discount=amount*(15/100)
    elif((amount>15000)&(amount<=20000)):
        discount=amount*(10/100)
    elif((amount>14000)&(amount<=15000)):
        discount=amount*(9/100)
    else:
        discount=amount*(5/100)

print("Purchase Amount is Rs",amount)
print("Amount after discount is Rs",int(discount))
