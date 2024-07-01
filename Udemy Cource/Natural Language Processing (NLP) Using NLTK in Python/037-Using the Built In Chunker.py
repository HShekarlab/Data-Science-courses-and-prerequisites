# %%
import nltk


# %%
text = "When life is sweet, say thank you and celebrate. When life is bitter, say thank you and grow."


# %%
sentences = nltk.sent_tokenize(text)
print(sentences)


# %%
for sentence in sentences:
    words = nltk.word_tokenize(sentence)
    tags = nltk.pos_tag(words)
    chunk = nltk.ne_chunk(tags)
    print(chunk)