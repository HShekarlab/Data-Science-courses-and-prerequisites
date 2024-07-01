# %%
import nltk


# %%
# Segmenting sentences using classification

def Feature_Extractor(words, i):
    return ({
        "current_word": words[i],
        "next_is_upper": words[i+1][0].isupper()
    }, words[i+1][0].isupper()
    )


# %%
def get_Feature_sets(sentence):
    words = nltk.word_tokenize(sentence)
    feature_sets = [Feature_Extractor(words, i) for i in range(1, len(words) - 1) if words[i] == "."]
    return feature_sets


# %%
def segment_Text_and_Print_Sentence(data):
    words = nltk.word_tokenize(data)
    for i in range(0, len(words) - 1):
        if words[i] == ".":
            if classifier.classify(Feature_Extractor(words, i)[0]) == True:
                print(".")
            else:
                print(words[i], end= "")
        else:
            print("{}".format(words[i]), end= "")
    print(words[-1])


# %%
train_data = "Success seems to be connected with action. Successful people keep moving. They make mistakes but they don't quit."
test_data = "Life is not a rehearsal. Each day is a new show, no repeat no rewind. Perform carefully live the best, choose the best and do the best."


# %%
train_data_set = get_Feature_sets(train_data)


# %%
classifier = nltk.NaiveBayesClassifier.train(train_data_set)


# %%
segment_Text_and_Print_Sentence(test_data)