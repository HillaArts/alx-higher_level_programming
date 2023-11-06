#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    '''
    finds all multiples of 2 in a list
    '''
    new_list = [True if i % 2 == 0 else False for i in my_list]
    return (new_list)
