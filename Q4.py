#Define a tuple of fruits; use a for loop to print those starting with 'A' or 'B'.
#Tuples in Python
fruits = ('Apple', 'Banana', 'Cherry', 'Mango','Watermelon', 'Avocado', 'Orange', 'Blueberry', 'Grapes')
print('---Access complete Tuple---')
print(fruits)
#Tuple is comprehended into list
a1 = tuple([f for f in fruits if 'A' in f]) #access tuple using for loop
b1 = tuple([f for f in fruits if 'B' in f]) 
print(a1)
print(b1)