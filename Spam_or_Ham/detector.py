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
    #message = str(message)
    return TextBlob(message).words
# This is what the first 5 records look when splitted into individual words
print(messages.message.head().apply(SplitIntoWords))


# Convert each word into its base form
def WordsIntoBaseForm(message):
    message = message.lower()
    words = TextBlob(message).words
    return [word.lemma for word in words]
# Convert each message into a vector
trainingVector = CountVectorizer(analyzer=WordsIntoBaseForm).fit(messages['message'])

# View occurrence of words in an arbitrary vector. Use 9 for vector #10.
message10 = trainingVector.transform([messages['message'][9]])
print (message10)

# Print message #10 for comparison
print(messages['message'][9])
# Identify repeated words
print('First word that appears twice:',trainingVector.get_feature_names()[3437])
print('Word that appears three times:',trainingVector.get_feature_names()[5192])

# Bag-of-words for the entire training dataset
messagesBagOfWords = trainingVector.transform(messages['message'])
# Weight of words in the entire training dataset - Term Frequency and Inverse Document Frequency
messagesTfidf = TfidfTransformer().fit(messagesBagOfWords).transform(messagesBagOfWords)

# Train the model
spamDetector = MultinomialNB().fit(messagesTfidf,messages['class'].values)

# Test message
#You can test the model by giving your own example string
example = ['England v Macedonia - dont miss the goals/team news. Txt ENGLAND to 99999']
# Result
checkResult = spamDetector.predict(trainingVector.transform(example))[0]
print('The message [',example[0],'] has been classified as', checkResult)