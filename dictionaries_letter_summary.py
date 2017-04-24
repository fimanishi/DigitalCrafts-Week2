#!/usr/env/bin python3

import string

def letter_histogram(text):
    dict_histogram = {}
    for i in text:
        lower = i.lower()
        if lower in string.ascii_lowercase:
            number = dict_histogram.get(lower, 0)
            dict_histogram[lower] = number + 1
    return dict_histogram

if __name__ == "__main__":
    print(letter_histogram("banana"))
