fib_sequence=[1,2]

next_number=fib_sequence[len(fib_sequence)-2]+fib_sequence[len(fib_sequence)-1]

while next_number<4000000:
	fib_sequence.append(next_number)
	next_number=fib_sequence[len(fib_sequence)-2]+fib_sequence[len(fib_sequence)-1]

total=0
for x in fib_sequence:
	if x%2==0:
		total+=x
print(total)
