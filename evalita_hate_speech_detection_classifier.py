#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
TASK EVALITA-2018 HATE SPEECH DETECTION IN ITALIAN
__________________________________________________
@inproceedings{HaSpeeDe2018Evalita,
  author    = {Bosco, Cristina  and Dell'Orletta, Felice and  Poletto, Fabio  and  Sanguinetti, Manuela and Tesconi, Maurizio},
  title     = {{Overview of the Evalita 2018 Hate Speech Detection Task}},
  booktitle = {Proceedings CLiC-it 2018 and EVALITA 2018},
  month     = {December},
  year      = {2018},
  address   = {Torino, Italy},
  publisher = {AILC}
}

Team name: InriaFBK
Subtask I: HaSpeeDe-TW
The following LinearSVC-based classifier was used in Subtask I: HaSpeeDe-TW

"""


from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.svm import LinearSVC
from sklearn.pipeline import Pipeline
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
from sklearn.metrics import precision_recall_fscore_support
from collections import defaultdict
from evalita_hate_speech_detection_preprocessing import preprocess_evalita_data 

# Preprocess Twitter Development Set 
dataset = 'haspeede_TW-train.tsv'
X, y = preprocess_evalita_data(dataset)


# This shows the label distributions in Twitter Development Set 
def label_distribution(labels):
    label_count = defaultdict(int)
    for l in labels:
        label_count[l] += 1
    return label_count

print("Development set label distribution:", label_distribution(y))

       
# This splits the data (i.e., Twitter Development Set) into a training set(60%), a validation set(20%) and a test set(20%)
X_train, X_val_test, y_train, y_val_test = train_test_split(X, y, test_size=0.40, random_state=42)
X_val, X_test, y_val, y_test = train_test_split(X_val_test,y_val_test, test_size=0.50, shuffle=False)


# This is for a dummy tokenizer and preprocessor to be used in TfidfVectorizer 
# since we already tokenized and preprocessed our data.
def identity(x):
    return x

tfidf = True


if tfidf:
    vec = TfidfVectorizer(preprocessor = identity,
                          tokenizer = identity,
                          ngram_range=(1,1))

                         
else:
    vec = CountVectorizer(preprocessor = identity,
                          tokenizer = identity)


# This creates LinearSVC classifier 
cls = LinearSVC(random_state=0,class_weight="balanced", C = 0.7)


# This combines the vectorizer with the Linear Support Vector Classification Algorithm
classifier = Pipeline( [('vec', vec),
                        ('cls', cls)])


# This fits the model for training set (60% of X)
classifier.fit(X_train, y_train)


# This predicts the labels for training, validation and test sets  
Yguess_train = classifier.predict(X_train)
Yguess_validation  = classifier.predict(X_val)
Yguess_test  = classifier.predict(X_test)

# This evaluates the performance of the classifier of hate speech detection for training, validation and test sets
print("The model has been run on 'Evalita Twitter Development Dataset'")
print("The results of Training Set (%60 of X)")
print("_" * 30)
print("Classification report of the training set:\n", classification_report(y_train, Yguess_train)) # This will give us precision, recall,f score for each class as well as the average precision, recall and f score among classes. This will give us the total number of each class existing in the training set as well. 
print("Confusion matrix:\n",confusion_matrix(y_train, Yguess_train))
print("Accuracy Score:\n",accuracy_score(y_train, Yguess_train))
print("macro avg:\n",precision_recall_fscore_support(y_train, Yguess_train, average="macro"))
print("micro avg:\n",precision_recall_fscore_support(y_train, Yguess_train, average="micro"))


print("The results of Validation Set (%20 of X)")
print("_" * 30)
print("Classification report of the validation set: \n ",classification_report(y_val, Yguess_validation)) # This will give us precision, recall,f score for each class as well as the average precision, recall and f score among classes. This will give us the total number of each class existing in the validation set as well. 
print("Confusion matrix:\n",confusion_matrix(y_val,Yguess_validation))
print("Accuracy:\n",accuracy_score(y_val,Yguess_validation))
print("macro avg:\n",precision_recall_fscore_support(y_val, Yguess_validation, average="macro"))
print("micro avg:\n",precision_recall_fscore_support(y_val, Yguess_validation, average="micro"))


print("The results of Test Set (%20 of X)")
print("_" * 30)
print("Classification report of the test set: \n ",classification_report(y_test, Yguess_test)) # This will give us precision, recall,f score for each class as well as the average precision, recall and f score among classes. This will give us the total number of each class existing in the testset as well. 
print("Confusion matrix:\n",confusion_matrix(y_test,Yguess_test))
print("Accuracy:\n",accuracy_score(y_test,Yguess_test))
print("macro avg:\n",precision_recall_fscore_support(y_test, Yguess_test, average="macro"))
print("micro avg:\n",precision_recall_fscore_support(y_test, Yguess_test, average="micro"))
