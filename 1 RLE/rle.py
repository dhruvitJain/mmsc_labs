data = input ("Enter the string: ")
n = len (data)
count = 1
output = ""
for i in range (0,n-1):
	if data [i] == data [i+1]:
		count = count +1 
	else:
		output += data[i] + str(count)
		count = 1

output += data[i] + str(count) 
print (output)

