"""
CW 4:  Return the three largest numbers from the input
Name: Katherine St. John
Email: katherine.stjohn@hunter.cuny.edu
"""


def max3(data):
  s = data.replace('\n', ' ')
  words = s.split(' ')
  nums = []
  for w in words:
      if w != ' ' and w != '':
          nums.append(float(w))
  nums = sorted(nums)
  return(f"{nums[-1]} {nums[-2]} {nums[-3]}")
