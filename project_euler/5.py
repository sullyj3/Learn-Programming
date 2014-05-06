x=0
found=False
while found==False:
	x+=8580
	for oneto20 in range(11,21):
		remainder=x%oneto20
		if remainder!=0:
			print(str(x)+" Is not evenly divisible by "+str(oneto20))
			break
		else:
			print(str(x)+" IS evenly divisible by "+str(oneto20))
	else:
		print(str(x))
		found=True
		break
