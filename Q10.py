#Merge two sets of numbers; use intersection and union, print differences with loop
a = {1, 2, 3, 4}
b = {3, 4, 5, 6, 7, 8}

# Union of sets
union = a | b
print("Union:",union)

# Intersection of sets
intsect = a & b
print("Intersection:",intsect) 

# Differences using loop
print("Difference (a - b):")
for num in a:
    if num not in b:
        print(num,end=' ')

print("\n Difference (b - a):")
for num in b:
    if num not in a:
        print(num,end=' ')