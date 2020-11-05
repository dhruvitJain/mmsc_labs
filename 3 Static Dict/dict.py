from sys import getsizeof
string1 = 'and or and with or not go for and not got for with and for go on there'

l1= string1.split()
print (l1)

dict1 = {}
for word in l1:
	i=l1.count(word)
	dict1.update ({word:i})
# print (dict1)

words = list (dict1.keys())
# print (words)

dict2 = {}
k=1
for i in words:
	dict2.update({i:k})
	k+=1
print (dict2)

l1 = [dict2[k] for k in l1]
#print (l1)

str2 = ' '.join([str(elem) for elem in l1]) 
print(str2)  

b1 = getsizeof(string1)
b2 = getsizeof(str2)
print (f"Compression Ratio = {b1}/{b2} = " + str(b1/b2))