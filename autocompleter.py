from data_parser import clear_str


def get_suggestion_with_replace_letter(input_, substrs_tree):
    temp_tree = substrs_tree
    is_already_rep_letter = False
    suggestions = []
    for index, letter in enumerate(input_):
        if letter in temp_tree.children.keys():
            temp_tree = temp_tree.children[letter]
        elif not is_already_rep_letter:
            is_already_rep_letter = True
            for key, child in temp_tree.children.items():
                if key != letter:
                    child_suggest =  get_suggestions(input_[index + 1:], child)
                    suggestions = suggestions + child_suggest
            return suggestions
    return temp_tree.data


def get_suggestion_with_add_letter(input_, substrs_tree):
    temp_tree = substrs_tree
    is_already_add_letter = False
    suggestions = []
    for index, letter in enumerate(input_):
        if letter in temp_tree.children.keys():
            temp_tree = temp_tree.children[letter]
        elif not is_already_add_letter:
            is_add_remove_letter = True
            for key, child in temp_tree.children.items():
                child_suggest =  get_suggestions(input_[index:], child)
                suggestions = suggestions + child_suggest
            return suggestions
    return temp_tree.data


def get_suggestion_with_remove_letter(input_, substrs_tree):
    temp_tree = substrs_tree
    is_already_remove_letter = False
    for letter in input_:
        if letter in temp_tree.children.keys():
            temp_tree = temp_tree.children[letter]
        elif not is_already_remove_letter:
            is_already_remove_letter = True
        else:
            return []
    return temp_tree.data

def get_suggestions(input, substrs_tree):
    temp_tree = substrs_tree
    for letter in input:
        if letter in temp_tree.children.keys():
            temp_tree = temp_tree.children[letter]
        else:
            return []
    return temp_tree.data


def get_completions(input, storage_tree, data_as_dict):
    cleared_input = clear_str(input)
    regular_suggestions = get_suggestions(cleared_input, storage_tree)
    removed_letter_suggestions= get_suggestion_with_remove_letter(cleared_input, storage_tree)
    add_letter_suggestions= get_suggestion_with_add_letter(cleared_input, storage_tree)
    replace_letter_suggestions = get_suggestion_with_replace_letter(cleared_input, storage_tree)
    suggestions = regular_suggestions + removed_letter_suggestions + add_letter_suggestions + replace_letter_suggestions
    #suggestions = [data_as_dict[item[0]].completed_sentence for item in suggestions]
    return set(suggestions)