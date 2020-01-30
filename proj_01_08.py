

import requests
from bs4 import BeautifulSoup

"""
1.  Go to project gutenberg home page and figure out what URL to use to get a page of random English texts.

Enter the URL you want to start with for the URL variable here.
"""

startURL = 'https://www.gutenberg.org/ebooks/search/?sort_order=random&query=l.en'

"""
It's best to explore web scraping possiblities in the CONSOLE, because you don't know what you're
looking for till you find it.

"""

r = requests.get(startURL)


Explore in the console:
r.status_code
r.text


soup = BeautifulSoup(r.text, "html.parser")

soup.find_all("a")
soup.find_all("a",  class_="link")
len(soup.find_all("a",  class_="link")) 

#try the first
first = soup.find_all("a", class_="link")[0]
print(first)
# try the third - named generically.
somelink = soup.find_all("a", class_="link")[3]
print(somelink)



#
# Regular Expressions
# Try different test strings and run this code...
# In the console.
# Try out different patterns and test strings!
# Leave your own experimentation in here.
#

import requests


# an r-string is specifically for regular expressions.
regex = r".*/(\d+)"
test_str = "ebooks/12345x"
matches = re.match(regex, test_str, re.IGNORECASE)
# there are different regular expression match functions.  search and findall are commonly used.
# match always starts at the beginning of the string.
# search looks through the string for the first match.
# findall returns a list of all the search matches.
# print out the first match group.  The zeroeth match group is the entire matched string....
if matches:
    print("Match of digit part is: ", matches[1])


from bs4 import BeautifulSoup

# find a random set of gutenberg texts in english
# And parse it into beautiful soup!
startURL = 'https://www.gutenberg.org/ebooks/search/?sort_order=random&query=l.en'
r = requests.get(startURL)
soup = BeautifulSoup(r.text, "html.parser")
# find all the links in the gutenberg query.
links = soup.find_all("a", class_="link")
# Go through and build a list of the book numbers out of the matching links.
booknums = []
for link in links:
    regex = r".*/(\d+)"
    test_str = link.get('href')
    matches = re.match(regex, test_str, re.IGNORECASE)
    if matches:
        print(f"Matched: {matches[1]} - {test_str}")
        booknums.append(matches[1])
    else:
        print("no match: ", test_str)

booknums

