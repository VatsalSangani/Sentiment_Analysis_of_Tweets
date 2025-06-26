# Sentiment Analysis of Tweets

## Description

This project implements a machine learning and deep learning solution for classifying tweets as positive, negative, or neutral. By leveraging neural networks and GloVe word embeddings, the model analyzes tweet text to determine sentiment, providing valuable insights into public opinion on various topics.

---

## Technologies Used

- **Programming Language**: Python
- **Libraries/Frameworks**:
  - TensorFlow
  - Keras
  - NLTK
  - NumPy
  - Pandas
  - Scikit-learn
- **Tools**: Jupyter Notebook

---

## Project Workflow

### 1. Data Collection

- **Datasets**: The repository includes several datasets:
  - `twitter-training-data.txt`
  - `twitter-dev-data.txt`
  - `twitter-test1.txt`
  - `twitter-test2.txt`
  - `twitter-test3.txt`

### 2. Data Preprocessing

- **Text Cleaning**: Removal of special characters, URLs, and unnecessary whitespace.
- **Tokenization**: Splitting text into individual words.
- **Lemmatization**: Reducing words to their base forms.
- **Stop Words Removal**: Eliminating common words that do not contribute to sentiment.

### 3. Feature Extraction

- **Word Embeddings**: Utilization of GloVe embeddings to represent words as vectors. Ensure to download the GloVe embeddings as described in the [Installation](#installation) section.

### 4. Model Building

- **Neural Network Architecture**: Construction of a sequential model with embedding, LSTM, and dense layers for sentiment classification.

### 5. Model Training and Evaluation

- **Training**: Model trained on the preprocessed training dataset.
- **Evaluation**: Performance assessed using accuracy, precision, recall, and F1-score metrics.

---

## Features

- **Comprehensive Data Preprocessing Pipeline**: From raw text to clean, tokenized inputs.
- **Integration of Pre-trained Word Embeddings**: Enhancing model understanding of semantic relationships.
- **Neural Network Implementation**: Employing LSTM layers for sequence processing.
- **Performance Evaluation**: Detailed metrics to assess model effectiveness.

---

## Installation

To set up the project locally:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/VatsalSangani/Sentiment_Analysis_of_Tweets.git


## Dataset

All the data is mentioned in this repository. But you have to download this Glove Word Embedding I am mentioning the steps to do it Download the GloVe word embeddings and map each word in the dataset into its pre-trained GloVe word embedding. First go to "https://nlp.stanford.edu/projects/glove/" and download the pre-trained embeddings from 2014 English Wikipedia into the "data" directory. It's a 822MB zip file named glove.6B.zip, containing 100-dimensional embedding vectors for 400,000 words (or non-word tokens). Un-zip it. Parse the unzipped file (it's a txt file) to build an index mapping words (as strings) to their vector representation (as number vectors). Build an embedding matrix that will be loaded into an Embedding layer later. It must be a matrix of shape (max_words, embedding_dim), where each entry i contains the embedding_dimdimensional vector for the word of index i in our reference word index (built during tokenization). Note that the index 0 is not supposed to stand for any word or token -- it's a placeholder.

---

## DistillBERT Version

I have used the same datasets to train a larger model that is "distillbert-base-uncased" which is deployed in my Hugging Face Spaces and you can 👉 [Click here to try it out](https://huggingface.co/spaces/brendvat/Sentiment_Analysis_from_Twitter_Data).

This model gave me better results which is displayed in README.md File in HF Space.
So try it out.

