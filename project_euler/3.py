import math
import time

def find_odd_factors(target_number):
	odd_factors=[]
	print("Finding odd factors of "+str(target_number))
	print()
	time.sleep(2)
	for potential_odd_factor in range(3,int(math.sqrt(target_number)),2): 
		if target_number%potential_odd_factor==0: #is a factor of target number
			if potential_odd_factor%2 != 0: 		  #is an odd factor of target number
				odd_factors.append(potential_odd_factor)
				print(potential_odd_factor)
	print("Success!")
	print()
	return odd_factors

def find_primes(odd_number_list):
	primes=[]
	print("Finding which odd numbers in input list are prime")
	print()
	time.sleep(2)
	for potential_prime in odd_number_list:
		for y in range(3,math.ceil(potential_prime/2),2):
			if potential_prime%y==0:
				break
		else:
			primes.append(potential_prime)
			print(potential_prime)
	print("Success!")
	print()
	return primes

odd_factor_list=find_odd_factors(int(input("Enter a number to find the prime factors of: ")))
prime_factors=find_primes(odd_factor_list)
print("prime factors are",prime_factors)
highest_prime_factor=prime_factors[len(prime_factors)-1]

print("The highest prime factor of your target number is " + str(highest_prime_factor))
