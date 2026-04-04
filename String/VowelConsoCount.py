s='My name is dinesh'
vowel=0
conso=0
for ch in s:
    if ch =='a' or ch =='e' or  ch =='i' or  ch =='o' or  ch =='u' or  ch =='A' or  ch =='E' or  ch =='I' or  ch =='O' or  ch =='U':
        vowel+=1 
    else:
        if ch!=' ':
            conso+=1
print(f'No of vowel present in the string is {vowel}')
print(f'No of consonent present in the string is {conso}')