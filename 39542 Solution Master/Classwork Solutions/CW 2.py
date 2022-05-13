"""
Name: Katherine St. John
Email: katherine.stjohn@hunter.cuny.edu
Resources:  Used CSci 127 textbook for files and python documentation for keyword args
I attended lecture today.
Row: Podium/Front
Seat: 1
"""

def make_dict(file_name, sep = ": "):
    """
    Opens and reads from file_name, and returns a dictionary.

    Keyword arguments:
    sep -- the deliminators for splitting up the data (default ': ')
    """

    d = {}
    with open(file_name) as fd:
        for l in fd:
            if l.find(sep) > -1:
                words = l[:-1].split(sep)
                d[words[0]] = words[1]
    return d
