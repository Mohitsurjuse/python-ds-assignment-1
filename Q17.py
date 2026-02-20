#Nested dict {class: {student: grades}}; function to find class average using recursion-like loops
classes = {'Class1': {'Ramesh': 65, 'Jayesh': 60, 'Suresh': 65},
           'Class2': {'Chintu': 82, 'Mintu': 80, 'Pintu': 81},
           'Class3': {'Jaya': 60, 'Pushpa': 70, 'Nirma': 67},
           'Class4': {'Amar': 85, 'Akbar': 90, 'Anthony': 95}}
def calcClassAvg(className):
    studs = classes[className]
    totalGrades = sum(studs.values())
    avgGrade = totalGrades / 3
    return [f'Average grade for {className} is {avgGrade:.2f}']
# Example usage
print(calcClassAvg('Class1'))
print(calcClassAvg('Class2'))
print(calcClassAvg('Class3'))
print(calcClassAvg('Class4'))