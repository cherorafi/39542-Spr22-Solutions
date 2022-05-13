"""
Q 1:  Return most common letter for each position
Name: Katherine St. John
Email: katherine.stjohn@hunter.cuny.edu
"""

def helper(words, pos):
    d = {}
    for w in words:
        if w[pos] in d.keys():
            d[w[pos]] += 1
        else:
            d[w[pos]] = 1
    print(sorted(d,key=d.get))
    return(max(d,key=d.get))

def wordle_count(data):
    words = data.split('\n')
    answer = ""
    print(words)
    for i in range(5):
        answer = answer + helper(words,i)
    return(answer)
