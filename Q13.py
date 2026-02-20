#Use list comprehension with if to filter even numbers from 1-50 into a tuple
#List comprehension
nums = range(1, 51)
nums1 = tuple([n for n in nums if n % 2 == 0])
print('---Even numbers from 1 to 50---')
print(nums1)