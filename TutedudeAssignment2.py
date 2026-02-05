
# To check the number entered by user is a odd or even number
Number=int(input("Enter any number :"))
if Number%2==0:
    print(Number,"is a even number")
else:
    print(Number," is a odd number")


# Python program to calculate the sum of integers from 1 to 50

# Initialize sum
total_sum = 0

# Iterate over numbers from 1 to 50
for num in range(1, 51):
    print(num)
    total_sum += num

# Display the final sum
print("The sum of integers from 1 to 50 is:", total_sum)