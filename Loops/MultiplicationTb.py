#A program to print multiplication table of any number
n=int(input("Enter a number: "))
for i in range(1,11):
    print(f"{n} * {i} = {n*i}")