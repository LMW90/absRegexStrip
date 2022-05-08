#! python3
# using regex strip whitespace from a string in same manner as strip() method does
import re
import pyperclip as pc
lstrip = re.compile(r'(^\s*)')
rstrip = re.compile(r'(\s*$)')
text = pc.paste()
text = lstrip.sub('', text)
text = rstrip.sub('', text)
pc.copy(text)