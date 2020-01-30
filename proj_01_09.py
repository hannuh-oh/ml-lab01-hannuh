

import requests
from bs4 import BeautifulSoup
import time
import re

def read_fileAsList( fname ):
    with  open(fname) as f:
        return [  (line[:-1] if line[-1] == "\n" else line) for line in f.readlines()]


def find_lineWithTextInList(direction, somelist,  sometext, startingPoint = None):
    if (startingPoint is None):
        i = len(somelist) // 2
    else:
        i = startingPoint
    while (i >= 0 and i < len(somelist)):
        if sometext is "" and somelist[i].strip() == "":
            # we have found a blank line, which is what we were looking for.
            return i
        elif sometext.lower() in somelist[i].lower():
            # we found the marker text.
            return i
        i = i + direction
    return False


def extract_GutenText(lines):
    startpoint1 = find_lineWithTextInList(-1, lines, "project gutenberg")
    startpoint2 = find_lineWithTextInList(1, lines, "", startpoint1)
    endpoint1 = find_lineWithTextInList(1, lines, "project gutenberg")
    endpoint2 = find_lineWithTextInList(-1, lines, "", endpoint1)
    result = lines[startpoint2+1: endpoint2]
    if len(result) == 0:
        raise ValueError("The text seems to be empty.  Maybe a marker is missing.")
    return result


def get_gutentextURLs() :
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
            #print(f"Matched: {matches[1]} - {test_str}")
            booknums.append(matches[1])
        else:
            #print("no match: ", test_str)
            pass

    baseURL = "https://www.gutenberg.org/ebooks/NNN.txt.utf-8"
    urls = [baseURL.replace('NNN', x) for x in booknums]
    return urls


def get_gutenTexts(numTexts = 2):
    # this with statement opens a large session
    # for making multiple requests. More efficient.
    urls = get_gutentextURLs()
    texts = []
    with requests.Session() as rsession:
        for url in urls:
            time.sleep(3)
            print(url)
            getresult = rsession.get(url)
            ## Insert code to split lines from the lab here.
            # remember the text of the result is getresult.text
            lines =  ????
            gutenText = extract_GutenText((lines))
            texts.append(gutenText)
            # quit once we exceed the allowed number of texts
            numTexts -= 1
            if numTexts == 0: return texts

    return texts


if __name__ == '__main__':
    texts = get_gutenTexts()



