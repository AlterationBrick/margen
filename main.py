"""
Markov text generator
Author: Taite Clark
December 2018
"""

import random

def build_dict(infile):
    """
    Construct a relationship map based on text of infile.
    Structure is a dictionary, {word_1: choices}
        where choices is a dictionary, {word_2: frequency}
        where frequency is the number of times word_2 follows word_1
    """
    d = dict()
    L = infile.read().split()
    for i in range(len(L) - 1):
        cur_word, next_word = L[i], L[i+1]
        if cur_word in d:
            if next_word in d[cur_word]:
                d[cur_word][next_word] += 1
            else:
                d[cur_word][next_word] = 1
        else:
            d[cur_word] = {next_word: 1}
    return d

def build_text(word_dict, num_words):
    """
    Create a string based on the relations specified in word_dict.
    num_words: the length of the string, in words
    Variation is created by multiplying the frequency associated with each choice
        by a random number between 0 and 1 before choosing the word with the 
        highest frequency
    """
    s = ""
    cur_word = random.choice(list(word_dict.keys()))
    for _ in range(num_words):
        s += cur_word + " "
        choices = word_dict[cur_word]
        choices_list = [(choices[word] * random.random(), word) for word in choices]
        cur_word = sorted(choices_list)[-1][1]
    return s

if __name__ == "__main__":
    fname = input("Enter file name -> ")
    num_words = input("Enter number of words in output -> ")
    num_words = int(num_words)
    print(build_text(build_dict(open(fname)) , num_words))
        
