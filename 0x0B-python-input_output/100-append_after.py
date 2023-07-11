#!/usr/bin/python3

"""
functionss that inserts a liness of text to a file, after each line containing a specific strings.
"""

def append_after(filename="", search_string="", new_string=""):
    '''module Search and update
    '''
    with open(filename, 'r+') as f:
        lines = f.readlines()
        x = 0
        for line in lines:
            if line.find(search_string) is not -1:
                lines.insert(x + 1, new_string)
            x += 1
        f.seek(0)
        f.write("".join(lines))
