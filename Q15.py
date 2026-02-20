#Function to remove duplicates from list of dicts by key 'id' using set of ids
cart = [{'id': 1, 'name': "Ben10"},{'id': 2, 'name': 'Avengers'},{'id': 1, 'name': 'Spiderman'},
        {'id': 3, 'name': 'Batman'},{'id': 2, 'name': 'Superman'},{'id': 4, 'name': 'Krish'}] # List of dicts
print('---- Original list of dicts ---')
print(cart)
def removeDuplicates(cart):
    seenIds = set()  # Set to track seen ids
    cartlist = []  # List to store unique items

    for c in cart:
        if c['id'] not in seenIds:
            cartlist.append(c)  # Add unique item to the list
            seenIds.add(c['id'])  # Add id that are seen
    return cartlist
print('---- List of dicts after removing duplicates ---')
#call the function
result = removeDuplicates(cart)
print(result)