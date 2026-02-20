#Use nested for loops and if to print a multiplication table (1-10) as a list of tuples. 

table = [] #empty list
#Nested for loops to multiply from 1 to 10
for i in range(1, 11):
    for j in range(1, 11):
        if i >= 1 and j >= 1:
            table.append(( i, j, i * j)) #append is used to add item at end of list
print('---Tables from 1 to 10 are:---')
print(table)
