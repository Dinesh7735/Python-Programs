#A program to print even numbers between any range
start=int(input('Enter the starting number: '))
last=int(input('Enter the last number: '))
print("All even numbers are: ")
for val in range(start,last+1):
    if val%2==0:
        print(val)
print("All odd numbers are: ")
for val in range(start,last+1):
    if val%2!=0:
        print(val)