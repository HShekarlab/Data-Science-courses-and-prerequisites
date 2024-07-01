# %%
# Solving the text similarity problem

import nltk
import math
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


# %%
class Text_Similarity_Example:
    def __init__(self):
        self.statement = [
            "ruled india",
            "Chalukyas ruled Badami",
            "So many kingdoms ruled India",
            "Lalbagh is a botanical garden in India"
        ]
    
    def TF(self, sentence):
        words = nltk.word_tokenize(sentence.lower())
        freq = nltk.FreqDist(words)
        dictionary = {}
        for key in freq.keys():
            norm = freq[key] / float(len(words))
            dictionary[key] = norm
        return dictionary
    
    def IDF(self):
        def idf(total_number_of_documents, number_of_documents_with_this_word):
            return 1.0 + math.log(total_number_of_documents / number_of_documents_with_this_word)
        num_documents = len(self.statement)
        unique_words = {}
        idf_values = {}
        for sentence in self.statement:
            for word in nltk.word_tokenize(sentence.lower()):
                if word not in unique_words:
                    unique_words[word] = 1
                else:
                    unique_words[word] += 1
        for word in unique_words:
            idf_values[word] = idf(num_documents, unique_words[word])
            return idf
    
    def TF_IDF(self, query):
        words = nltk.word_tokenize(query.lower())
        idf = self.IDF()
        vectors = {}
        for sentence in self.statement:
            tf = self.TF(sentence)
            for word in words:
                tfv = tf[word] if word in tf else 0.0
                idfv = idf[word] if word in idf else 0.0
                mul = tfv * idfv
                if word not in vectors:
                    vectors[word] = []
                vectors[word].append(mul)
        return vectors
    
    def display_vectors(self, vectors):
        print(self.statement)
        for word in vectors:
            print("{} -> {}",format(word, vectors[word]))
            
    def cosine_similarity(self):
        vec = TfidfVectorizer()
        matrix = vec.fit_transform(self.statement)
        for j in range(1, 5):
            i = j - 1
            print("\tsimilarity of document {} with others".format(i))
            similarity = cosine_similarity(matrix[i:j], matrix)
            print(similarity)

    def demo(self):
        input_query = self.statement[0]
        vectors = self.TF_IDF(input_query)
        self.display_vectors(vectors)
        self.cosine_similarity()


# %%
similarity = Text_Similarity_Example()
similarity.demo()