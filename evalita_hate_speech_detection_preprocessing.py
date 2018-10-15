#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
SHARED TASK EVALITA HATE SPEECH DETECTION IN ITALIAN
____________________________________________________
Subtask I: HaSpeeDe-TW
Team name: InriaFBK

The following preprocessing steps were followed for Subtask I: HaSpeeDe-TW
"""

import csv
import re
from nltk.stem.snowball import SnowballStemmer
from nltk.corpus import stopwords

# Read Evalita data, get texts and labels
def read_evalita_data(dataset): 
    with open(dataset) as tsvfile:
        hate_speech_labels = []
        tweets = []
        reader = csv.reader(tsvfile, delimiter='\t')
        for row in reader:
            hate_speech_labels.append(row[-1])
            tweets.append(row[1])
    return tweets, hate_speech_labels

# Read Evalita data, get ids, texts
def read_evalita_testdata(dataset): 
    with open(dataset) as tsvfile:
        tweet_ids = []
        tweets = []
        reader = csv.reader(tsvfile, delimiter='\t')
        for row in reader:
            tweet_ids.append(row[0])
            tweets.append(row[1])
    return tweets, tweet_ids


def tag_URLs(texts):
    # URLs are shown with URL tag
    texts_with_URLabels = []
    for t in texts:
        text = re.sub('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', 'URL', t)
        texts_with_URLabels.append(text)
    return texts_with_URLabels

def remove_abundant_new_line_symbols(text_in_list):
    # This removes unnecessary newline symbols in the texts
    text_without_newline_symbols = [] 
    for line in text_in_list:
    
        	line_string = "".join(line)
        	rexp_string = r'\\n+'
        	tags_created_rexp = re.compile(rexp_string)
        	text_cleaned = tags_created_rexp.sub(" ",line_string)
        	text_without_newline_symbols.append(text_cleaned)
    return text_without_newline_symbols

def remove_hashtag_symbols(text_in_list):
    # This deletes hashtag symbols
    # e.g. #calm becomes calm
    text_without_hashtag_symbols = [] 
    for line in text_in_list:
    
        	line = line.strip().split()
        	line_string = " ".join(line)
        	rexp_string = r'#'
        	tags_created_rexp = re.compile(rexp_string)
        	text_cleaned = tags_created_rexp.sub(" ",line_string)
        	text_without_hashtag_symbols.append(text_cleaned)
    return text_without_hashtag_symbols

def add_whitespace_before_and_after_punctuation(text_in_list):
    # This puts a whitespace before and after punctuation """
    selected_punctuations = '!\"#$%&()*+,_-./:;<=>?[\]^`{|}~'
    text_with_space_before_after_punctuation = []

    for line in text_in_list:
        text_with_space_before_after_punctuation.append(["".join(line).translate(str.maketrans({key: " {0} ".format(key) for key in selected_punctuations}))])

    tokenized_text_with_space_before_after_punctuation = []
    for line in text_with_space_before_after_punctuation:
        tokenized_text_with_space_before_after_punctuation.append("".join(line).strip().split())
        
    return tokenized_text_with_space_before_after_punctuation

def remove_italian_stopwords(texts):
    stopWords = set(stopwords.words('italian'))
    X_noStopWords = []
    for x in texts:
        wordsFiltered = []
        for w in x:
            if w not in stopWords:
                wordsFiltered.append(w)
        X_noStopWords.append(wordsFiltered)
    return X_noStopWords

def tag_usernames(text_in_list):
    # This puts a placeholder for usernames
    # @melanie becomes USERNAME 
    text_with_tagged_usernames = [] 
    for line in text_in_list:
        line_string = " ".join(line)
        rexp_string = r'(?<=^|(?<=[^a-zA-Z0-9-_\.]))@([_A-Za-z0-9-_]+[A-Za-z0-9-_]+)'
        tags_created_rexp = re.compile(rexp_string)
        text_cleaned = tags_created_rexp.sub("USERNAME",line_string)
        text_with_tagged_usernames.append(text_cleaned.split())
    return text_with_tagged_usernames

def read_emolex_italian(corpus_file): 
    # This reads the filtered italian emolex lexicon (NRC EmoLex)
    # This puts emolex words and labels in lists
    lexicon = []  
    labels = []  
    
    with open(corpus_file, encoding='utf-8') as f: 
        for line in f: 
            tokens = line.strip().split("\t")
            emo_pol_labels = "".join(tokens[1])
            words = "".join(tokens[0])
                
            labels.append(emo_pol_labels)
            lexicon.append(words)
                    
    return lexicon, labels

def extract_italian_emolex_emotion_sentiment_words():
    # This reads the italian emolex text file with Italian emolex words
    #                                                       and emolex labels
    # The filtered file contains only emolex words and labels with binary value "1"
    # This function creates word lists for each emotion and sentiment label in Italian

    words, emo_pol_labels = read_emolex_italian("italian_NRC_emolex.txt")
    
    anger_words = []
    fear_words = []
    joy_words = []
    sadness_words = []
    trust_words = []
    disgust_words = []
    surprise_words = []
    anticipation_words = []
    positive_words = []
    negative_words = []

    for i,l in enumerate(emo_pol_labels):
        if l == "anger":
            anger_words.append(words[i])
        if l == "fear":
            fear_words.append(words[i])
        if l == "sadness":
            sadness_words.append(words[i])
        if l == "joy":
            joy_words.append(words[i])
        if l == "positive":
            positive_words.append(words[i])
        if l == "negative":
            negative_words.append(words[i])
        if l == "trust":
            trust_words.append(words[i])
        if l == "disgust":
            disgust_words.append(words[i])
        if l == "surprise":
            surprise_words.append(words[i])
        if l == "anticipation":
            anticipation_words.append(words[i])       
        
    return anger_words, fear_words,joy_words,sadness_words,positive_words,negative_words, trust_words, surprise_words, anticipation_words, disgust_words

            
def stemming_italian_words_with_emolex_labels(text_in_list):
    # This calls the function "extract_italian_emolex_emotion_polarity_words"
    # to get the Italian emotion and sentiment words 
    # This tags numbers with "NUMBER" tag
    # Each emolex label (i.e. 10 labels) are tagged (e.g. _ANGER_, _JOY_)
    # Each word is then stemmed
    # Finally each text is shown with stemmed words, emolex and number tags
    italian_stemmer = SnowballStemmer("italian")
    anger_words, fear_words,joy_words,sadness_words,positive_words,negative_words, trust_words, surprise_words, anticipation_words, disgust_words = extract_italian_emolex_emotion_sentiment_words()
        
    text_with_emolex_labelled_stemmed_words = []
    
    
    for line in text_in_list:
        
        numbers = re.findall(r"([0-9]+)"," ".join(line))
        X_sentences = []
        
        for w in line:
        
            new_sentences = []
            lowered_words = w.lower()
            stemmed_words = italian_stemmer.stem(w)
    
        
            if lowered_words in anger_words:
                label = "_ANGER_" 
                new_sentences.append(label)
                
            if lowered_words in sadness_words:
                label = "_SADNESS_"
                new_sentences.append(label)
    
            if lowered_words in joy_words:
                label = "_JOY_"
                new_sentences.append(label)
            
            if lowered_words in fear_words:
                label = "_FEAR_"
                new_sentences.append(label)
                
            if lowered_words in trust_words:
                label = "_TRUST_"
                new_sentences.append(label)
                
            if lowered_words in surprise_words:
                label = "_SURPRISE_"
                new_sentences.append(label)
            
            if lowered_words in anticipation_words:
                label = "_ANTICIPATION_"
                new_sentences.append(label)
            
            if lowered_words in disgust_words:
                label = "_DISGUST_"
                new_sentences.append(label)
                
            if lowered_words in positive_words:
                label = "_POSITIVE_"
                new_sentences.append(label)
            
            if lowered_words in negative_words:
                label = "_NEGATIVE_"
                new_sentences.append(label)
                
            if stemmed_words in numbers:
                label = "NUMBER"
                new_sentences.append(label)
                
            
            if stemmed_words not in numbers:
                new_sentences.append(stemmed_words)
                        
            X_sentences = X_sentences + new_sentences
        text_with_emolex_labelled_stemmed_words.append(X_sentences)
        
    return text_with_emolex_labelled_stemmed_words

def preprocess_evalita_data(dataset):
    Xraw, y = read_evalita_data(dataset)
    X = remove_italian_stopwords(stemming_italian_words_with_emolex_labels(tag_usernames(add_whitespace_before_and_after_punctuation(remove_hashtag_symbols(remove_abundant_new_line_symbols(tag_URLs(Xraw)))))))
    return X, y