palindromes=[]
for x in range(999,0,-1):
	for y in range(999,0,-1):
		current_number=str(x*y)
		if len(current_number)==6:
			if current_number[0]==current_number[5] and current_number[1]==current_number[4] and current_number[2]==current_number[3]:
				print(current_number)
				palindromes.append(current_number)
	else:
		continue
palindromes.sort()
print(palindromes)
