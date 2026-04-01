class Father:
    def Feature(self):
        print('Caring and Responsible')
class Mother:
    def Feature(self):
        print('Loving and Caring')
class Child(Father,Mother):
    def Feature(self):
        super().Feature()
        Mother.Feature(self)
        print('Study and Scorlling Reels')
obj = Child()
obj.Feature()
