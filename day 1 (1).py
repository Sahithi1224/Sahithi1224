
#Cost_of_loaves
r1=185.00
r2=r1-(0.6*r1)
try:
    n1=int(input("Enter the no of fresh loaves: "))
    n2=int(input("Enter the no of day old loaves: "))
    if((n1>=0)&(n2>=0)):
        a1=n1*r1
        a2=n2*r2
        total=a1+a2
        print("Regular price",r1)
        print("Discount price",r2)
        print("Price of fresh loaves = ",a1)
        print("Price of day old loaves = ",a2)
        print("Total Price = ",total)
    else:
        print("Enter a positive number")
except ValueError:
    print("Enter the input as whole number")
