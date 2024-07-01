# %%
import nltk
from nltk import word_tokenize
from nltk.corpus import stopwords
import string
from nltk import pos_tag
from nltk.stem.lancaster import LancasterStemmer
from nltk.stem.porter import PorterStemmer
from nltk.stem.snowball import SnowballStemmer
from nltk.stem import WordNetLemmatizer



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
tagged_words = pos_tag(clean_words)


# %%
# Stemming

stemmer = LancasterStemmer()


# %%

stemmer = PorterStemmer()



# %%

stemmer = SnowballStemmer("english")


# %%
# Lemmatization

lemmatizer = WordNetLemmatizer()


# %%
# NER

from nltk import ne_chunk, sent_tokenize

sentences = sent_tokenize(Text)

for sentence in sentences:
    words = word_tokenize(sentence)
    tags = pos_tag(words)
    ner = ne_chunk(tags)
    ner.draw()
