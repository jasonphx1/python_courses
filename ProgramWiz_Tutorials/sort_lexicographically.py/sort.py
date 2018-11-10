#!/usr/bin/env python3

#URL: https://www.programiz.com/python-programming/examples/alphabetical-order

my_str = "Hello this Is an Example With cased letters"

words = my_str.split()
words.sort()

print("The sorted words are:")
for word in words:
    print(word)
