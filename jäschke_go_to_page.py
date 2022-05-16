import tk
import os
import re
import sys
import traceback
import easygui
from pathlib import Path
from os import listdir
import time
import pyewts
from tibetan_sort.tibetan_sort import TibetanSort
from collections import namedtuple
import random
import applescript


def abort(message):
    exc = traceback.format_exc()
    print(exc + message)
    sys.exit()


def Skim_go_to_page(dic_page):
    offset = 26  # difference between number of pages in PDF and real page numbers in dictionary
    scpt = f'''
        tell application "Skim"
            tell document 1

               go to page {dic_page + offset}
            end tell
        end tell'''
    r = applescript.run(scpt)


def find_closest_header_page(query, tib_list):
    if not query.endswith("་"):
        query += "་"
    if query in tib_list:
        offset = 1
    else:
        offset = 0
    return sorter.sort_list(tib_list + [query]).index(query) + offset


def sorter_test(ordered_headers_list):
    jumbled_headers_list = ordered_headers_list[:]
    random.shuffle(jumbled_headers_list)
    jumbled_headers_list = sorter.sort_list(jumbled_headers_list)
    range_list_length = range(len(ordered_headers_list))
    for count, x, y in zip(
            range_list_length, ordered_headers_list, jumbled_headers_list):
        message = ""
        if x != y:
            message = "failure"
        print(count, x, "|||", y, "|||", message)


def wordlist_test():
    test_word = namedtuple("test_word", "word page")
    test_words = [test_word("ཁ་ག་པོ་", 36),
                  test_word("གོང་མ་", 72),
                  test_word("མགུར་ལྷ་", 90),
                  # a real header with its real page
                  test_word("བགྲོང་བ་", 90),
                  test_word("ཚ་འཁྲུ་", 442),
                  test_word("ཚང་ངུ", 444)]
    for test_word in test_words:
        closest_header_page = find_closest_header_page(
            test_word.word, tib_headers_no_wasurs)
        print(test_word.page, closest_header_page)


def remove_wasur(tib_string):
    tib_string_bytes = tib_string.encode('utf-8')
    return tib_string_bytes.replace(b'\xbe\xad\xe0', b'').decode("utf-8")

sorter = TibetanSort()
home = str(Path.home())
txt_file = os.path.join(
    home,
    "Documents",
    "Code",
    "tib_dic_utilities",
    "jäschke_headers.md")

tib_headers = []
try:
    with open(txt_file, "r") as file:
        lines = file.readlines()
        for line in lines:
            tib_text = re.search(r"\d+\.\s(.+?)(?:\s|\n)", line).group(1)
            tib_headers.append(tib_text)
except BaseException:
    abort(f"{txt_file}|{line}")

# Get list of headers without wasur
tib_headers_no_wasurs = []
for header in tib_headers:
    tib_headers_no_wasurs.append(remove_wasur(header))

query = easygui.enterbox("Tibetan word to be found.")
page = find_closest_header_page(query, tib_headers_no_wasurs)
Skim_go_to_page(page)