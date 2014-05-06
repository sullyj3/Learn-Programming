def findsumsquares(a):#find sum of squares of all natural numbers up to and including a
	sumsquares=0
	for cnum in range(1,a+1):
		sumsquares+=cnum**2
	return sumsquares

def findsquaresum(b):#find square of sum of all natural numbers up to and including b
	squaresum=0
	for cnum in range(1,b+1):
		squaresum+=cnum
	squaresum**=2
	return squaresum

ubound=int(input('what number? '))

susq=findsumsquares(ubound)
sqsu=findsquaresum(ubound)

print('The sum of the squares of all integers up to',str(ubound),'is',str(susq))
print('The square of the sum of all integers up to',str(ubound),'is',str(sqsu))

print('The difference between them is',str(abs(susq-sqsu)))
