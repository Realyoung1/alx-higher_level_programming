#!/usr/bin/python3


def search_replace(my_list, search, replace):
    """
    search and replace an element in a list
    Args:
        my_list - The function for the list to search.
        search - the function of the elments to replaced.
        replace - subtitute for searches.
    """
    if my_list is None:
        return None
    return [replace if q == search else q for q in my_list]
