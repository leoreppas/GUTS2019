import numpy as np
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis as lda
from lda_analysis.readCsv import process as csv
from src import watson

class LDAThresh:
    def __init__(self,file):
        self.file = file

    def threshold_model(self):
        text,labels = csv(self.file)
        emotion_analysis = watson.WatsonLang()
        emotions = []
        for i in text:
            emo_json = emotion_analysis.analyze_emotion(i)
            emo = list(emo_json.values())
            emotions.append(emo)
        model = lda()
        model.fit(emotions,labels)
        return(model)