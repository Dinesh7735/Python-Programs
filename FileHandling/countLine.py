with open('C:/Users/DINESH/OneDrive/Desktop/M85/Rahul.txt','r') as fobj:
    count = 0
    for line in fobj:
        count += len(line.strip('\n'))
    print(count)