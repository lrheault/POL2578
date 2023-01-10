#!/usr/bin/env python
# coding: utf-8

# <h1> POL2578.  Classes 1-2.  Introduction to Python.</h1>
# 
# During the first two classes, we will gain familiarity with the Python programming language. In particular, we will cover the key building blocks of programming languages and see how they are handled in Python.
# 
# We will cover the following themes:
# <ol>
# <li> Introductory words on strings and encodings.</li>
# <li> Data types: integers, floating-point numbers and strings. </li>
# <li> Lists, tuples and dictionaries. </li>
# <li> Loops and conditional statements. </li>
# <li> Input/Output. </li>
# <li> Functions. </li>
# <li> Classes. </li>
# <li> Exercises with handling file formats. </li>
# </ol>
# 
# <h2>Introductory words on strings and encodings</h2>
# 
# We will use the <b>Jupyter</b> notebook for examples during class (based on iPython). This is a popular and modern approach to write code in Python.  It allows to combine formatted comments, input code and output in a single document.
# 
# For starters, we will look at how <b>Python</b> processes strings (textual characters) and encodings.
# 
# Unlike low-level languages, Python recognizes a string without the need to declare it when we use the quotation marks.  For instance:
# 
# 
# 

# In[ ]:


x = "This is a sentence."
print(x)


# Notice that we can use the single, double or triple quotes; we only need to be consistent in our usage, i.e. closing the quote with the same type we use to open it.

# In[ ]:


y = 'Hello, World!'
print(y)


# Python 3 uses the unicode standard by default to encode strings. This is what we want. But you may face situations where a document was encoded using an older standard. Here's an example. Suppose someone sends you the file gazette.txt, an article from The Gazette. The below may cause an error on Mac or Linux systems. On a Windows OS, it should open fine. However, Windows does not use unicode as default, and users may need to specify the encoding, which I will do for the examples in this class.

# In[ ]:


f = open('gazette.txt')
text = f.read()
f.close()


# Specifically, the file was encoded with the ISO-8859-1 standard. It contains accents. We can open it properly by specifying the encoding. Here, "latin" is an alias for that encoding.

# In[ ]:


f = open('gazette.txt', encoding='latin')
text = f.read()
f.close()

print(text)


# On Mac or Linux, files will be saved in unicode by default. 
# 
# For cross-platform consistency, I will specify the encoding when opening files.

# In[ ]:


g = open('gazette_unicode.txt', 'w', encoding='utf-8')
g.write(text)
g.close()


# In[ ]:


f = open('gazette_unicode.txt', encoding='utf-8')
text = f.read()
f.close()

print(text)


# These types of problems are less and less frequent, given that most people have moved to unicode as the new standard.
# 
# Again, if the document uses unicode, it won't be a problem. Even this Jupyter page is utf-8 encoded. For instance:

# In[ ]:


text = '緁 榃痯痻 彃慔慛 噅尰崺 圁垺,槄 鞿鬖 裌覅詵 裺觨誖 鈖嗋圔'
print(text)


# If running into troubles, you may find the full list of encodings supported in Python here: https://docs.python.org/3/library/codecs.html#standard-encodings

# <h2> Data types </h2>
# 
# The most common data types in programming are:
# <ul>
# <li> Integers </li>
# <li> Floating-point numbers </li>
# <li> Characters (strings) </li>
# </ul>
# 
# A particularity of Python is that there is no need to define the type of a new variable.  The interpreter will recognize and assign a type automatically.  
# 
# We define a variable, no matter their type, with the equal sign.  Values are assigned to objects. For instance, we can assign the integer 5 to an object we want to call x as follows:

# In[ ]:


x = 5


# Type the name of an object to display its value:

# In[ ]:


x


# Again, to know the type assigned to an object, use the <b>type</b> function.

# In[ ]:


type(x)


# Basic mathematical operations can be performed with this new object x.

# In[ ]:


print(x + 2) # Addition.
print(x - 2) # Subtraction.
print(x * 2) # Multiplication.
print(x ** 2) # Exponentiation.
print(x / 2) # Division.
print(x % 2) # Modulus (remainder of a division).


# To declare a floating point number, add a decimal.

# In[ ]:


x = 5.0


# In[ ]:


type(x)


# The type we're especially interested in for this course is the string type, which contains  characters.

# In[ ]:


x = 'Joe'


# In[ ]:


x


# In[ ]:


type(x)


# Manipulating strings in Python is very easy, making the language ideal for text processing.  
# 
# For instance, concatenate strings with the addition simple:

# In[ ]:


y = 'Biden'
print(x + ' ' + y)


# Modifications are usually not "in place" by default; you need to reassign values to an object if they are to be used later.

# In[ ]:


x = x + ' ' + y
print(x)


# We can select characters from a string using indexes.   The usage is object[i:j] for subsetting the characters from position i to j exclusive, i.e. to j-1.  
# 
# Importantly, note that Python is <b>0-based</b>.
# 
# For instance, get characters 0 to 5 with x[0:6]:

# In[ ]:


x[0:6]


# For the first n characters, use object[:n], which is implicitly x[0:n]. 

# In[ ]:


x[:2]


# For the last n characters, use object[-n:].

# In[ ]:


x[-3:]


# There is a number of built-in methods (functions) for strings, which are very useful for everything we do in this course. Here are some of them:
# 
# <ul>
# <li> Capitalize first letter: object.capitalize() </li>
# <li> Convert all to lower case: object.lower() </li>
# <li> Convert all to upper case: object.upper() </li>
# <li> Find if a substring/character is present: object.find(substring) </li>
# <li> Replace a substring/character within a string: object.replace(substring, replacement) </li>
# <li> Split a string based on a delimiter: object.split(delimiter) </li>
# </ul>

# In[ ]:


'joe'.capitalize()


# In[ ]:


x.lower()


# In[ ]:


x.upper()


# In[ ]:


x.find('Biden')


# In[ ]:


x.startswith('J')


# In[ ]:


x.replace('Biden','Brown')


# In[ ]:


x.split()


# In[ ]:


'     Annoying white space on the left.'.lstrip()


# In[ ]:


'Annoying white space on the right.        '.rstrip()


# In[ ]:


'    Annoying white space on both sides!    '.strip()


# <h2> Lists, Tuples and Dictionaries </h2>
# 
# <h3> Lists </h3>
# 
# The most "Pythonic" of all object types is the <b>list</b>.  Lists are used all the time, and are declared using squared brackets.  Lists give Python its own identity; they are incredibly powerful and useful, as we will see below.

# In[ ]:


x = ['Joe', 1, 2.0, 'maybe']


# In[ ]:


x


# In[ ]:


len(x)


# In[ ]:


for item in x:
    print(item)


# In[ ]:


x[0]


# In[ ]:


x[1]


# In[ ]:


type(x[0])


# In[ ]:


type(x[1])


# In[ ]:


x.append('Trudeau')
x


# In[ ]:


x = 'This is a sample sentence'.split()
x


# In[ ]:


x = 'This is a first sentence. And a second one in the same string.'.split('. ')
x


# <b>List comprehensions</b> allow you to loop over the elements of a list intuitively and efficiently.

# In[ ]:


x = 'This is a sample sentence'
x = x.split()
x = [item.lower() for item in x]
x


# In[ ]:


y = [item for item in x if item.startswith('s')]
y


# Looping through a list using a for loop is very intuitive as well.  Notice that Python does not use a numerical index by default.

# In[ ]:


for i in x:
    for j in y:
        print(i + ' ' + j)


# To loop with an index the traditional way, as in C and other languages, we can use the enumerate function.

# In[ ]:


for i, element in enumerate(x):
    print(i, element)


# <h3> Tuples </h3>

# In[ ]:


x = ('Kamala', 'Harris')
x


# In[ ]:


for item in x:
    print(item)


# Tuples within a list:

# In[ ]:


y = [x, ('Hillary', 'Clinton')]
y


# In[ ]:


for firstname, lastname in y:
    print(firstname + ' ' + lastname)


# <h3> Dictionaries </h3>

# In[ ]:


x = {'First Name' : 'Joe', 'Last Name': 'Biden', 'Age' : 80, 'Location': 'Delaware'}
print(x)


# We can get the value corresponding to an key using the square brackets, as follows:

# In[ ]:


x['First Name']


# In[ ]:


x['Age']


# However, the best way to get values from a dictionary is with the method "get"; the second argument to get is what to return if the key is not in the dictionary:

# In[ ]:


x.get('First Name')


# In[ ]:


x.get('Party')


# In[ ]:


x.get('Party', 0)


# In[ ]:


x.get('Party', 'Unknown')


# We can replace values within a dictionary as follows:

# In[ ]:


x['Age'] = 70
print(x)


# Loop through the items of a dictionary using the items() method:

# In[ ]:


for key, value in x.items():    
    print(key + ': ' + str(value))


# We can also create an object using dictionary comprehension, as follows. 

# In[ ]:


{word:nb for word,nb in [('one',1),('two',2),('three',3)]}


# Dictionaries are useful for many reasons.  It allows to store data on specific attributes of an item (the 'keys'), and join the values of those attributes together.  Also, the JSON format, one of the most popular to transfer large amounts of data online, is constructed like a dictionary.
# 
# A dictionary can be used to <b>map</b> keys to values, in order to transform a dataset in a desired format efficiently.  Here's an example:

# In[ ]:


sentiment = {'happy' : 'positive', 
             'joyful' : 'positive',
             'content' : 'positive',
             'sad' : 'negative',
             'depressed' : 'negative',
             'frustrated' : 'negative'}


# In[ ]:


sentiment.keys()


# In[ ]:


sentiment.values()


# In[ ]:


s1 = 'i am very happy to hear that'
s2 = 'this is so sad it makes me feel depressed'


# In[ ]:


sent1 = [sentiment.get(word) for word in s1.split()]
print(sent1)
print(sent1.count('positive'))
print(sent1.count('negative'))


# There are many ways to use a dictionary with text documents.

# In[ ]:


sum(1 for word in s1.split() if sentiment.get(word)=='positive')


# In[ ]:


sent2 = [sentiment.get(word) for word in s2.split()]
print(sent2)
print(sent2.count('positive'))
print(sent2.count('negative'))


# In[ ]:


sentscores = []
for sentence in [s1, s2]:
    tokens = sentence.split()
    sentwords = [sentiment.get(word,0) for word in tokens]
    score = (sentwords.count('positive') - sentwords.count('negative'))/len(tokens)
    sentscores.append(score)


# In[ ]:


sentscores


# In[ ]:


for i, score in enumerate(sentscores):
    print(f"Sentence {i+1} has a sentiment score of: {score:0.3f}.")


# <h3> Data Frames </h3>
# 
# R users may be familiar with the data frame type, which is a spreadsheet-like arrangement of a dataset.
# 
# Python has the equivalent in the form of the very efficient <i>pandas</i> library.

# In[ ]:


import pandas as pd

x = pd.DataFrame({'variable1' : [1, 2, 3], 'variable2' : [4, 5, 6]})
x


# In[ ]:


x.variable1[0]


# In[ ]:


x.variable2[1]


# <h3> Loops and conditional statements </h3>
# 
# Python has a very lean and simplified structure for loops and conditional statements, close to English language.  In particular, Python does not require brackets and literally uses 'and' and 'or' as boolean operators (rather than && and ||).
# 
# Importantly, recall to use the same type of indentation (tab or 4 spaces) consistently.  This is the only clue that the interpreter has to understand your code. 
# 
# If you get an indentation error, revise the indents you used and make sure they are consistent.

# In[ ]:


x = [92, 109, 4, 'Canada is a country', 
         'Quantum computing is the future', 12, 17, 52, 
         'I currently live in Canada']


# In[ ]:


for item in x:
    if type(item)==str and 'Canada' in item:
        print(item)


# In[ ]:


for item in x:
    if type(item)==str and 'Canada' not in item:
        print(item)


# In[ ]:


x = 1
while x < 6:
    print(x)
    x+=1


# <h3> Input/Output </h3>
# 
# Input/Output is a key component to learn when becoming familiar with a new language. We'll need to spend some time to cover all the possible formats later one, but let's see how it works.
# 
# First, you can check the working directory with:

# In[ ]:


import os

os.getcwd()


# If you wanted to set the working directory to something else, then do the following:
# <code>
# import os
# os.chdir('new_path')
# </code>
# 
# The os and sys packages contain most of the tools to communicate with your Operating System and perform advanced input/output operations.
# 
# For instance, os.dirlist(path) will list the files contained in the specified path.

# In[ ]:


default_path = os.getcwd()
filelist = os.listdir(default_path)

for f in filelist:
    print(f)


# As you can see, the list is unordered.  If order matters, enclose the expression within sorted()

# In[ ]:


filelist = sorted(os.listdir(default_path))

for f in filelist:
    print(f)


# Now, suppose there's a file on your computer called 'example.txt'.  The open function is a pointer to that file.

# In[ ]:


f = open('example.txt', encoding='utf-8')


# In[ ]:


f


# In[ ]:


f.read()


# Reading it a second time won't work:

# In[ ]:


f.read()


# In[ ]:


f


# In[ ]:


f.seek(0)
f.read()


# In[ ]:


f.close()


# A more common way to write Python code, consistent with this behaviour, is to use the with statement:

# In[ ]:


with open('example.txt', encoding='utf-8') as f:
    text = f.read()
text


# If the lines correspond to relevant units of texts (they often are), i.e. documents, then we can split them by line as follows:

# In[ ]:


with open('example.txt', encoding='utf-8') as f:
    text = f.read().splitlines()
text


# In[ ]:


for document in text:
    print(document)
    print()


# There is a csv library that can be used to write and load spreadsheet-like files.

# In[ ]:


document_numbers = [1,2,3]
document_tags = ['Some Value', 'Some Other Value', 'Yet Another Value']


# In[ ]:


dataset = zip(document_numbers, text, document_tags)


# Note that the zip function above creates an iterator.  It will be "exhausted" after one use.

# In[ ]:


import csv

with open('example_spreadsheet.csv', 'w', encoding='utf-8', newline='') as fout:
    w = csv.writer(fout)
    w.writerow(('docnumber','text','values'))
    for d, t, v in dataset:
        w.writerow((d, t, v))  


# I recommend using <b>pandas</b> instead to handle spreadsheets:

# In[ ]:


import pandas as pd

df = pd.read_csv('example_spreadsheet.csv', delimiter=',', header=0)


# In[ ]:


df


# In[ ]:


text = df.text.tolist()


# In[ ]:


print(text)


# <h3> Functions </h3>

# In[ ]:


def remove_words(text):
    words_to_remove = ['Canada','bill','government','law']
    text = text.split()
    text = [w for w in text if w not in words_to_remove]
    text = ' '.join(text)
    return text


# In[ ]:


x = 'i proudly introduce this bill in the name of our government'
x


# In[ ]:


remove_words(x)


# <h3> Classes </h3>
# 
# Python is an object-oriented language and classes represent a fundamental component for this type of languages.

# In[ ]:


class NlpStudents:
    
    def __init__(self, firstname, lastname, age):
        self.age = age
        self.fname = firstname
        self.lname = lastname
    
    def word_transform(self,text):
        self.text = text
        return self.text.lower()
    
    def print_name(self):
        print(self.fname + ' ' + self.lname)


# In[ ]:


johnny = NlpStudents('John', 'Doe', 29)


# In[ ]:


type(johnny)


# In[ ]:


johnny.age


# In[ ]:


johnny.word_transform('Canada')


# In[ ]:


johnny.print_name()


# <h3> Handling common file formats for textual data </h3>
# 
# We've seen how to load a text file and spreadsheet-like files, two common formats.  But there are other formats used to store and disseminate textual data.  These are:
# 
# <ol>
# <li> The e<b>X</b>tensible <b>M</b>arkup <b>L</b>anguage (xml); </li>
# <li> The <b>H</b>yper<b>T</b>ext <b>M</b>arkup <b>L</b>anguage (html); </li>
# <li> The <b>J</b>ava<b>S</b>cript <b>O</b>bject <b>N</b>otation (JSON); </li>
# <li> SQL databases. </li>
# </ol>
# 
# The JSON format is becoming popular to share large dataset online.  It is the easiest one to use, so we'll focus mostly on the two trickier ones: xml and html.
# 
# SQL is a database management system, widely used on servers.  It's probably the format you'll want to learn to prepare for the business world.  Covering this topic would require some more time.  We may come back to it at the end of the course, only if time permits.

# <h4> Coming to grips with XML </h4>
# 
# There are many libraries to parse xml and html files in Python.  For simplicity, we will concentrate on one of those libraries: lxml.
# 
# Consider the example file from the British parliamentary debates.
# 
# The lazy way to parse is to identify the element we want and select the appropriate path with the xpath function in lxml.

# In[ ]:


import lxml.etree as etree


# First we recover the xml tree (structure) by parsing the xml file, using the etree.parse class.

# In[ ]:


with open('uk.proc.d.2013-12-11.xml', encoding='utf-8') as f:
    parsedf = etree.parse(f)
parsedf


# The resulting object is a parsed tree pointer for extracting information.  
# 
# Dealing with xml data is not always intuitive, which is why other formats have become more popular.  In practical terms, what you probably want to achieve is the following:
# 
# <ol>
# <li> Finding the tag(s) of interest, e.g. the one that delimit the text and/or the attributes contained within tags. </li> 
# <li> Verifying if the xml file uses a customized namespace, in which case you will need to do one of two things: </li>
# <ul>
# <li> Extract information about namespaces and declare it. </li>
# <li> Remove the namespace markers to bypass the namespaces. </li>
# </ul>
# <li> Loop through the file and extract information contained in the tags of interest. </li> 
# </ol>
# 
# For illustration, let's extract speeches and names from the UK parliament xml files.  It may help to visualize all the tags used in the file to identify where is the information we want, and that we don't want.  The following does just that.

# In[ ]:


taglist = [child.tag for child in parsedf.iter()]    
for tag in sorted(set(taglist)):
    print(tag)


# This illustrates an xml file with pre-defined namespaces: there is an {}-expression before the tag names.

# The key here is to declare the namespace.  In this case, we saw the namespace designation in the curly brackets. 

# In[ ]:


# We declare the namespace:
ns = {"pm":"http://www.politicalmashup.nl"}

speeches = []
# We specify the namespace everytime we use xpath:
speechtags = parsedf.xpath('.//pm:speech', namespaces=ns) 
for s in speechtags:
    speech = etree.tostring(s,method="text",encoding="unicode",pretty_print=True)
    speeches.append(speech)

print(len(speeches))
print(speeches[0].strip())


# In[ ]:


speeches = []
speakernames = []

for s in speechtags:
    speech = etree.tostring(s,method="text",encoding="unicode",pretty_print=True)
    name = s.xpath('@pm:speaker',namespaces=ns)[0]
    speeches.append(speech)
    speakernames.append(name)

print(speakernames[0])
print(speeches[0].strip())


# <h4> Parsing HTML </h4>
# 
# Parsing html files follows the same steps.  However, we normally won't have to care about namespaces.  The usage of tags follows standard conventions.  For instance, the text content of a website is usually located within the &lt;body&gt; tag and may have &lt;p&gt; tags interspersed.  Or we may want to extract items from a list contained within the common &lt;ol&gt; or &lt;ul&gt; tags.  As with xml, the data may be malformed. 
# 
# Beautiful Soup is a Python library that attempts a "universal" approach to clean and extract information from html files.  It'll usually work well, in most cases.  lxml can also be used to parse html. 

# In[ ]:


from bs4 import BeautifulSoup

with open('about_library.html', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f, 'lxml')


# In[ ]:


text = soup.find('article', {"about" : "/about"})
text


# In[ ]:


text.getText()


# In[ ]:


text.getText().split('\n')


# In[ ]:


library_text = text.getText().split('\n')
library_text = [line for line in library_text if line.strip()!='']
library_text


# <h4>The JSON format</h4>
# 
# JSON, on the other hand, is very simple.  It is simply a dictionary.  If you have multiple lines with one tweet in JSON format per line, load all the file, split the lines, and then parse the JSON objects.
# 
# Let's consider this example of data obtained from the Twitter Stream API.

# In[ ]:


import json

with open('tweets-sample.txt') as f:
    tweet_stream = f.read().splitlines()

tweet = json.loads(tweet_stream[0])
print(tweet['text'])
print(tweet['user']['screen_name'])


# In[ ]:


print(tweet_stream[0])


# In[ ]:


for line in tweet_stream:
    if line:
        tweet = json.loads(line)
        text = tweet['text']
        user = tweet['user']['screen_name']
        print(user + ': ' + text)
        print()


# In[ ]:


import html

for line in tweet_stream:
    if line:
        tweet = json.loads(line)
        text = tweet['text']
        user = tweet['user']['screen_name']
        print(html.unescape(text))


# In[ ]:


for line in tweet_stream:
    if line:
        tweet = json.loads(line)           
        if 'extended_tweet' in tweet:
            text = tweet['extended_tweet']['full_text']
        else:
            text = tweet['text']
        user = tweet['user']['screen_name']
        print(html.unescape(text))


# In[ ]:


for line in tweet_stream:
    if line:
        tweet = json.loads(line)
        if 'retweeted_status' in tweet:
            if 'extended_tweet' in tweet['retweeted_status']:
                text = tweet['retweeted_status']['extended_tweet']['full_text']
            else:
                text = tweet['retweeted_status']['text']
        else:
            if 'extended_tweet' in tweet:
                text = tweet['extended_tweet']['full_text']
            else:
                text = tweet['text']
        user = tweet['user']['screen_name']
        print(html.unescape(text)) 


# In[ ]:


# The newline argument is needed for Windows only.

with open('my_tweets.csv', 'w', encoding='utf-8', newline='') as fout:
    writer = csv.writer(fout)
    writer.writerow(('user','tweet'))
    for line in tweet_stream:
        if line:
            tweet = json.loads(line)
            if 'retweeted_status' in tweet:
                if 'extended_tweet' in tweet['retweeted_status']:
                    text = tweet['retweeted_status']['extended_tweet']['full_text']
                else:
                    text = tweet['retweeted_status']['text']
            else:
                if 'extended_tweet' in tweet:
                    text = tweet['extended_tweet']['full_text']
                else:
                    text = tweet['text']
            user = tweet['user']['screen_name']
            writer.writerow((user, html.unescape(text)))


# Of course, we can take advantage of using a programming language and write a function that will parse the tweets as we want.  Once defined, we can invoke that function on the fly and process the Tweets within the same script.

# In[ ]:


def tweet_parser(tweet_object):
    tweet = json.loads(tweet_object)
    if 'retweeted_status' in tweet:
        if 'extended_tweet' in tweet['retweeted_status']:
            text = tweet['retweeted_status']['extended_tweet']['full_text']
        else:
            text = tweet['retweeted_status']['text']
    else:
        if 'extended_tweet' in tweet:
            text = tweet['extended_tweet']['full_text']
        else:
            text = tweet['text']
    user = tweet['user']['screen_name']
    return (user, text)


# In[ ]:


for line in tweet_stream:
    if line:
        user, text = tweet_parser(line)
        print(user)
        print(html.unescape(text))


# This concludes our tour of the Python programming language.  We will have opportunities to work with all sorts of scripts later on, and to learn libraries specific to NLP. 
# 
# An advantage of Python is its simplicity and the very large community of users.  For most questions that you may have, the answer is already there on StackOverflow.  
