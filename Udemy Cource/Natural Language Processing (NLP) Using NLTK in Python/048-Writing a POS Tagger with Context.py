# %%
import nltk


# %%
# Writing a POS tagger with context

sentences = [
    "Not all those who wander are lost.",
    "A rose by any other name would smell as sweet.",
    "If you really look closely, most overnight successes took a long time.",
    "Do you know? A fortune that you don’t use, is others wish"
    "What screws us up the most in life is the picture in our head of how it is supposed to be."
    "I am not afraid of tomorrow, for I have seen yesterday and I love today White.",
    "Forgiving is good…but forgetting is better."
]


# %%
def get_sentence_words():
    sent_words = []
    for sentence in sentences:
        words = nltk.pos_tag(nltk.word_tokenize(sentence))
        sent_words.append(words)
    return sent_words


# %%
def no_context_Tagger():
    tagger = nltk.UnigramTagger(get_sentence_words())
    print(tagger.tag("the little remarks towards assembly are laughable".split()))


# %%
def with_context_Tagger():
    def word_features(words, word_POS_in_sentence):
        end_features = {
            "last(1)": words[word_POS_in_sentence][-1],
            "last(2)": words[word_POS_in_sentence][-2:],
            "last(3)": words[word_POS_in_sentence][-3:]
        }
        if word_POS_in_sentence > 1:
            end_features["prev"] = words[word_POS_in_sentence - 1]
        else:
            end_features["prev"] = "|NONE|"
        return end_features
    all_sentence = get_sentence_words()
    featured_data = []
    for sentence in all_sentence:
        untagged_Sentence = nltk.tag.untag(sentence)
        featured_sentence = [(word_features(untagged_Sentence, index), tag) for index, (word, tag) in enumerate(sentence)]
        featured_data.extend(featured_sentence)
    breakup = int(len(featured_data) * 0.5)
    train_data = featured_data[breakup:]
    test_data = featured_data[:breakup]
    classifier = nltk.NaiveBayesClassifier.train(train_data)
    print("Accuracy of the classifier : {}".format(nltk.classify.accuracy(classifier, test_data)))


# %%
no_context_Tagger()
with_context_Tagger()