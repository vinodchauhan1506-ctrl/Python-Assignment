
# To check the number entered by user is a odd or even number
Number=int(input("Enter any number :"))
if Number%2==0:
    print(Number,"is a even number")
else:
    print(Number," is a odd number")

# To print a range 1 to 50 with the help of forloop and also get total of range

for i in range (1,51):
    print(i)
print("The sum of range (1,51) is :",sum(range(1,51)))