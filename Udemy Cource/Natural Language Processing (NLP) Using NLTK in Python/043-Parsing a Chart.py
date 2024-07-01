# %%
import nltk

# %%
# Parsing a chart

from nltk.grammar import CFG
from nltk.parse.chart import ChartParser, BU_LC_STRATEGY


# %%
grammar = CFG.fromstring("""
S -> T1 T4
T1 -> NNP VBZ
T2 -> DT NN
T3 -> IN NNP
T4 -> T3 | T2 T3
NNP -> 'Tajmahal' | 'Agra' | 'Paris' | 'France'
VBZ -> 'is'
IN -> 'in' | 'of'
DT -> 'the'
NN -> 'capital'
""")


#%%
cp = ChartParser(grammar, BU_LC_STRATEGY, trace= True)


# %%
sentence = "Paris is the capital of France"


# %%
tokens = sentence.split()


# %%
chart = cp.chart_parse(tokens)


# %%
parse = list(chart.parses(grammar.start()))


# %%
print("Total Edge : ", len(chart.edges()))


# %%
for tree in parse: print(tree)


# %%
tree.draw()