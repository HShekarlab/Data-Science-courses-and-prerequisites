# %%
import nltk


# %%
simple_sentence = "Paris is the capital of France."
print(simple_sentence)


# %%
words_in_sentence = nltk.word_tokenize(simple_sentence)
print(words_in_sentence)


# %%
parts_of_speech_tags = nltk.pos_tag(words_in_sentence)
print(parts_of_speech_tags)


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