# %%
import nltk


# %%
# Creating inversing and using dictionaries

class Learning_Dictionary():
    def __init__(self, sentence):
        self.words = nltk.word_tokenize(sentence)
        self.tagged = nltk.pos_tag(self.words)
        self.build_Dictionary()
        self.build_Reverse_Dictionary()

    def build_Dictionary(self):
        self.dictionary = {}
        for (word, pos) in self.tagged:
            self.dictionary[word] = pos

    def build_Reverse_Dictionary(self):
        self.rdictionary = {}
        for key in self.dictionary.keys():
            value = self.dictionary[key]
            if value not in self.dictionary:
                self.rdictionary[value] = [key]
            else:
                self.rdictionary[value].append(key)

    def is_Word_Present(self, word):
        return "Yes" if word in self.dictionary else "No"
    
    def get_POS_for_Word(self, word):
        return self.dictionary[word] if word in self.dictionary else None
    
    def get_Word_for_POS(self, pos):
        return self.dictionary[pos] if pos in self.dictionary else None
    

# %%
sentence ="All the flights got delayed due to bad weather"


# %%
learning = Learning_Dictionary(sentence)


# %%
words = ["chair", "flights", "delayed", "pencil", "weather"]


# %%
pos = ["NN", "VBS", "NNS"]


# %%
for word in words:
    status = Learning_Dictionary(word)
    print("Is '{}' present in dictionary ? : '{}'".format(word, status))
    if status is True:
        print("\tPOS for '{}' is '{}'".format(word, learning.get_POS_for_Word(word)))


# %%
for pword in pos:
    print("POS '{}' has '{}' words".format(pword, learning.get_Word_for_POS(pword)))