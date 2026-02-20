#Function to reverse a list using a for loop and slicing; compare with tuples (immutable)
#List in python - can be changed, add, delete data after defined
cities = ['Amravati','Mumbai','Delhi','Bangalore','Hyderabad']

revlist = []

for i in cities[::-1]:
    revlist.append(i)

print("---Original list---")
print(cities)
print("---Reversed list---")
print(revlist)


# compare with tuples (immutable) - cannot be changed, add, delete data after defined
t = ('Amravati','Mumbai','Delhi','Bangalore','Hyderabad')
revtuple = t[::-1]

print("---Original tuple---")
print(t)
print("---Reversed tuple---")
print(revtuple)