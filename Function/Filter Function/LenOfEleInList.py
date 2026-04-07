print(list(filter(len,['1234','250','420','','123'])))

#O/p:- ['1234','250','123'] Because Filter only gives the True value an empty string('') lenth will be 0, 
# So filter will not accept it because it is a False value and filter gives the actual value so instead of 
# the length of element the actual element will be printed