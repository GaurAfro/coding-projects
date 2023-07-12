import json
import nltk
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np

# Download the 'punkt' package for sentence tokenization
nltk.download('punkt')

def summarize_conversation(chat_log_v6.json):
    # Load the JSON file
    with open(chat_log_v6.json, 'r') as file:
        chat_data = json.load(file)

    # Concatenate all the messages into a single string, separating them with spaces
    conversation_text = " ".join([message['message'] for message in chat_data])

    # Split the conversation into sentences using nltk's sent_tokenize function
    sentences = nltk.sent_tokenize(conversation_text)

    # Use the TfidfVectorizer to identify the most important words in the conversation
    vectorizer = TfidfVectorizer(stop_words='english', max_features=50)
    tfidf_matrix = vectorizer.fit_transform(sentences)

    # Compute the average tf-idf score for each sentence
    average_tfidf_scores = np.mean(tfidf_matrix.toarray(), axis=1)

    # Select the top 20% of sentences based on their average tf-idf scores
    num_sentences_in_summary = int(len(sentences) * 0.2)
    top_sentence_indices = np.argsort(average_tfidf_scores)[-num_sentences_in_summary:]

    # Sort the indices so that the sentences are in their original order
    top_sentence_indices.sort()

    # Select the sentences that go into the summary
    summary_sentences = [sentences[i] for i in top_sentence_indices]

    # Join the sentences together to form the summary
    summary = " ".join(summary_sentences)

    return summary

# Use the function to summarize a conversation
summary = summarize_conversation('chat_log_v6.json')
print(summary)
