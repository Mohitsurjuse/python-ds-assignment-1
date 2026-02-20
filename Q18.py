#Generate 20 random nums (1-100), use sets for uniques, dict for frequency, print most common with conditional
import random

numbers = [] 
for i in range(20):
    numbers.append(random.randint(1, 100)) # Generate 20 random numbers(1-100)
print("Random Numbers:", numbers)

# Use set for uniques
uniques = set(numbers)
print("Unique Numbers:", uniques)

# dict for frequency
freq = {}

for num in numbers:
    if num in freq:
        freq[num] = freq[num] + 1
    else:
        freq[num] = 1
print("Frequency:", freq)

# Find most common number
max = 0
mostCmn = None

for num in freq:
    if freq[num] > max:
        max = freq[num]
        mostCmn = num

print("Most Common Number:", mostCmn)