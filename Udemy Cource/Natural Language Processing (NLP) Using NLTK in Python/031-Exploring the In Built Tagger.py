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