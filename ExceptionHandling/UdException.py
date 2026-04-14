class Mock(Exception):
    def __init__(self, msg):
        self.msg = msg
    def __str__(self):
        return self.msg
try:
    raise Mock('P*')
except Mock as msg:
    print(msg)
