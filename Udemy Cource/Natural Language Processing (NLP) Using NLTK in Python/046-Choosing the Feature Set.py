# %%
import nltk


# %%
# Choosing the feature set

import random


# %%
sample_data = [
    ("KA-01-F 1034 A", "rtc"),
    ("KA-02-F 1030 B", "rtc"),
    ("KA-03-FA 1200 C", "rtc"),
    ("KA-01-G 0001 A", "gov"),
    ("KA-02-G 1004 A", "gov"),
    ("KA-03-G 0204 A", "gov"),
    ("KA-04-G 9230 A", "gov"),
    ("KA-27 1290", "oth")
]


# %%
random.shuffle(sample_data)


# %%
test_data = [
    "KA-01-G 0109",
    "KA-02-F 9020 AC",
    "KA-02-FA 0801",
    "KA-01 9129"
]


# %%
def Learn_Simple_Feature():
    def vehicle_Number_Feature(vnumber):
        return {"vehicle_class": vnumber[6]}
    feature_sets = [(vehicle_Number_Feature(vn), cls) for (vn, cls) in sample_data]
    classifier = nltk.NaiveBayesClassifier.train(feature_sets)
    for num in test_data:
        feature = vehicle_Number_Feature(num)
        print("(simple) %s is of type %s" %(num, classifier.classify(feature)))


# %%
def Learn_Feature():
    def vehicle_Number_Feature(vnumber):
        return {
            "vehicle_class": vnumber[6],
            "vehicle_prev": vnumber[5]
            }
    feature_sets = [(vehicle_Number_Feature(vn), cls) for (vn, cls) in sample_data]
    classifier = nltk.NaiveBayesClassifier.train(feature_sets)
    for num in test_data:
        feature = vehicle_Number_Feature(num)
        print("(simple) %s is of type %s" %(num, classifier.classify(feature)))


# %%
Learn_Simple_Feature()
Learn_Feature()