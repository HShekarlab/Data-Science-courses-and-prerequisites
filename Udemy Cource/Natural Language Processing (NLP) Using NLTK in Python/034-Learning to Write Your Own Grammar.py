# %%
import nltk


# %%
# Writing your own tagger

def Learn_Default_Tagger(simple_sentence):
    words_in_sentence = nltk.word_tokenize(simple_sentence)
    tagger = nltk.DefaultTagger("NN")
    pos_enable_tag = tagger.tag(words_in_sentence)
    print(pos_enable_tag)


# %%
def Learn_Re_Tagger(simple_sentence):
    customer_patterns = [
        (r".*ing$", "ADJECTIVE"),
        (r".*ly$", "ADVERB"),
        (r".*ion", "NOUN"),
        (r"(.*ate|.*en|is)$", "VERB"),
        (r"^an$", "INDEFINITE-ARTICLE"),
        (r"^(with|on|at)$", "PREPOSITION"),
        (r"^\-?[0-9]+(\.[0-9]+)$", "NUMBER"),
        (r".*$", None)
    ]
    tagger = nltk.RegexpTagger(customer_patterns)
    words_in_sentence = nltk.word_tokenize(simple_sentence)
    pos_enable_tags = tagger.tag(words_in_sentence)
    print(pos_enable_tags)


# %%
def Learn_LookUp_Tagger(simple_sentence):
    mapping = {
        ".": ".",
        "place": "NN",
        "on": "IN",
        "earth": "NN",
        "Mysore": "NNP",
        "is": "VBZ",
        "an": "DT",
        "amazing": "JJ"
    }
    tagger = nltk.UnigramTagger(model= mapping)
    words_in_sentence = nltk.word_tokenize(simple_sentence)
    pos_enable_tag = tagger.tag(words_in_sentence)
    print(pos_enable_tag)


# %%
if __name__ == "__main__":
    test_sentence = "Mysore is an amazing place on earth. I have visited Mysore 10 times."
    Learn_Default_Tagger(test_sentence)
    Learn_Re_Tagger(test_sentence)
    Learn_LookUp_Tagger(test_sentence)


# %%
# Tagging your on tagger
import pickle


# %%
def Sample_Data():
    return [
        "Paris is the capital of France.",
        "Steve Jobs was the CEO of Apple.",
        "iPhone was Invented by Apple.",
        "Books can be purchased in Market."
    ]


# %%
def Build_Dictionary():
    dictionary = {}
    for sent in Sample_Data():
        parts_of_speech_tags = nltk.pos_tag(nltk.word_tokenize(sent))
        for tag in parts_of_speech_tags:
            value = tag[0]
            pos = tag[1]
            dictionary[value] = pos
    return dictionary


# %%
def Save_my_Tagger(tagger, file_name):
    file_handle = open(file_name, "wb")
    pickle.dump(tagger, file_handle)
    file_handle.close()


# %%
def Save_my_Traning(file_name):
    tagger = nltk.UnigramTagger(model= Build_Dictionary())
    Save_my_Tagger(tagger, file_name)


# %%
def Load_my_Tagger(file_name):
    return pickle.load(open(file_name, "rb"))


# %%
sentence = "Iphone is purchased by Steve Jobs in Paris Market"
file_name = "my_Tagger.pickle"


# %%
Save_my_Traning(file_name)


# %%
my_Tagger = Load_my_Tagger(file_name)


# %%
print(my_Tagger.tag(nltk.word_tokenize(sentence)))


# %%
# Learning to write you own grammar
import string
from nltk.parse.generate import generate


# %%
productions = [
    "ROOt -> WORD",
    "WORd -> ' '",
    "WORD -> NUMBER LETTER",
    "WORD -> LETTER NUMBER"
]


# %%
digits = list(string.digits)

for digit in digits[:4]:
    productions.append("NUMBER -> '{w}'".format(w= digit))


# %%
letters = "' | '".join(list(string.ascii_lowercase)[:4])
productions.append("LETTER -> '{w}'".format(w= letters))


# %%
grammar_string = "\n".join(productions)


# %%
grammar = nltk.CFG.fromstring(grammar_string)
print(grammar)


# %%
for sentence in generate(grammar, n= 5, depth= 5):
    palindrom = "".join(sentence).replace(" ", "")
    print("Generated Word: {}".format(palindrom, len(palindrom)))