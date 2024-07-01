# %%
import nltk
from nltk import word_tokenize
from nltk.corpus import stopwords
import string


# %%
Text = "Iran’s culture, or contemporary Persian culture,\
    has its roots in one of the most ancient civilizations in the Middle East.\
        Throughout history, the Persian cultural radiation of various kinds of literature and\
            arts had a wide presence and influence that transcends\
                the boundaries of place, extending to various parts of the world.\
                    The emergence of Islam in the seventh century and the Arab conquests of Iran\
                        were a turning point for various types of arts and literature.\
                            Persian music, along with other Persian cultural elements,\
                                became the main component of what has been termed “Islamic civilization”.\
                                    Where Persian literature emerged with the formation of the modern Persian language after the Arab conquest.\
                                        Thus, Language and literature joined forces for the advancement of intellect,\
                                            before the emergence of the classical Persian literature,\
                                                then its transformation into its modern styles later on, especially after the Khomeini’s revolution in 1979"



# %%
# Word Tokenization

words = word_tokenize(Text)


# %%
# Remove Stop Words

stop_words = set(stopwords.words("english"))
stop_words = stop_words.union(string.punctuation)  

clean_words = [w for w in words if not w in stop_words]


# %%
# POS

from nltk import pos_tag

print(nltk.help.upenn_tagset())


# %%
tagged_words = pos_tag(clean_words)
print(tagged_words)


# %%
i = 0

for tagged_word in tagged_words:
    i += 1
    print("-" + str(i) + " : " + str(tagged_word))
