from data_parser import load_data, test_load_data
from storing_data import build_tree
from autocompleter import get_completions

def get_input_from_user(output_str):
    val = input(output_str)
    return val


def print_output(completions, data_dict):
    for i, val in enumerate(completions):
        str_obj = data_dict[val[0]]
        origin_str = str_obj.completed_sentence
        path_ =str_obj.source_text
        print("{}. {} ({})".format(i + 1, origin_str, path_))

def read_sentence_from_user(storage_tree, data_dict):
    to_end = False
    print_before = "The system is ready. Enter your text:\n"
    input_val = ""
    while not to_end:
        input_val = input_val + get_input_from_user(print_before)
        print_before = input_val
        if input_val[-1] == '#':
            to_end = True
        completions = get_completions(input_val, storage_tree, data_dict)
        print_output(completions, data_dict)


def run():
    test_dict = {}
    test_load_data(test_dict)
    storage_tree = build_tree(test_dict)
    while True:
        read_sentence_from_user(storage_tree, test_dict)


run()
