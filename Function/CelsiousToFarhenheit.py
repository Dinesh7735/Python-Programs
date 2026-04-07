#Celsios to Farhenheit
def CelsiousToFarheheit(f):
    return 5*(f-32)/9
f=int(input("Enter temprature in F: "))
c=CelsiousToFarheheit(f)
print(f"{round(c,2)}°C")