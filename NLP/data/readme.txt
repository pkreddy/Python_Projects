About the data science challenge


1)The data is the DailyDialogue dataset, which contains 10,000+ text-based dialogues between two people. A full description of the dataset is here and the data can be downloaded in a single zip file here.

2)Each conversation is a single row in the text file. Each conversation (or row) has multiple (alternating) messages between two speakers. Each message in the conversation is separated by the special delimiter “__eou__”. 

3)Each message in the conversation is labeled both with an intent (e.g. question) and an emotion (e.g. happy). Therefor, you should have as many intent and emotion labels per conversation as there are “__eou__” delimiters. See the README in the zip file for me information.



Here are some explanations about the files:


1) dialogues_text.txt: The DailyDialog dataset which contains 11,318 transcribed dialogues.

2) dialogues_topic.txt: Each line in dialogues_topic.txt corresponds to the topic of that in dialogues_text.txt.

The topic number represents: {1: Ordinary Life, 2: School Life, 3: Culture & Education,
4: Attitude & Emotion, 5: Relationship, 6: Tourism , 7: Health, 8: Work, 9: Politics, 10: Finance}

3) dialogues_act.txt: Each line in dialogues_act.txt corresponds to the dialog act annotations in dialogues_text.txt.
 The dialog act number represents: { 1: inform，2: question, 3: directive, 4: commissive }

4) dialogues_emotion.txt: Each line in dialogues_emotion.txt corresponds to the emotion annotations in dialogues_text.txt.
The emotion number represents: { 0: no emotion, 1: anger, 2: disgust, 3: fear, 4: happiness, 5: sadness, 6: surprise}
5) train.zip, validation.zip and test.zip are two different segmentations of the whole dataset. 
