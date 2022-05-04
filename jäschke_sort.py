import os, re, sys, traceback
from pathlib import Path
from os import listdir
from os.path import isfile, join, isdir
import time
import pyewts
from tibetan_sort.tibetan_sort import TibetanSort
from collections import namedtuple
import random

def find_page(query):
    for count,header in enumerate(tib_headers):
        if count + 1 == len(tib_headers):
            break
        ordered_list = sorter.sort_list([header,query,tib_headers[count+1]])
        if ordered_list == [header,query,tib_headers[count+1]]:
            return header

def sorter_test(ordered_headers_list):
    jumbled_headers_list = ordered_headers_list[:]
    random.shuffle(jumbled_headers_list)
    for x,y in zip(ordered_headers_list,sorter.sort_list(jumbled_headers_list)):
        message = ""
        if x != y:
            message = "failure"
        print(x,y,"\n",message)

headers_file = 'path_to_jäschke_headers.md'
tib_headers = []
with open(headers_file, "r") as file:
    lines = file.readlines()
    for line in lines:
        tib_text = re.search(r"\d+\.\s(.+?)(?:\s|\n)",line).group(1)
        tib_headers.append(tib_text)

# Real entries, real page numbers ; not used currently
test_word = namedtuple("test_word","word page")
test_words = [test_word("ཁ་གཔོ་",36),
test_word("གོང་མ་",72),
test_word("མགུར་ལྷ་",90),
test_word("བགྲོང་བ་",90)]

# Compare original list to randomized then sorted list
sorter = TibetanSort()
sorter_test(tib_headers)