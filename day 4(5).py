def reverse_string(str): 
 tr1 = "" 
 for i in str: 
     tr1 = i + tr1 
 return tr1 
str = "TEMPLE" 
print("The original string is: ",str) 
print("The reverse string is",reverse_string(str))
