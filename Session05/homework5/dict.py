inventory ={
    'gold' : 500,
    'pounch' : ['flint', 'twine', 'gemstone'],
    'backpack' : ['a', 'b', 'c', 'd']
}

inventory['pocket'] = ['seashell', 'berry', 'lint']
print(inventory)

inventory['backpack'].remove('b')

print(inventory)
inventory['gold'] += 50

print(inventory)
