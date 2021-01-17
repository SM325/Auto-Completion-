import re
import string
import glob
import os
from sentence import AutoCompleteData


class sentence:
    def __init__(self, str_, path, row):
        self.str_ = str_
        self.path = path
        self.row = row

def clear_str(str_):
    s = ''.join(ch for ch in str_ if ch not in string.punctuation)
    low_str = s.lower()
    clear_space = re.sub(' +', ' ', low_str)
    return clear_space


def load_data(data_dict):
    key_counter = 0
    path_base = './Archive'
    flist_files = glob.glob(os.path.join(path_base, '*.txt'))
    for txt_file in flist_files:
       with open(txt_file, 'r', encoding="utf8") as f:
            content = f.read()
            content = content.split('\n')
            for index, row in enumerate(content):
                if row:
                    new_sentence = AutoCompleteData(row, txt_file + ' ' + str(index+1), None, None)
                    data_dict[key_counter] = new_sentence
                    key_counter += 1


def test_load_data(data_dict):
    key_counter = 0
    txt_file = 'init2.txt'
    with open(txt_file, 'r', encoding="utf8") as f:
        content = f.read()
        content = content.split('\n')
        for index, row in enumerate(content):
            if row:
                new_sentence = AutoCompleteData(row, txt_file + ' ' + str(index+1), None, None)
                data_dict[key_counter] = new_sentence
                key_counter += 1




