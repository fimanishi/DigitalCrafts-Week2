#!/usr/bin/env python3

def dict_top3(d):
    top = list(d.values())
    top.sort(reverse=True)
    top = top[0:3]
    top3 = []
    for i in top:
        for key, value in d.items():
            if value == i:
                top = key
                d.pop(key)
                top3.append([key,value])
                break
    for i in range(1,4):
        print("Top" + str(i) + " is:", top3[i-1])

if __name__ == "__main__":
    dict_top3({'to': 3, 'be': 4, 'or': 6, 'not': 1})
