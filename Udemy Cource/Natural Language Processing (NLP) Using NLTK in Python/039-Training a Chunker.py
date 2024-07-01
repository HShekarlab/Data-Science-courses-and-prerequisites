# %%
import nltk


# %%
# Training a chunker

from nltk.corpus import conll2000, treebank_chunk


# %%
def my_simple_chunker():
    grammar = "NP: {<NNP>+}"
    return nltk.RegexpParser(grammar)


# %%
def test_nothing(data):
    cp = nltk.RegexpParser("")
    print(cp.evaluate(data))


# %%
def test_my_simple_chunker(data):
    chunker = my_simple_chunker()
    print(chunker.evaluate(data))


# %%
datasets = [
    conll2000.chunked_sents("text.txt", chunk_types= ["NP"]),
    treebank_chunk.chunked_sents()
]


# %%
for dataset in datasets:
    test_nothing(dataset[:50])
    test_my_simple_chunker(dataset[:50])