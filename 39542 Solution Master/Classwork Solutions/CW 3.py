"""
Name: Katherine St. John
Email: katherine.stjohn@hunter.cuny.edu
Resources:  Used DS100 textbook to look up pandas syntax.
I attended lecture today.
Row: Podium/Front
Seat: 1
"""

import pandas as pd

in_file = input("Enter a input file name: ")
out_file = input ("Enter an output file name: ")

df = pd.read_csv(in_file)

#Select 3rd graders, column stores values as strings:
df = df[ df['Grade'] == '3' ]
#Select 2019 data:
df = df[ df['Year'] == 2019 ]
df.to_csv(out_file, index=False)
