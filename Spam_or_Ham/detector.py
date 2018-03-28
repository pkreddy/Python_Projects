# -*- coding: utf-8 -*-
"""
@author: Pranay Katta
"""

# Import libraries
import csv
from textblob import TextBlob
import pandas
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer,TfidfTransformer
from sklearn.naive_bayes import MultinomialNB

# Load the training dataset 'SMSSpamCollection' into variable'messages'
messages = [line.rstrip() for line in open('E:\GitHub\Python-Projects\Spam_or_Ham\SMSSpamCollection')]
# Print number of messages
print(len(messages))


"""
Read the dataset. Specify the field separator is a tab instead of a
comma.
Additionally, add column captions ('label' and 'message') for
the two
fields in the dataset.
To preserve internal quotations in messages, use QUOTE_NONE.
"""
messages = pandas.read_csv('E:\GitHub\Python-Projects\Spam_or_Ham\SMSSpamCollection', sep='\t',
quoting=csv.QUOTE_NONE,
names=["class", "message"])
# Print first 5 records
print(messages.head())

# Group by class and count
print(messages.groupby('class').count())

# Split messages into individual words
def SplitIntoWords(message):
    #message = message.decode('utf_8')
    #message = unicode(message, 'utf8')
    #print(TextBlob(message).words)
    message = str(message)
    return TextBlob(message).words
# This is what the first 5 records look when splitted into individual words
print(messages.message.head().apply(SplitIntoWords))
print(messages.message.head().apply())