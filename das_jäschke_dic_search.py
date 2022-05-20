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


def Skim_go_to_page(dic_name, dic_page, offset=0):
    scpt = f'''
        tell application "Skim"
            set p to documents
            repeat with i from 1 to count p
                if the name of p's item i begins with "{dic_name}" then set doc_counter to i
            end repeat
            tell document doc_counter
               go to page {dic_page + offset}
            end tell
        end tell'''
    r = applescript.run(scpt)


def find_closest_header_page(query, dic_name):
    '''
    func for Das's dic.
    '''
    if dic_name == "Jäschke":
        headers = jaschke_headers
    elif dic_name == "Das":
        headers = das_headers
    if not query.endswith("་"):
        query += "་"
    if query in [x.word for x in headers]:
        offset = 0
    else:
        offset = -1
    index = sorter.sort_list(
        [x.word for x in headers] + [query]).index(query) + offset
    return int(headers[index].page)


def sorter_test(ordered_headers_list):
    jumbled_headers_list = ordered_headers_list[:]
    random.shuffle(jumbled_headers_list)
    jumbled_headers_list = sorter.sort_list(
        x.word for x in jumbled_headers_list)
    range_list_length = range(len(ordered_headers_list))
    for count, x, y in zip(
            range_list_length, ordered_headers_list, jumbled_headers_list):
        message = ""
        if x.word != y:
            message = "failure"
        print(count, x, "|||", y, "|||", message)


def wordlist_test():
    test_words_J = [tibWord("ཁ་ག་པོ་", 36),
                    tibWord("གོང་མ་", 72),
                    tibWord("མགུར་ལྷ་", 90),
                    tibWord("བགྲོང་བ་", 90),
                    tibWord("ཚ་འཁྲུ་", 442),
                    tibWord("ཚང་ངུ", 444)]
    test_words_D = [tibWord("བསམ་བྱ་", 1317),
                    tibWord("ལ་པ་ཤ་", 1201),
                    tibWord("དད་འདུན་", 617),
                    tibWord("པོ་ཏ་ལ་", 785),
                    tibWord("མང་བ་", 952),
                    tibWord("སྐྱེར་སྐྱ་", 110),
                    tibWord("རྒྱབ་པ་", 309),
                    tibWord("ལྕོག་", 401)]
    for test_word in test_words_D:
        closest_header_page = find_closest_header_page(
            test_word.word, dic_name="Das")
        print(test_word.page, closest_header_page)


def remove_wasur(tib_string):
    tib_string_bytes = tib_string.encode('utf-8')
    return tib_string_bytes.replace(b'\xbe\xad\xe0', b'').decode("utf-8")


def build_headers(file):
    headers = []
    try:
        with open(file, "r") as file:
            lines = file.readlines()
            for line in lines:
                if "\t" not in line:
                    query = re.search(r"(\d+)\.\s([^(]+)", line.rstrip())
                    page, tibText = query.group(
                        1), remove_wasur(query.group(2))
                    word = tibWord(tibText, page)
                    headers.append(word)
    except BaseException:
        abort(f"{file}|{line}")
    return headers


sorter = TibetanSort()
home = str(Path.home())
tibWord = namedtuple("word", "word page")
jaschke_headers_file = os.path.join(
    home,
    "Documents",
    "Code",
    "tib_dic_utilities",
    "jäschke_headers.md")
das_headers_file = os.path.join(
    home,
    "Documents",
    "Code",
    "tib_dic_utilities",
    "das_headers.md")

query = easygui.enterbox("Tibetan word to be found.")

das_headers = build_headers(file=das_headers_file)
jaschke_headers = build_headers(file=jaschke_headers_file)

page_J = find_closest_header_page(query, dic_name="Jäschke")
page_D = find_closest_header_page(query, dic_name="Das")

Skim_go_to_page(dic_name="Jäschke", dic_page=page_J, offset=26)
Skim_go_to_page(dic_name="Das_Tibetan", dic_page=page_D, offset=40)