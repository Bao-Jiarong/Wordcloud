import wordcloud
import numpy as np
from matplotlib import pyplot as plt
from IPython.display import display
import io
import sys
import os

f = open("b.txt", "r")
file_contents = f.read()
f.close()

def calculate_frequencies(file_contents):

    # Here is a list of punctuations and uninteresting words you can use to process your text.

    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    uninteresting_words = ["the", "a", "to", "if", "is", "for","not","on","out","into","in","it", "of", "and", "or", "an", "as", "i", "me", "my", \
    "we", "our", "ours", "you", "your", "yours", "he", "she", "him", "his", "her", "hers", "its", "they", "them", \
    "their", "what", "which", "who", "whom", "this", "that", "am", "are", "was", "were", "be", "been", "being", \
    "have", "has", "had", "do", "does", "did", "but", "at", "by", "with", "from", "here", "when", "where", "how", \
    "all", "any", "both", "each", "few", "more", "some", "such", "no", "nor", "too", "very", "can", "will", "just"]

    file_contents = file_contents.lower()
    file_contents = file_contents.split(" ")
    frequencies = {}
    for content in file_contents:
        if content not in punctuations and content not in uninteresting_words:
            if content.isalpha() == True:
                if content not in frequencies:
                    frequencies[content] = 0
                frequencies[content] += 1

    #wordcloud
    cloud = wordcloud.WordCloud()
    cloud.generate_from_frequencies(frequencies)
    return cloud.to_array()

# Display wordcloud image

myimage = calculate_frequencies(file_contents)
plt.imshow(myimage, interpolation = 'nearest')
plt.axis('off')
plt.show()
