# %%
# Performing sentiment analysis

import nltk
import nltk.sentiment.sentiment_analyzer
import nltk.sentiment.util


# %%
def word_based_sentiment():
    positive_words = ["love", "hope", "joy"]
    text = "Rainfall this year brings lot of hope and joy to Farmers.".split()
    analysis = nltk.sentiment.util.extract_bigram_feats(text, positive_words)
    print("-- single word sentiment --")
    print(analysis)


# %%
def multi_word_based_sentiment():
    word_sets = [("heavy", "rains"), ("flood", "bengalura")]
    text = "heavy rains cause flash flooding in bengalura".split()
    analysis = nltk.sentiment.util.extract_bigram_feats(text, word_sets)
    print("-- multi word sentiment --")
    print(analysis)


# %%
def mark_negativity():
    text = "Rainfall last year did not bring joy to Farmers".split()
    negation = nltk.sentiment.util.mark_negation(text)
    print("-- negativity --")
    print(negation)


# %%
if __name__ == "__main__":
    word_based_sentiment()
    multi_word_based_sentiment()
    mark_negativity()