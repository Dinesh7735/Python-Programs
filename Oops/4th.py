import random

class Train:
    def __init__(self,trainNo):
        self.trainNo = trainNo
    
    def bookTicket(self,From,to):
        print(f'Ticket booked successfully on trainNo {self.trainNo} from {From} to {to}.')
    
    def status(self):
        print(f'TrainNo {self.trainNo} is running on time')

    def fare(self,From,to):
        print(f'TrainNo {self.trainNo} from {From} to {to} is chraging Rs: {random.randint(1,20000)}.')

t = Train(768045)
t.bookTicket('Bargarh','Banglore')
t.status()
t.fare('Bargarh','Bangalore')