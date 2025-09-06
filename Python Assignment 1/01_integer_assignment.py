# INTEGER DATATYPE ASSIGNMENT
# ===========================

# SOLVED EXAMPLE
# --------------
# Question: Calculate the sum of first 5 even numbers
print("SOLVED EXAMPLE:")
print("Calculate the sum of first 5 even numbers")
first_5_even = [2, 4, 6, 8, 10]
sum_even = sum(first_5_even)
print(f"First 5 even numbers: {first_5_even}")
print(f"Sum: {sum_even}")
print("-" * 50)

# ASSIGNMENT QUESTIONS
# ===================

# Question 1: Calculate the product of first 10 natural numbers
print("Question 1: Calculate the product of first 10 natural numbers")
x=range(1,11)
product=1
for i in x:
  product*=i
print(product)

# Question 2: Find the remainder when 156 is divided by 7
print("\nQuestion 2: Find the remainder when 156 is divided by 7")
remainder=156%7
print(remainder)

# Question 3: Calculate the square of 25
print("\nQuestion 3: Calculate the square of 25")
 n=25
print(n**2)

# Question 4: Find the cube root of 125
print("\nQuestion 4: Find the cube root of 125")
n=125
print(n**3)

# Question 5: Calculate the sum of digits in number 12345
print("\nQuestion 5: Calculate the sum of digits in number 12345")
n=[1,2,3,4,5]
sum=0
for i in n:
 sum+=i
print(sum)

# Question 6: Check if 97 is a prime number
print("\nQuestion 6: Check if 97 is a prime number")
num = 97
if (num%i ==0):
    print(f"{num} is not a prime")
else:
    print(f"{num} is a prime")

# Question 7: Find the factorial of 8
print("\nQuestion 7: Find the factorial of 8")
fact=8
for i in range(1,fact):
 fact=fact*i 
print(fact)

# Question 8: Calculate the average of numbers: 15, 23, 31, 42, 56
print("\nQuestion 8: Calculate the average of numbers: 15, 23, 31, 42, 56")
n=[15,23,31,42,56]
sum=0
for i in n:
    sum=sum+i
print(sum/len(n))

# Question 9: Find the greatest common divisor (GCD) of 48 and 36
print("\nQuestion 9: Find the greatest common divisor (GCD) of 48 and 36")
a=48
b=56
while b!=0:
  a,b=b,a%b
print(a)

# Question 10: Calculate the sum of first 20 odd numbers
print("\nQuestion 10: Calculate the sum of first 20 odd numbers")
odd_sum=0
count=0
n=1
while count<20:
 odd_sum=odd_sum+n
 n=n+2
 count+=1
print(odd_sum)
