import re

ALPHABET_LEN = 26

def is_pangram(sentence):
    sentence = set(re.sub(r"[^a-zA-Z]", "", sentence.lower()))

    return len(sentence) == ALPHABET_LEN
