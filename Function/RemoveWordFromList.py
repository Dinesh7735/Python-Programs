#Removing a word from list
def RemoveWord(l,w):
    l.remove(w)
    return l
L=['Jaga','Rahul','Romio','Roshan']
print(L)
w=input(f"Enter any name present in above list: ")
print(f"New list after removing the word \n {RemoveWord(L,w)}")