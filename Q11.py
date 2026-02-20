#Function: Input list of tuples (id, score); sort by score descending using sorted() and loop
# List of tuples
data = [(101, 85), (102, 92), (103, 78), (104, 90)] #(id, score)
print("---Original list of tuples (id,score)---")
print(data)
#Using sorted() to sort by score in descending order
sorted_data = sorted(data, key=lambda x: x[1], reverse=True)
print("---Sorted list of tuples (id,score)---")
#For loop to print sorted data
for item in sorted_data:
    print(item)