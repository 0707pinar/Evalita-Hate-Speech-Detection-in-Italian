# Hate Speech Detection Classifier 
This repository contains hate speech detection classifier built for the Evalita 2018 - Shared Task on Hate Speech Detection in Italian Twitter. More specifically, the hate speech detection classifier introduced here was used in Evalita HaSpeeDe-TW (i.e., subtask I). For  hate  speech  detection  on  Twitter,  LinearSVC-based  model  was used which  was  based  on  unigrams. The model had  penalty  parameter C of  0.7  and  “balanced” class_weight parameter. This classifier ranked 6th  out  of  19  submissions  in  terms  of  macro average  f-score.

# Resources
In order to run the classifier, the following resources are needed.
1. Evalita Twitter Dataset  ==> obtained upon the registration of the shared task
2. NRC Emotion Lexicon (i.e., NRC-Emotion-Lexicon-v0.92-In105Languages-Nov2017Translations.xlsx) ==> obtained upon request (https://www.nrc-cnrc.gc.ca/eng/solutions/advisory/emotion_lexicons.html)

# Scripts
After getting the necessary resources, you can run the following scripts available in this repository:
- *(1) "extract_italian_emolex.py"* ==> to yield the "italian_NRC_emolex.txt" containing Italian emotion and sentiment bearing words along with NRC EmoLex labels. 
- *(2) "evalita_hate_speech_detection_preprocessing.py".* ==> to preprocess the Evalita dataset and to yield labels such as word-level emotion and sentiment labels 
- *(3) "evalita_hate_speech_detection_classifier.py".* ==> The classifier yielded macro average f1-score of 0.78 when run on the test set provided by Evalita.

# References
Cristina  Bosco,   Felice  Dell’Orletta,   Fabio  Poletto,Manuela Sanguinetti, and Maurizio Tesconi.  2018. Overview of the Evalita 2018 Hate Speech Detection Task.   In Proceedings CLiC-it 2018 and EVALITA2018, Torino, Italy, December. AILC.

Saif M Mohammad and Peter D Turney.  2010.  Emotions  evoked  by  common  words  and  phrases:  Using mechanical turk to create an emotion lexicon. In Proceedings of the NAACL HLT 2010 workshop on computational approaches to analysis and generation of emotion in text, pages 26–34. Association forComputational Linguistics.

Saif M Mohammad and Peter D Turney. 2013. Crowdsourcing a word–emotion association lexicon. Computational Intelligence, 29(3):436–465.
