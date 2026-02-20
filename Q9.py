#Given list of scores, use while loop and conditionals to count passing (>=60) vs failing
# List of scores
scores = [70, 50, 95, 67, 35, 81, 20]

i = 0
while i < len(scores):
    if scores[i] >= 60:
        passing = i + 1
    else:
        failing = i + 1
    i = i + 1

print("Passing students:", passing)
print("Failing students:", failing)


