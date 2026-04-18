import re
S = 'naikdinesh544@gmail.com'
if re.match('^[A-Za-z0-9._]+@gmail.com$',S) and len(S[:-10]) <= 230 and '..' not in S and '__' not in S:
    print('Valid')
else:
    print('Invalid')