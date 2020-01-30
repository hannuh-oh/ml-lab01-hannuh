
"""
Lab set 01 - Project 01 - Re-acquainting with Python

01.02 - 10 pts.
"""

# First let's try reading in and displaying the sonnets.

# Read in the file for all the sonnets along with the header and footer garbage
filename = "wssnt10.txt"

with open(filename) as f:
    content = f.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line


content = [x.strip() for x in content]   # list comprehension !!!


# equivalent to...

content = []
for x in content:
    content.append( x.strip() )

# print the number of lines in the file
count = 0





# Print the entire sonnet file to the console, without the extra line breaks!







