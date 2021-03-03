"""Generate Markov text from text files."""

from random import choice

def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """
    text = open(file_path) 
    
    text_final = []

    for word in text:  #iterate over words in line of file splited by spaces
        text_final += word.split() 
    text.close()

    return text_final


def make_chains(text_string):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains('hi there mary hi there juanita')

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']

        >>> chains[('there','juanita')]
        [None]
    """

    chains = {}

    for i in range(len(text_string)-2): #Stop at the 41 index (i ending at 40 and i+1 ending at 41)
        key = (text_string[i],text_string[i+1])
        value = text_string[i+2]

        if key not in chains: #Make key tupled name into dictionary chains
            chains[key] = []
            chains[key].append(value)
        else:
            chains[key].append(value)

    return chains


#def make_text(chains):
#    """Return text from chains."""

    #pull first key
    # key_list = list(chains.keys())

    # first_key = list(chains.keys())[0]

    # word = str(list(chains.keys())[0][1]), str(choice(chains[first_key])
    
    #pass


    # first_key = key_list[0] #(would, you)
    # second_word = key_list[0][1] #'you'
    # new_first_value = choice(chains[first_key]
    # next_key = (str(second_word),str(new_first_value))

def make_text(chains):
    """Return text from chains."""

    key = choice(list(chains.keys())) #pull a random key 
    words = [key[0], key[1]]
    word = choice(chains[key])
    #(would,you) >could
                #>
    # Keep looping until we reach a value of None
    # (which would mean it was the end of our original text)
    # Note that for long texts (like a full book), this might mean
    # it would run for a very long time.

    while word is not None:
        key = (key[1], word)
        words.append(word)
        word = choice(chains[key])

    return ' '.join(words)



    # #get a random key from chains 
    # ran_key = choice(list(chains.keys()))   #yay

    # #get the second word in the key pulled
    # s_word = ran_key[1]

    # #get the random value in the called key from dictionary
    # ran_value = choice(chains[ran_key])


    # #make a new key
    # new_key = (s_word,ran_value)

    # #pull a random value from the generated new key
    # random_value = choice(chains[new_key])

    # # random_robot_words = []
    # keys > random value > 


    # words = []

    # your code goes here

    #return ' '.join(words)


input_path = 'green-eggs.txt'

# Open the file and turn it into one long string
# input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_path)

# Produce random text
random_text = make_text(chains)

print(random_text)
