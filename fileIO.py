#!/usr/bin/env python3

from dictionaries_word_summary import word_histogram
from dictionaries_letter_summary import letter_histogram

def input_file_read():
    user_input = input("Enter file name: ")
    file_location = "/Users/laurenkim/code/py-exercises/" + user_input
    with open(file_location) as file:
        contents = file.read()
    return contents

def input_file_write():
    user_input = input("Enter file name: ")
    contents = input("Enter content: ")
    file_location = "/Users/laurenkim/code/py-exercises/" + user_input
    with open(file_location, "w") as file:
        file.write(contents)

def crash_test():
    with open("/Users/laurenkim/code/py-exercises/crash_test.txt", "w") as file:
        counter = 0
        while True:
            file.write("1"*100)
            print(counter)
            counter+= 100

def read_plot(filename):
    import json
    import matplotlib.pyplot as plot
    with open("/Users/laurenkim/code/py-exercises/" + filename) as file:
        data = json.load(file)
    x = []
    y = []
    for i in data["data"]:
        x.append(i[0])
        y.append(i[1])
    plot.plot(x,y)    
    plot.show()




def main():
    contents = input_file_read()
    word = word_histogram(contents)
    letter = letter_histogram(contents)
    print(word)
    print(letter)


if __name__ == "__main__":
    read_plot("test.json")
