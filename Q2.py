#Use if-elif-else to classify a number as positive, negative, or zero; test in a for loop over a list.
numbers = [1, -2, 3, 0, 4, -5, 7, 0, -8 ] #test list
for num in numbers:  #for loop
#Nested conditions
    if num > 0:
        print( f"The Number {num} is Positive")
    elif num < 0:
        print(f"The Number {num} is Negative")
    else:
        print(f"The Number {num} is Zero")