import json
D = {'a':['hello',21], '3':23}
with open('C:/Users/DINESH/OneDrive/Desktop/M85/Dinesh1.json','w') as fobj:
    json.dump(D,fobj,indent=4)