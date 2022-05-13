"""
Name: Katherine St. John
Email: katherine.stjohn@hunter.cuny.edu
Resources:  Used CSci 127 textbook for files and pandas documentation for keyword args
"""

def extract_names(file_name, sep = ["\n"]):
    """
    Opens and reads from file_name, and returns a list of names.

    Keyword arguments:
    sep -- the deliminators for splitting up the data (default ['\n'])
    """

    with open(file_name) as fd:
        data = fd.read()
        if len(sep) == 1:
            lst = data.split(sep[0])
        else:
            tmpData = data
            for s in sep[:-1]:
                tmpData = sep[-1].join(data.split(s))
                #print(s, tmpData)
            lst = tmpData.split(sep[-1])
    lst = [w for w in lst if len(w) > 0]
    return lst

def count_names(names_lst):
    """
    Returns a dictionary of names with values the number of times each name occurs
    in the input, names_lst.
    """
    dict = {}
    for n in names_lst:
        if n in dict:
            dict[n] += 1
        else:
            dict[n] = 1
    return dict

def popular_names(names_dict,num = 3):
    """
    Returns a list of the num most popular names as a list of strings. If no value is passed for num, the default value of 3 is used (that is, it returns the 3 most popular names).
    """

    lst = sorted(names_dict, key = names_dict.get, reverse=True)[:num]
    return lst


def percent_captured(names_dict,threshold = 75):
    """
    Returns the number of names needed to have at least threshold percent of all the names in the dictionary. If no value is passed for percent, the default value of 75 is used (that is, it returns the number of names needed to have 75 percent (or more) of the total number of names).
    """
    total = sum([v for v in names_dict.values()])
    needed = total * threshold/100
    count = 0
    running_total = 0
    for w in sorted(names_dict, key = names_dict.get, reverse=True):
        if running_total >= needed:
            break;
        else:
            count += 1
            running_total += names_dict[w]
    return count
