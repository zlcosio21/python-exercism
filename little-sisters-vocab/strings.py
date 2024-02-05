"""Functions for creating, transforming, and adding prefixes to strings."""


def add_prefix_un(word):
    return "un" + word


def make_word_groups(vocab_words):
    return f" :: {vocab_words[0]}".join(vocab_words)


def remove_suffix_ness(word):
    new_word = word.rstrip("ness")

    return new_word[0:-1] + "y" if new_word.endswith("i") else new_word


def adjective_to_verb(sentence, index):
    return sentence.split()[index].rstrip(".") + "en"
