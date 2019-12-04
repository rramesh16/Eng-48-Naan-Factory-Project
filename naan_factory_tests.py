from naan_factory_functions import *

# Tests go here for separation of concern

# Make test for make_dough
print("Testing make_dough with 'water' and 'flour'. Expected --> 'dough'")
print(make_dough('water', 'flour') == 'dough')
print('got:', make_dough('water', 'flour') )

#When I pass in cement and water or any other arguement...I should get: 'Not dough'

print("Testing make_dough with 'cement' and 'water'. Expected --> 'not dough'")
print(make_dough('cement','sand') == 'not dough')
print('got:', make_dough('cement', 'sand'))



# Make test for bake_dough
print("Testing bake_dough with 'dough'. Expected --> 'Naan'")
print(bake_dough('dough') == 'Naan')
print("When calling bake dough('dough'), got:", bake_dough('dough'))

# When bake_dough is passed something other than 'dough' it should output: 'not Naan'
print("Testing bake_dough with 'chicken'. Expected --> 'not Naan'")
print(bake_dough('chicken') == 'not Naan')
print("When calling bake dough('chicken'), got:", bake_dough('chicken'))