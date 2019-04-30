"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here: 

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file

import os
foo = open('foo.txt')
for text in foo:
    print(text)
foo.close()

# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make 
# sure that it contains what you expect it to contain

newfile = open("bar.txt", "w+" or 'r')
for i in range(3):
    line = ("foobarfoobarfoobar")
    newfile.write(str(line) + '\n')
newfile.close()

bar = open("bar.txt")
for text in bar:
    print(text)
foo.close()