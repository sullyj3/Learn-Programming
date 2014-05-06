import math
primes=[]
debug=True

def debug_print(x):
    if debug==True:
        print(x)

def main():
    tally=1
    number_being_tested==3
    while tally<=10001:
        #test numbers for primacy
        if isitprime(number_being_tested)==True:
            primes.append(number_being_tested)
            tally+=1
            number_being_tested+=2	
        return primes[10000]	


#todo debug isitprime() returns True on 9

def isitprime(potential_prime):#only works when potential_prime is larger than the largest number in primes and potential_prime is odd
    debug_print("testing "+str(potential_prime)+" for divisibility by existing found primes")
    for n in primes:#if potential_prime divisible by existing prime, it's not prime.
        debug_print("testing "+str(potential_prime)+" for divisibility by "+str(n))
        if potential_prime%n==0:
            debug_print(str(potential_prime)+" is not prime (evenly divisible by "+str(n)+")")
            return False
    
    debug_print("testing "+str(potential_prime)+" for divisibility by odd numbers up to its square root rounded ("+str(round(math.sqrt(potential_prime+1)))+")")
    search_area=[3]
    for n in range(3,round(math.sqrt(potential_prime+1)),2):
        debug_print("appending "+str(n)+" to search area")
        search_area.append(n)
    for n in search_area:
        debug_print("testing "+str(potential_prime)+" for divisibility by "+str(n))
        if potential_prime%n==0:
            debug_print(str(potential_prime)+" is not prime (evenly divisible by "+str(n)+")")
            return False
    else:
        primes.append(potential_prime)
        debug_print(str(potential_prime)+" is prime")
        return True

for x in range(2,11): #don't start at one! you'll fuck the whole thing up!
    isitprime(x)
    print()

