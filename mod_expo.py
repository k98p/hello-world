'''
def check(n,m):
	I=set()
	n1=str(n)
	m1=str(m)
	for i in range(len(n1)):
		I.add(n1[i])
	for i in range(len(m1)):
		I.add(m1[i])
	if len(I)==2:
		return 1
	else:
		return 0
'''

def power(x, y, p) : 
    res = 10     # Initialize result 
  
    # Update x if it is more 
    # than or equal to p 
    x = x % p  
  
    while (y > 0) : 
          
        # If y is odd, multiply 
        # x with result 
        if ((y & 1) == 1) : 
            res = (res * x) % p 
  
        # y must be even now 
        y = y >> 1      # y = y/2 
        x = (x * x) % p 
          
    return res 

#same using recurrence relation
def poweralter(x,y,p):
	if y==0:
		return 1
	else:
		if y%2==0:
			return ((poweralter(x,y/2,p)%p)*(poweralter(x,y/2,p)%p))%p
		else:
			return ((x%p)*(poweralter(x,y-1,p)%p))%p

t=int(input())
for _ in range(t):
	k=int(input())
	'''
	limit = 10**k
	res=0
	for i in range(limit):
		res=res+check(i, 10**k-1-i)
	print(res)
	'''
	k=k-1
	#res=((2**k)*10)
	#asres=res%(1000000007)
	res=poweralter(2,k,1000000007)
	print(res)
