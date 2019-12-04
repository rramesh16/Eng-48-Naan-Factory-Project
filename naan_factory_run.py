# here we run the factory (functions)
from naan_factory_functions import *

# Call the functions
print('//Welcome to the Naan factory//')
produce1 = input('What is the first produce?')
produce2 = input('Second produce?')

# output1 = make_dough(produce1, produce2)
# final_output = bake_dough(output1)

final_output = run_factory(produce1, produce2)
print('Well done! You made some: ', final_output)
