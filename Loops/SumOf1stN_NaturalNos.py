#Sum of 1st n natural numbers
num=int(input("Enter the number: "))
sum=0
for val in range(1,num+1):
    sum=sum+val
print(f'Sum of first 10 natural numbers is {sum}')