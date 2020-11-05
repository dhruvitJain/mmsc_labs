import math 

def unary_code (x):
	ones = x*'1'+'0'
	return ones

m=14
n=8

k=math.ceil(math.log(m,2))
print ("k =",k)
r=n%m
print ('r =',r)
c= 2**k -m
print ('c =',c)
q=math.floor (n/m)
print ('q =',q)
uc= unary_code(q)
print ('Unary code of q is =',uc)

if r>=c:
	r=r+c
	binary=bin(r).replace("0b", "")
	binary = binary.zfill (k)
	print ("Binary code of r is =",binary)
else:
	binary=bin(r).replace("0b", "")
	binary = binary.zfill (k-1)
	print ("Binary code of r is =",binary)

qr = uc+binary
print ("Golomb Code = ",qr)





