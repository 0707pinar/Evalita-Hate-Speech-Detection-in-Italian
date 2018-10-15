# Hate Speech Detection Classifier 
This repository contains hate speech detection classifier built for the Evalita 2018 - Shared Task on Hate Speech Detection in Italian Twitter. More specifically, the hate speech detection classifier introduced here was used in Evalita HaSpeeDe-TW (i.e., subtask I) so that this detected hate speech in Italian tweets. This classifier ranked 6th  out  of  19  submissions  in  terms  of  macro average  f-score.
For  hate  speech  detection  on  Twitter,  LinearSVC-based  model  was used which  was  based  on  unigrams. The model had  penalty  parameter C of  0.7  and  “balanced” class_weight parameter. 

# Resources
In order to run the classifier, the following resources are needed.
1. Evalita Twitter Dataset  ==> obtained upon the registration of the shared task
2. NRC Emotion Lexicon (i.e., NRC-Emotion-Lexicon-v0.92-In105Languages-Nov2017Translations.xlsx) ==> obtained upon request (https://www.nrc-cnrc.gc.ca/eng/solutions/advisory/emotion_lexicons.html)

# Scripts
After getting the necessary resources, you can run the use the following scripts available in this repository:
*(1) "extract_italian_emolex.py"* will yield the "italian_NRC_emolex.txt" containing Italian emotion and sentiment bearing words along with NRC EmoLex labels. This txt file is needed for *(2) "evalita_hate_speech_detection_preprocessing.py".* Upon getting "italian_NRC_emolex.txt", you can run *(3) "evalita_hate_speech_detection_classifier.py".*



