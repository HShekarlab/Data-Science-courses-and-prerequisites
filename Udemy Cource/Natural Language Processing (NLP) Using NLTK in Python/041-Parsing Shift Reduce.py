# %%
import nltk


# %%
# Parsing shift-reduce

def SR_Parser_Example(grammar, text_list):
    parser = nltk.parse.ShiftReduceParser(grammar)
    for txt in text_list:
        sentence = nltk.word_tokenize(txt)
        for tree in parser.parse(sentence):
            print(tree)
            tree.draw()


# %%
text = [
    "Tajmahal is in Agra",
    "Paris is the capital of France"
]


# %%
grammar = nltk.CFG.fromstring("""
S -> NP VP
NP -> NNP VBZ
VP -> IN NNP | DT NN IN NNP
NNP -> 'Tajmahal' | 'Agra' | 'Paris' | 'France'
VBZ -> 'is'
IN -> 'in' | 'of'
DT -> 'the'
NN -> 'capital'
""")


# %%
SR_Parser_Example(grammar, text)