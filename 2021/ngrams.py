
#Implementation of unigram bigram and trigrams in  NLP
#imports
import string
import random
import nltk


from nltk.util import pad_sequence
from nltk.util import bigrams
from nltk.util import ngrams
from nltk.util import everygrams
from nltk.lm.preprocessing import pad_both_ends
from nltk.lm.preprocessing import flatten
text = [['a', 'b', 'c'], ['a', 'c', 'd', 'c', 'e', 'f']]

list(bigrams(text[0]))  #bigrams
