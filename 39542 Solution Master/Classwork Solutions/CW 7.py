"""
Name: Katherine St. John
Email: katherine.stjohn@hunter.cuny.edu
Resources: used textbook for regex and pandas documentation for setting up DataFrames.
"""

import pandas as pd
import re

infile = input("Enter input file name: ")
outfile = input("Enter output file name: ")


#Use read() so that the whole file is in one string:
data = open(infile).read()
print(data)

#Make one massive pattern with groups (surrounded by parens) for links and titles
#   group 0:  <a href= "http://
#   group 1:  contains the url (without quotes)
#   group 2:  ">
#   group 3:  contains title
#   group 4:  </a>
pattern = r'(<a href=\s*\"https?://)([\w\.\-/]+\w)(/?\w*\"\s*>)([\w\-\s]+)(</a>)'
links = re.findall(pattern,data)
print(len(links))


#Pull out the urls and titles from the tuples found in links:
urls = [x[1] for x in links]
titles = [x[3] for x in links]

#Set up the DataFrame and save to the outfile:
df = pd.DataFrame({ "Title" : titles, "URL" : urls })
df.to_csv(outfile,index=False)
