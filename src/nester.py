"""This module prints lists that may or may not contain nested lists"""


def print_lol(the_list, tabs):
    """This function takes a positional argument: called "the_list", which is any
Python list which may include nested lists.  Each data item in the provided lists
recursively printed to the screen on its own line."""
    for each_item in the_list:
        if isinstance(each_item,list):
            print_lol(each_item)
        else:
            for(num in range(tabs)):
                print("\t",end="")
            print(each_item)
    
