from sys import getsizeof

dict1 = {'a':0, 'b':1, 'c':2, 'd':3, 'r':4, 'ab':5,'ac':6,'ad':7}
string1 = 'abracadabra '
str1 = list(string1)
print (str1)
n = len (str1)
string2=''
i=0
while i < n-1:
	a=str1[i]
	b=str1[i+1]
	c=a+b
	if c in dict1:
		string2+=str((dict1[c]))
		i+=2
	else:
		string2+=str((dict1[a]))
		i+=1

print(string2) 

b1 = getsizeof(string1)
b2 = getsizeof(string2)
print (f"Compression Ratio = {b1}/{b2} = " + str(b1/b2))