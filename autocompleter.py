from data_parser import clear_str


def get_suggestions(input, substrs_tree):
    temp_tree = substrs_tree
    for letter in input:
        if letter in temp_tree.children.keys():
            temp_tree = temp_tree.children[letter]
        else:
            return None
    return temp_tree.data


def get_completions(input, storage_tree, data_as_dict):
    cleared_input = clear_str(input)
    suggestions = get_suggestions(cleared_input, storage_tree)
    suggestions = [data_as_dict[item[0]].completed_sentence for item in suggestions]
    return suggestions