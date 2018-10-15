#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: pinararslan
Aim: To obtain Italian Emotion and Sentiment Labels by using "NRC-Emotion-Lexicon-v0.92-In105Languages-Nov2017Translations.xlsx"
NRC Emolex Lexicon is available when you contact Saif M. Mohammad (Saif.Mohammad@nrc-cnrc.gc.ca)

1) convert xlsx file to csv
2) get italian words and all emotion&sentiment values
3) get italian words if emotion&sentiment values are 1.0
4) save the output into a txt file --> italian_NRC_emolex.txt
"""

import xlrd
import csv



""" Convert excel file to csv """
def csv_from_excel():
    wb = xlrd.open_workbook('NRC-Emotion-Lexicon-v0.92-In105Languages-Nov2017Translations.xlsx')
    sh = wb.sheet_by_name('NRC-Lex-v0.92-word-translations')
    your_csv_file = open('NRC-Emotion-Lexicon-v0.92-In105Languages-Nov2017Translations.csv', 'w')
    wr = csv.writer(your_csv_file, quoting=csv.QUOTE_ALL)

    for rownum in range(sh.nrows):
        wr.writerow(sh.row_values(rownum))

    your_csv_file.close()

# runs the csv_from_excel function:
csv_from_excel()

# Importing the NRC lexicon in csv format
with open("NRC-Emotion-Lexicon-v0.92-In105Languages-Nov2017Translations.csv") as csvfile:
    italian_words = []
    positive_labels = []
    negative_labels = []
    anger_labels = []
    disgust_labels = []
    fear_labels = []
    joy_labels = []
    sadness_labels = []
    surprise_labels = []
    trust_labels = []
    anticipation_labels = []

    
    reader = csv.DictReader(csvfile)
    title = reader.fieldnames
    for row in reader:
        italian_words.append(row["Italian (it)"])
        positive_labels.append(row["Positive"])
        negative_labels.append(row["Negative"])    
        anger_labels.append(row["Anger"])
        fear_labels.append(row["Fear"])
        joy_labels.append(row["Joy"])
        sadness_labels.append(row["Sadness"])
        surprise_labels.append(row["Surprise"])
        trust_labels.append(row["Trust"])
        disgust_labels.append(row["Disgust"])
        anticipation_labels.append(row["Anticipation"])

# Write a txt file containing only Italian emotion and sentiment bearing words along with their NRC emolex labels
filtered_txt_file = open("italian_NRC_emolex.txt", "w")
italian_words_emolex = []
emolex_labels = []
for i, w in enumerate(italian_words):
    if positive_labels[i] == "1.0":
        labels = "positive"
        emolex_labels.append("positive")
        italian_words_emolex.append(w)
        filtered_txt_file.write("{}\t{}\n".format(w, labels))
    if negative_labels[i] == "1.0":
        labels = "negative"
        emolex_labels.append("negative")
        italian_words_emolex.append(w)
        filtered_txt_file.write("{}\t{}\n".format(w, labels))
    if anger_labels[i] == "1.0":
        labels = "anger"
        emolex_labels.append("anger")
        italian_words_emolex.append(w)
        filtered_txt_file.write("{}\t{}\n".format(w, labels))
    if fear_labels[i] == "1.0":
        labels = "fear"
        emolex_labels.append("fear")
        italian_words_emolex.append(w)
        filtered_txt_file.write("{}\t{}\n".format(w, labels))
    if sadness_labels[i] == "1.0":
        labels = "sadness"
        emolex_labels.append("sadness")
        italian_words_emolex.append(w)
        filtered_txt_file.write("{}\t{}\n".format(w, labels))
    if joy_labels[i] == "1.0":
        labels = "joy"
        emolex_labels.append("joy")
        italian_words_emolex.append(w)
        filtered_txt_file.write("{}\t{}\n".format(w, labels))
    if surprise_labels[i] == "1.0":
        labels = "surprise"
        emolex_labels.append("surprise")
        italian_words_emolex.append(w)
        filtered_txt_file.write("{}\t{}\n".format(w, labels))
    if trust_labels[i] == "1.0":
        labels = "trust"
        emolex_labels.append("trust")
        italian_words_emolex.append(w)
        filtered_txt_file.write("{}\t{}\n".format(w, labels))

    if disgust_labels[i] == "1.0":
        labels = "disgust"
        emolex_labels.append("disgust")
        italian_words_emolex.append(w)
        filtered_txt_file.write("{}\t{}\n".format(w, labels))

    if anticipation_labels[i] == "1.0":
        labels = "anticipation"
        emolex_labels.append("anticipation")
        italian_words_emolex.append(w)
        filtered_txt_file.write("{}\t{}\n".format(w, labels))


filtered_txt_file.close()
