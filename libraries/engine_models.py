from collections import Counter

def delete_char(word, verbose=False):
    '''
    Input:
        word: the string/word for which you will generate all possible words in the vocabulary which have 1 missing character
    Output:
        delete_l: a list of all possible strings obtained by deleting 1 character from word
    '''
    delete_l = []
    split_l = []

    for i in range(len(word)):
        split_l.append((word[:i], word[i:]))
        delete_l.append(word[:i]+word[i+1:])

    if verbose: print(f"input word : {word} \nsplit : {split_l}, \ndelete : {delete_l}")

    return delete_l

def switch_char(word, verbose=False):
    '''
    Input:
        word: input string
     Output:
        switches: a list of all possible strings with one adjacent charater switched
    '''
    switch_l = []
    split_l = []

    for i in range(len(word)):
        split_l.append((word[:i], word[i:]))
        if len(word[i:]) >= 2 : switch_l.append(word[:i] + word[i+1] + word[i] + word[i+2:])

    if verbose: print(f"Input word : {word} \nsplit : {split_l} \nswitch : {switch_l}")

    return switch_l

def replace_char(word, verbose=False):
    '''
    Input:
        word: the input string/word
    Output:
        replaces: a list of all possible strings where we replaced one letter from the original word.
    '''
    letters = 'abcdefghijklmnopqrstuvwxyz'
    replace_l = []
    split_l = []

    for i in range(len(word)):
        split_l.append((word[:i], word[i:]))
        if len(word[i:]) >= 1 : [replace_l.append(word[:i] + j + word[i+1:]) for j in letters]

    replace_set = set(replace_l)
    replace_set.remove(word)
    replace_l = sorted(list(replace_set))

    if verbose: print(f"Input word : {word} \nsplit : {split_l} \nreplace : {replace_l}")

    return replace_l

def insert_char(word, verbose=False):
    '''
    Input:
        word: the input string/word
    Output:
        inserts: a set of all possible strings with one new letter inserted at every offset
    '''
    letters = 'abcdefghijklmnopqrstuvwxyz'
    insert_l = []
    split_l = []

    for i in range(len(word)+1):
        split_l.append((word[:i], word[i:]))
        [insert_l.append(word[:i] + j + word[i:]) for j in letters]

    if verbose: print(f"Input word : {word} \nsplit : {split_l} \ninsert : {insert_l}")

    return insert_l

def edit_one_char(word, allow_switches = True):
    """
    Input:
        word: the string/word for which we will generate all possible wordsthat are one edit away.
    Output:
        edit_one_set: a set of words with one possible edit. Please return a set. and not a list.
    """
    edit_one_set = set()

    if allow_switches:
        edit_one_set.update(switch_char(word))
    edit_one_set.update(delete_char(word))
    edit_one_set.update(replace_char(word))
    edit_one_set.update(insert_char(word))

    return edit_one_set

def edit_two_chars(word, allow_switches = True):
    '''
    Input:
        word: the input string/word
    Output:
        edit_two_set: a set of strings with all possible two edits
    '''
    edit_two_set = set()

    for i in edit_one_char(word,allow_switches):
        if len(i) >=1:
            edit_two_set.update(edit_one_char(i, allow_switches))

    return edit_two_set

def get_corrections(word, probs, vocab, n=2, verbose = False):
    '''
    Input:
        word: a user entered string to check for suggestions
        probs: a dictionary that maps each word to its probability in the corpus
        vocab: a set containing all the vocabulary
        n: number of possible word corrections you want returned in the dictionary
    Output:
        n_best: a list of tuples with the most probable n corrected words and their probabilities.
    '''
    suggestions = []
    n_best = []

    suggestions = list((word in vocab and word) or
                   edit_one_char(word).intersection(vocab) or
                   edit_two_chars(word).intersection(vocab))
    n_best = [(i, probs[i]) for i in suggestions]

    if verbose: print("entered word = ", word, "\nsuggestions = ", suggestions)

    return n_best