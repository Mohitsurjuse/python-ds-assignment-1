#Create a list of 10 numbers, loop to find and print the maximum using only conditionals (no max()).
a = [10, 24, 76, 23, 12, 95, 67, 50, 1, 33] #list of 10 numbers

res = a[0] # Assume first element is maximum
for n in a: #for loop in python
    if n > res: #conditional statement
        res = n
print(f'The Maximum number is: {res}') 