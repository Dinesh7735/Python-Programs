class Bank:
    IFSC = 'BANK000420'
    ROI = 0.07

    def  __init__(self,name,accno,bal,mobno,pin):
        self.name = name
        self.accno = accno
        self.bal = bal
        self.mobno = mobno
        self.pin = pin

    @staticmethod
    def getPassword():
        return int(input('Enter your 4 digit pin- '))

    def Details(self):
        print(f'Name : {self.name}')
        print(f'Account Number: {self.accno}')
        print(f'Mobile Number: {self.mobno}')
    
    def Withdrawn(self):
        attempts = 3
        while attempts > 0:
            if self.getPassword() == self.pin:
                amount = int(input('Enter the amount to withdraw: '))
                if amount % 100 == 0:
                    if 500 <= amount <= 10000:
                        if amount <= self.bal:
                            self.bal -= amount
                            print('Transaction Successfull....')
                            print(f'Available Balance = {self.bal}')
                            break
                        else:
                            print('Insufficient Amount')
                    else:
                        print('Minimum withdraw amount = 500 and maximum withdraw amount = 10000')
                else:
                    print('Enter a valid amount')
            else:
                attempts -= 1
                print('Incorrect Password')
                print(f'Remaning attempts {attempts}')
        else:
            print('No more attempts left')
            print('Try after 24 hours')
                
    def Deposite(self):
        if self.accno == int(input('Enter your Account number: ')):
            amount = int(input('Enter amount to deposite: '))
            if amount % 100 == 0:
                if 500 <= amount <= 50000:
                    self.bal += amount
                    print(f'Available Balance = {self.bal}')
                else:
                    print('You can add between 500 to 50000 Rs.')
            else:
                print('Add a valid amount')
        else:
            print('Enter a valid account number')

    def checkBalance(self):
        attempts = 3
        while attempts > 0:
            if self.getPassword == self.pin:
                print(f'Available Balance = {self.bal}')
                break
            else:
                attempts -= 1
                print('Incorrect Password')
                print(f'Remaning attempts: {attempts}')

        else:
            print('No more attempts left')
            print('Truy after 24 hours')
    
    @classmethod
    def changeROI(cls):
        cls.ROI = 0.08

obj1 = Bank('Saroj',123456789,10000,7735455250,1111)
boj2 = Bank('Ashish',789456123,20000,7064180246,2222)
obj2 = Bank('Pravat',123789456,50000,1234567890,3333)
obj1.Withdrawn()
