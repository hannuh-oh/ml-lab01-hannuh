"""
Lab 01  Project 01-04.  extract_gutenText

Write the function extract_gutenText here and let's test it out!

So we'll also be writing a test function for this one.
"""

#  Copy and paste your code here from previous exercise:

def read_fileAsList( fname ):
    with  open(fname) as f:
        return [  (line[:-1] if line[-1] == "\n" else line) for line in f.readlines()]

# optional 01.06.  You can come back and do this LATER.
def find_lineWithTextInList(direction, somelist,  sometext, startingPoint = None):
    pass


# 01.05 - do this before 01.06.
def my_extract_GutenText(lines):
    # Look for "project gutenberg" before the mid point
    # I am including some sample code to get you started.....
    # Make sure you understand what this does BEFORE you copy it and modify it for below.
    # Also it's incomplete....
    startpoint1 = len(lines) // 2   # note the integer division.
    try:
        while startpoint1 >= 0:
            if "project gutenberg" in lines[startpoint1].lower():
                break
            startpoint1 = startpoint1 - 1 # or alternatively:  startpoint1 -= 1
    except IndexError as e:
        # we had a an index out of bounds problem in the above code.
        print("Error error - bounds error in finding start point!")  # in general it's not a good idea to print in your exceptions.
        startpoint1 = 0

    # look for the first blank line after that point.
    startpoint2 = startpoint1
    while startpoint2 >= startpoint1:
        if lines[startpoint2].strip() == "":
            break
        startpoint2 += 1
    # look for "project gutenberg" after the midpoint
    startpoint3 = len(lines) // 2
    while startpoint3 <= len(lines):
        if "project gutenberg" in lines[startpoint2].lower():
            break
        startpoint3 += 1
    # look for the first blank line before that point
    startpoint4 = startpoint3
    while startpoint4 <= len(lines):
        if "" in lines[startpoint2].lower():
            break
        startpoint4 += 1

    result = lines.trim()
    """
    a slice of the list that is just the text of the ebook.  Don't include the blank lines in the slice
    """
    if len(result) == 0:
        raise ValueError("Book is empty. May not have the right start and end markers.")
    return result


# Part 01.07 -
# Mars wrote this test FOR you.... pay particular attention to the notes in the lab
# and how it works!
# Especially string join, f-strings, assert.
#
# DO NOT GO ON if you don't understand how those work!
#

def extract_GutenText(lines):
    try:
        startpoint1 = find_lineWithTextInList(-1, lines, "project gutenberg")
        startpoint2 = find_lineWithTextInList(1, lines, "", startpoint1)
        endpoint1 = find_lineWithTextInList(1, lines, "project gutenberg")
        endpoint2 = find_lineWithTextInList(-1, lines, "", endpoint1)
    except:
        raise ValueError("the text is empty")
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





def test_basic_extract_GutenText():
    print("dude")
    texttext1 = """This is a test example
    *** Project GUTENberg should start here after the blank line ***
    *** and not include this line or the blank line after this one **
    
    guten text is here!
    
    ** some nonlank line **
    *** Project GutenBERG text should end here but the blank line before it should also not be included ***
    ** none of this should show up
    """
    testtextlines = texttext1.split("\n")
    actualtextlines = extract_GutenText(testtextlines)
    assert len(actualtextlines) == 1, f'Incorrect number of lines for testtext1: {len(actualtextlines)} should be 1. {"|".join(actualtextlines)}'
    assert actualtextlines[0] == "guten text is here!", f"testtext1 is wrong: {'|'.join(actualtextlines)}"


""" 
This SHOULD raise an exception - specifically a ValueError.
"""
from nose.tools import *
@raises(ValueError)

def test_empty_GutenText():
    text = """This text has no marker for start or end of book.""".split("\n")
    lines = extract_GutenText(text)  # This should throw an exception.  And Nose is expecting a "ValueError" exception.

def test_noGutenText():
    noGutenText = ""
    someGutenText = extract_GutenText(noGutenText)
    

