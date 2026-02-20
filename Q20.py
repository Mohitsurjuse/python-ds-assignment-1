#Prime finder: Loop 1-100, check primality with while/for, store in set, list primes in dict by digit sum
# Function to check if a number is prime
def isPrime(n):
    if n <= 1:
        return False
    for i in range(2, int(n*0.5) + 1):
        if n % i == 0:
            return False
    return True

# Set to store unique prime numbers
primeNum = set()

# Loop through numbers 1 to 100 and check for primality
for r in range(1, 101):
    if isPrime(r):
        primeNum.add(r)
print("Prime Numbers:", primeNum)

# Dictionary to store primes by digit sum
primeDict = {}
for p in primeNum:
    digitSum = sum(int(digit) for digit in str(p))
    if digitSum in primeDict:
        primeDict[digitSum].append(p)
    else:
        primeDict[digitSum] = [p]
print("Primes by Digit Sum:")
print(primeDict)