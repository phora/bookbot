import collections

def word_count(text):
    return len(text.split())

def char_frequency(text):
    return collections.Counter(text.lower())
