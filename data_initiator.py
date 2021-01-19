import re
import string
import glob
import os
from sentence import AutoCompleteData
import pickle
import sys
import os
import glob
from data_parser import load_data
from data_tree_builder import build_tree


def initiate_data():
    test_dict = {}

    # test_load_data(test_dict)
    load_data(test_dict)
    with open('data_dict.obj', 'wb') as fp:
        pickle.dump(test_dict, fp)

    storage_tree = build_tree(test_dict)

    for letter, node in storage_tree.children.items():
        with open('subtrees/sub_tree_' + letter +'.obj', 'wb') as fp:
            pickle.dump(node, fp)


initiate_data()