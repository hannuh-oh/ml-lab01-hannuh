"""
Hannuh Grant
January 2020
1) Regular Expressions
Look at proj_01_08.py.  If you execute that in the console, it defines some variables.
Put a multiline comment in your Thursday.py for this section (start with " "" and end with "" ")
Copy paste these instructions in there.  (copy out everything highlighted)
Look through the "links" variable and see if you can find some image covers.
Edit Proj_01_08 to make the loop in proj_01_08 print out the path to the images for all of the book cover thumb images.

"""

from bs4 import BeautifulSoup
import requests
import re

# find a random set of gutenberg texts in english
# And parse it into beautiful soup!
startURL = 'https://www.gutenberg.org/ebooks/search/?sort_order=random&query=l.en'
r = requests.get(startURL)
soup = BeautifulSoup(r.text, "html.parser")
# find all the links in the gutenberg query.
links = soup.find_all("a", class_="link")
images = soup.find_all('img')
# Go through and build a list of the book numbers out of the matching links.
booknums = []
allimages = []
for i in images:
    regex = r".*/(\d+)"
    test_str = link.get('href')
    matches = re.match(regex, test_str, re.IGNORECASE)
    if matches:
        print(f"Matched: {matches[1]} - {test_str}")
        booknums.append(matches[1])
    else:
        print("no match: ", test_str)

booknums


for i in images:
    print(i)

