#Factorial of a number using recursion
num=int(input("Enter a number: "))
def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)
print(f"Factorial of {num} is {factorial(num)}")