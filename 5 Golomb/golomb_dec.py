import math 

def unary_code_decimal (x):
	return x.count('1')

m=int(input("Enter value of m: "))
ip = input("Enter string to be decoded: ")
k=math.ceil(math.log(m,2))
print ("k =",k)
c= 2**k -m
print ('c =',c)

q = ''
for char in ip:
	if char == '1':
		q+=char
	if char == '0':
		q+='0'
		break
print ('q in unary code =',q)
q1=unary_code_decimal (q)
print ('q in decimal =',q1)


r = ip[len(q):] #after removal of q
# print (r)
r1 = r[0:k-1] #k-1 bits
print ("Next k-1 bits = ",r1)
r3 = r[k-1:k] #next ip bit
print ('Next input bit =',r3)
r1="0b"+r1
print ('r in binary = ',r1)

r2 = int (r1,2)
print ('r in decimal =',r2)

if r2<c:
	n=r2+(q1*m)
	print ("n =",n)
else:
	r2=r2*2 + int(r3)
	n=r2-c+(q1*m)
	print ("n =",n)