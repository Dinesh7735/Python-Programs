class Programmer:
    company = 'Microsoft'
    def __init__(self,name,salary,designation):
        self.name = name
        self.designation = designation
        self.salary = salary
e1 = Programmer('Dinesh',1200000,'Python Developer')
print(f'{e1.name} is working in {e1.company} as a {e1.designation} and getting salary {e1.salary}.')
