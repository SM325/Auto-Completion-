from data_parser import load_data, test_load_data
from storing_data import build_tree
from autocompleter import get_completions


def run():
    test_dict = {}
    test_load_data(test_dict)
    storage_tree = build_tree(test_dict)
    completions = get_completions('it is', storage_tree, test_dict)
    print(completions)


run()
