# Basis of a test
# You will be testing functions or methods, these need to be called or initialised
# Having controlled inputs for known outputs and testing

# Make test for make_dough
# Our factory should take in water and flour to make dough
print(make_dough('water', 'flour') == 'dough')

# Make test for bake_dough
# Then put the dough in the oven to produce the Naan
print(bake_dough('dough') == 'Naan')