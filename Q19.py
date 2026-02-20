#Tuple unpacking: Loop over list of (x,y) coords, dict to count quadrant (if x>0,y>0 etc.)
# List of (x, y) coordinates
points = [(2, 3), (-1, 4), (-3, -5), (4, -2), (0, 3), (5, 6)]
print('--- Original Points ---')
print(points)
# Dictionary to count quadrants
quads = {'Q1': 0, 'Q2': 0, 'Q3': 0, 'Q4': 0}

# Loop with tuple unpacking
for x, y in points:
    if x > 0 and y > 0:
        quads['Q1'] = quads['Q1'] + 1
    elif x < 0 and y > 0:
        quads['Q2'] = quads['Q2'] + 1
    elif x < 0 and y < 0:
        quads['Q3'] = quads['Q3'] + 1
    elif x > 0 and y < 0:
        quads['Q4'] = quads['Q4'] + 1

print("Quadrant Count:")
print(quads)