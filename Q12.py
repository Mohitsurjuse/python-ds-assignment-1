#Dictionary of {student: [grades]}; compute averages with loop, store in new dict, print top 3 

students = {'Bruce': [80, 75, 90],'Optimus': [60, 65, 70],'Steve': [88, 92, 85],'Tony': [95, 90, 93],'Ultron': [70, 80, 75]}
print("---Original dictionary of students and grades---")
print(students)
averages = {}

# Calculate averages with loop
for s in students:
    grades = students[s]
    avg = sum(grades) / len(grades)
    averages[s] = avg
    print(f'Average Marks of {s}: {avg:.2f}')

# Sort and print top 3
sorted_students = sorted(averages.items(), key=lambda x: x[1], reverse=True)

print("Top 3 Students are:")
for i in range(3):
    s, avg = sorted_students[i]
    print(f'Average Marks of {s}: {avg:.2f}')