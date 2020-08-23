from ibm_watson import NaturalLanguageUnderstandingV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_watson.natural_language_understanding_v1 import Features, EmotionOptions

import json

API_KEY = ''
SERVICE_URL = 'https://gateway-lon.watsonplatform.net/natural-language-understanding/api'

class WatsonLang:
    

    def __init__(self):
        self.authenticator = IAMAuthenticator(API_KEY)
        self.natural_language_understanding = NaturalLanguageUnderstandingV1(
            version='2019-07-12',
            authenticator=self.authenticator
        )
        self.natural_language_understanding.set_service_url(SERVICE_URL)


    def analyze_emotion(self, text):
        response = self.natural_language_understanding.analyze(
            html="<html>{}</html>".format(text),
            features=Features(emotion=EmotionOptions())).get_result()

        return(response["emotion"]["document"]["emotion"])
