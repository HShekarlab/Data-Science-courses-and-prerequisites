# %%
import nltk

# nltk.download_gui()


# %%
Text = "Iran’s culture, or contemporary Persian culture, \
       has its roots in one of the most ancient civilizations in the Middle East. \
       Throughout history, the Persian cultural radiation of various kinds of literature and \
       arts had a wide presence and influence that transcends \
       the boundaries of place, extending to various parts of the world. \
       The emergence of Islam in the seventh century and the Arab conquests of Iran \
       were a turning point for various types of arts and literature. \
       Persian music, along with other Persian cultural elements, \
       became the main component of what has been termed “Islamic civilization”. \
       Where Persian literature emerged with the formation of the modern Persian language after the Arab conquest. \
       Thus, Language and literature joined forces for the advancement of intellect, \
       before the emergence of the classical Persian literature, \
       then its transformation into its modern styles later on, \
       especially after the Khomeini’s revolution in 1979"


# %%
from nltk import sent_tokenize

# Sentence Tokenization
sentences = sent_tokenize(Text)

print("------- Original Text : \n" + Text + "\n\n")
print("------- Sentecne : " + str(len(sentences)) + "\n")


# %%
i = 0

for sentence in sentences:
    i += 1
    print("-" + str(i) + " : " + sentence)



# %%
# Word Tokenization

from nltk import word_tokenize

words = word_tokenize(Text)

print("------- Original Text : \n" + Text + "\n\n")
print("------- Word : " + str(len(words)) + "\n")

i = 0

for word in words:
    i += 1
    print("-" + str(i) + " : " + word)