from tree import Node
from data_parser import clear_str


def build_subtree(letter, index, sentence, sentence_id, root):
    offset = index
    root.add_child(sentence_id, offset, letter)
    last_added = root.children[letter]
    index += 1
    while index < len(sentence):
        letter = sentence[index]
        last_added.add_child(sentence_id, offset, letter)
        last_added = last_added.children[letter]
        index += 1


def build_tree(sentences):
    root = Node([])
    # sentences = {1: 'this line is very nice', 2: 'is'}

    for s_id, str_object in sentences.items():
        cleared_str = clear_str(str_object.completed_sentence)
        for index, letter in enumerate(cleared_str):
            build_subtree(letter, index, cleared_str, s_id, root)

    return root
