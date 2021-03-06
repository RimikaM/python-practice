# -*- coding: utf-8 -*-
"""
Created on Sun Nov 26 01:01:44 2017

@author: rimikamajumdar
"""

# Exercise 25: Even More practice
# More practice involving functions and variables

# try typing in help(ex25) and help(ex25.break_words) in the command line
# you will get a description of all the functions in """ for help(ex25)
# you will get a description of function break_words in """ for help(ex25.break_words)

def break_words(stuff):
    """ function will break up words for us """
    # split returns a list
    words = stuff.split(" ")
    return words

def sort_words(words):
    """ sorts the words """
    return sorted(words)

def print_first_word(words):
    """ prints the first word after popping it off """
    word = words.pop(0)
    print(word)
    
def print_last_word(words):
    """ prints the last word after popping it off"""
    word = words.pop(-1)
    print(word)
    
def sort_sentence(sentence):
    """ takes in a full sentence and returns the sorted words """
    words = break_words(sentence)
    return sort_words(words)

def print_first_and_last(sentence):
    """ prints the first and last words of the sentence """
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)
    
def print_first_and_last_sorted(sentence):
    """ sorts the words then prints the first and last one """
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)