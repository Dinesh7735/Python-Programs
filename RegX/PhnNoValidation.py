import re
mob = '+91 7735455415'
if re.match('^[+]91( |-)[6-9][0-9]{9}$',mob):
    print('Valid')
else:
    print('Invalid')