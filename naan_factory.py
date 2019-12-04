# Basis of a test
# You will be testing functions or methods, these need to be called or initialised
# Having controlled inputs for known outputs and testing

def make_dough(arg1, arg2):
    pass

def bake_dough(arg1):
    pass

# Make test for make_dough
print("Testing make_dough with 'water' and 'flour'. Expected --> 'dough'")
print(make_dough('water', 'flour') == 'dough')
print('got:', make_dough('water', 'flour'))

# Make test for bake_dough
print("Testing bake_dough with 'dough'. Expected --> 'Naan'")
print(bake_dough('dough') == 'Naan')
print('got:', bake_dough('dough'))