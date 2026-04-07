#sum of n natural numbers using recursion
def SumOfNaturalNo(n):
    if n==1:
        return 1
    else:
        return n+SumOfNaturalNo(n-1)
num=int(input("Enter a number: "))
print(f"Sum of first {num} natural number is {SumOfNaturalNo(10)}")    
