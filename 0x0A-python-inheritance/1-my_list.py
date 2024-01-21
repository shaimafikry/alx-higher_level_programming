#!/usr/bin/python3
"""my list class
    """


class MyList(list):
    """class mylist inherits from list class

    Args:
        list (_class_): base class
    """
    def print_sorted(self):
        self.m = sorted(self)
        print(self.m)
