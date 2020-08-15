import re
from collections import Counter

def extract_text(file):
    """
    Input:
        file_name : contains words that will be used to build engine model.
    Output:
        words: a list containing all the words in the corpus in lower case.
    """
    words = []

    with open(file) as f:
        data = f.read()
        data = data.lower()
        words = re.findall('\w+', data)

    return words

def get_count(word_l):
    '''
    Input:
        word_l: a set of words representing the corpus.
    Output:
        word_count_dict: The wordcount dictionary where key is the word and value is its frequency.
    '''
    word_count_dict = {}
    word_count_dict = Counter(word_l)
    return word_count_dict

def get_probs(word_count_dict):
    '''
    Input:
        word_count_dict: The wordcount dictionary where key is the word and value is its frequency.
    Output:
        probs: A dictionary where keys are the words and the values are the probability that a word will occur.
    '''
    probs = {}
    l = sum(word_count_dict.values())
    probs = {i:v/l for i, v in word_count_dict.items()}

    return probs