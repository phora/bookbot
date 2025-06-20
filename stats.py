import collections

def word_count(text):
    return len(text.split())

def char_frequency(text):
    return collections.Counter(text.lower())

def sort_char_frequency(freq_dict):
    freq_list = [{"char": k, "num": v} for k, v in freq_dict.items()]
    freq_list.sort(key=lambda x: -x["num"])
    return freq_list
