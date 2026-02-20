#Write a function that takes a list and returns a new list with only unique elements using a set
nums = [1, 2, 3, 2, 4, 5, 1, 7, 5, 9] 
print('---Original List---')
print(nums)
def uniqueElements(nums): #uniquelist() function is created that takes nums as parameter
    newList = list(set(nums))
    return newList
#call the function
result = uniqueElements(nums)
print('---New list with only unique elements---')
print(result)
