str=input('Enter a string: ')
rev=''
for ch in range(-1,-(len(str)+1),-1):
    rev+=str[ch]
print(rev)