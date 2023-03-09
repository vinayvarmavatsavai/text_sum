import streamlit as st
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from string import punctuation
from collections import defaultdict

nltk.download('punkt')
nltk.download('stopwords')

def text_rank(text):
    # Tokenize text into sentences and words
    sentences = sent_tokenize(text)
    words = [word.lower() for word in word_tokenize(text) if word.lower() not in stopwords.words('english') and word.lower() not in punctuation]

    # Create a graph with sentences as nodes and edges based on cosine similarity of word vectors
    graph = defaultdict(list)
    for i in range(len(sentences)):
        for j in range(i+1, len(sentences)):
            si = set(words[sentences.index(sentences[i])])
            sj = set(words[sentences.index(sentences[j])])
            similarity = len(si & sj) / (len(si) + len(sj))
            graph[sentences[i]].append((sentences[j], similarity))
            graph[sentences[j]].append((sentences[i], similarity))

    # Initialize scores for each sentence
    scores = defaultdict(float)

    # Iterate until convergence
    for _ in range(10):
        for sentence in sentences:
            score = 1.0
            for neighbor, similarity in graph[sentence]:
                score += similarity * scores[neighbor]
            scores[sentence] = score

    # Return the top 3 sentences with the highest scores
    return ' '.join(sorted(sentences, key=scores.get, reverse=True)[:30])


