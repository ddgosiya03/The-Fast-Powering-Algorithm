#fast power algoritham
p=int(input('Enter a prime: '))
g=int(input('Enter a base: '))
s=int(input('Enter power: '))
j=s
blist=[]
plist=[]
while True:
	q=s//2
	r=s%2
	blist.append(r)
	if q!=0:
		print('2 | {} | {}'.format(s,r))
		print('-------------')
		s=q
	else:
		print('2 | {} | {}'.format(s,r))
		break
u=0
l=0
for y in blist:
	c='{}*(2^{})'.format(y,u)
	l='{}+{}'.format(l,c)
	u=u+1
print('\n',j,'=',l)	
d=(g**(2**0))%p
plist.append(d)
for i in range(len(blist)-1):
	b=(d*d)%p
	plist.append(b)
	d=b
print('\n',plist,'\n')	
m=0
n=1
while True:
	if m<len(plist):
		n=((plist[m]**blist[m])*n)%p
		m=m+1
	else:
		break
	
print('\n',g,'^',j,'=',n,'mod',p,'\n')