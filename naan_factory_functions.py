# Functions go here

def make_dough(arg1, arg2):
    if arg1 != 'water' and arg2 != 'water':
        return 'not dough'
    elif arg1 != 'flour' and arg2 != 'flour':
        return 'not dough'
    else:
        return 'dough'


def bake_dough(arg1):
    if arg1 != 'dough':
        return 'not Naan'
    else:
        return 'Naan'


