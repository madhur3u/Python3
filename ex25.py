# PLAYING WITH SENTENCES AND WORDS

def break_words(stuff) :
    '''This function will break words'''
    words = stuff.split(' ')
    return words

def sort_words(words) :
    return sorted(words)

def print_first_word(words) :
    '''Print the 1st word after popping it off'''
    word = words.pop(0)
    print(word)

def print_last_word(words) :
    word = words.pop(-1)
    print(word)

def sort_sentence(sentence) :
    '''Take a full sentence and sort words in it'''
    words = break_words(sentence)
    return sort_words(words)

def print_first_last(sentence) :
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)

def print_first_and_last_sorted(sentence) :
    """Sorts the words then prints the first and last one."""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)
