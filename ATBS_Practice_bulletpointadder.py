#! /usr/bin/python3

# bulletpointadder.py - A programme for adding bullet points to any list

import pyperclip, sys

#Retrieves text from clipboard 
text = pyperclip.paste()

#Separates lines and adds stars.
lines = text.split('\n')

for i in range(len(lines)):
    lines[i] = '* ' + lines[i]

text = '\n'.join(lines)

#Returns to clipboard
pyperclip.copy(text)