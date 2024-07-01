# %%
import nltk


# %%
text = "When life is sweet, say thank you and celebrate. When life is bitter, say thank you and grow."


# %%
sentences = nltk.sent_tokenize(text)
print(sentences)


# %%
for sentence in sentences:
    words = nltk.word_tokenize(sentence)
    tags = nltk.pos_tag(words)
    chunk = nltk.ne_chunk(tags)
    print(chunk)


# %%
#Writing your own simple chunker

text = "Life is like a piano… what you get out of it depends on how you play it."


# %%
grammar = "\n".join([
    "NP: {<DT>*<NNP>}",
    "NP: {<JJ>*<NN>}",
    "NP: {<NNP>+}"
])


# %%
sentences = nltk.sent_tokenize(text)


# %%
for sentence in sentences:
    words = nltk.word_tokenize(sentence)
    tags = nltk.pos_tag(words)
    chunk_parser = nltk.RegexpParser(grammar)
    result = chunk_parser.parse(tags)
    print(chunk)