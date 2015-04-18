"""
Project Euler problem 3 solve

The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?
"""
#from __future__ import print_function
import sys
 
 
def is_prime(num):
    """Checks if num is prime number"""
    for i in range(2, num):
        if not num % i:
            return False
    return True
 

# TODO Optimize solution
def find_prime_factors(num):
    """Find prime factors of num"""
    result = []
    for i in range(2, num):
        if is_prime(i) and not num % i:
            result.append(i)
    return result
 
 
if __name__ == '__main__':
    try:
        num = int(sys.argv[1])
    except (TypeError, ValueError, IndexError):
        sys.exit("Usage: euler_3.py number")
    if num < 1:
        sys.exit("Error: number must be greater than zero")
 
    prime_factors = find_prime_factors(num)
    if len(prime_factors) == 0:
        print("Can't find prime factors of %d" % num)
    else:
        print("Answer: %d" % prime_factors[-1])