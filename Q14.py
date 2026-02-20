#Simulate shopping cart: list of dicts {item: price}; loop to apply 10% discount if total >100
#list of dicts
cart = [{'Bread': 60},{'butter': 55},{'egg': 30},{'Tea': 250},{'Chocolate':100}] #{item:price}
print('---Access complete list of dicts---')
print(cart)
total = 0

#Nested For loop
for c in cart:
    for key, value in c.items():
        total = total + value
print('Total amount:', total)

#Apply 10% discount if total > 100
if total > 100:
    disc = total * 0.10
    total = total - disc
    print('10% discount is applied')
else:
    print('No discount applied')

print('Final amount to pay:', total)
