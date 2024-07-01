# %%
# Resolving anaphora

import random
import nltk
from nltk.corpus import names
from nltk.chunk import tree2conlltags


# %%
class Anaphora_Example:
    def __init__(self):
        males = [(name, "male") for name in names.words("male.txt")]
        females = [(name, "female") for name in names.words("female.txt")]
        combined = males + females
        random.shuffle(combined)
        training = [(self.feature(name), gender) for (name, gender) in combined]
        self._classifier = nltk.NaiveBayesClassifier.train(training)

    def feature(self, word):
        return {"last(1)": word[-1]}
    
    def gender(self, word):
        return self._classifier.classify(self.feature(word))
    
    def Learn_Anaphora(self):
        sentence = [
             "Not all those who wander are lost.",
             "A rose by any other name would smell as sweet.",
             "If you really look closely, most overnight successes took a long time.",
             "Do you know? A fortune that you don’t use, is others wish"
             "What screws us up the most in life is the picture in our head of how it is supposed to be."
        ]
        for sent in sentence:
            chunks = nltk.ne_chunk(nltk.pos_tag(nltk.word_tokenize(sent)), binary= False)
            stack = []
            print(sent)
            items = tree2conlltags(chunks)
            for item in items:
                if item[1] == "NNP" and (item[2] == "B-PERSON" or item[2] == "O"):
                    stack.append((item[0], self.gender(item[0])))
                elif item[1] == "CC":
                    stack.append(item[0])
                elif item[1] == "PRP":
                    stack.append(item[0])
            print("\t {}".format(stack))


# %%
anaphora = Anaphora_Example()
anaphora.Learn_Anaphora()