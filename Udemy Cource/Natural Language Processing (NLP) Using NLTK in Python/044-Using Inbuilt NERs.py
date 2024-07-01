# %%
import nltk


# %%
# Using inbuilt NERs

def sample_NE():
    sent = nltk.corpus.treebank.tagged_sents()[0]
    print(nltk.ne_chunk(sent))


# %%
def sample_NE_2():
    sent = nltk.corpus.treebank.tagged_sents()[0]
    print(nltk.ne_chunk(sent, binary= True))


# %%
if __name__ == "__main__":
    sample_NE()
    sample_NE_2()