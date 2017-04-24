#!/usr/bin/env python3

import re

def word_histogram(text):
    word_histogram = {}
    nameRegex = re.compile(r"\b[\w^_]+\b")
    words_list = nameRegex.findall(text)
    for i in words_list:
        lower = i.lower()
        number = word_histogram.get(lower, 0)
        word_histogram[lower] = number+1
    return word_histogram

if __name__ == "__main__":
    print(word_histogram("To be or not to be"))
