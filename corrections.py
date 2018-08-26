import os

from symspellpy.symspellpy import SymSpell, Verbosity  # import the module


# create object
initial_capacity = 83000
# maximum edit distance per dictionary precalculation
max_edit_distance_dictionary = 2
prefix_length = 7
sym_spell = SymSpell(initial_capacity, max_edit_distance_dictionary,
                        prefix_length)
# load dictionary
dictionary_path = os.path.join(os.path.dirname(__file__), "symspellpy",
                                "frequency_dictionary_en_82_765.txt")
term_index = 0  # column of the term in the dictionary text file
count_index = 1  # column of the term frequency in the dictionary text file
if not sym_spell.load_dictionary(dictionary_path, term_index, count_index):
    print("Dictionary file not found")

def suggest(word):
    # lookup suggestions for multi-word input strings (supports compound
    # splitting & merging)
    input_term = word
    # max edit distance per lookup (per single word, not per whole input string)
    max_edit_distance_lookup = 2
    suggestions = sym_spell.lookup_compound(input_term,
                                            max_edit_distance_lookup)
    return suggestions
