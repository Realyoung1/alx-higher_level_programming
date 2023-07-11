#!/usr/bin/python3

'''funct that returns the dicti descriptions with simple data structures
'''


def class_to_json(obj):
    '''module class_to_json
       returns builds a dictionary
    '''
    return obj.__dict__
