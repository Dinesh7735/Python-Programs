#A program to print multiplication table of any number using function
def Multiplication(n):
    for i in range(1,11):
        print(f"{n} X {i} = {n*i}")
num=int(input("Enter a number: "))
Multiplication(num)