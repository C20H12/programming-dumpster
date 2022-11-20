def isPrime(n):
  if n == 1 or n == 0:        # 1 and 0 are not prime numbers
    return False
  for i in range(2, n // 2):  # check if n is divisible by any number between 2 and half of the number
    if n % i == 0:            # if n is divisible by i, then n is not prime
      return False  
  return True                 # if n is not divisible by any number between 2 and n / 2, then n is prime

def printPrimeFactors(n):
  for i in range(2, n):             # loop from 2 to n, since 2 is the least prime number
    if n % i == 0 and isPrime(i):   # if n is divisible by i and i is prime, then i is a prime factor of n
      print(i)


def printGCF(n1, n2):
  smaller = n1 if n1 < n2 else n2
  for i in range(smaller, 1, -1):         # loop, count down from the smaller number, since the GCF cannot be greater than the smaller number
    if n1 % i == 0 and n2 % i == 0:       # if n1 and n2 are divisible by i, then i is the greatest common factor of n1 and n2
      print(i)
      break

def printLCM(n1, n2):
  for i in range(1, n1 * n2):            # loop from 1 to n1 * n2, since the LCM cannot be greater than n1 * n2
    if i % n1 == 0 and i % n2 == 0:      # if i is divisible by n1 and n2, then i is the least common multiple of n1 and n2
      print(i)
      break

num1 = int(input("Please enter a number: ")) 
num2 = int(input("Please enter another number: "))

print(f"The prime factors of {num1} are")
printPrimeFactors(num1)

print(f"The prime factors of {num2} are")
printPrimeFactors(num2)

print(f"The greatest common factor of {num1} and {num2} is:")
printGCF(num1, num2)

print(f"The least common multiple of {num1} and {num2} is:")
printLCM(num1, num2)
