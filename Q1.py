#Write a function using a while loop to print even numbers from 1 to 20
#While Loop in python
print("Even numbers from 1 to 20 are: ")
i = 1
while i <= 20: #while is indentation block
    if i % 2 == 0:
        print(i, end=' ') #to print data on same line
    i = i+1