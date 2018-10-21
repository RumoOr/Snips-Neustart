# -*- coding: utf-8 -*-

import wolframalpha

from google.cloud import translate
from google.oauth2 import service_account

TEXT_QUESTION_ERROR = 'Ich habe die Frage leider nicht verstanden.'
TEXT_ANSWER_ERROR = 'Dazu habe ich leider keine Antwort.'

class Omniscient:
    def __init__(self, config):
        self.wolfram_key = ""
        self.google_key_path = ""
        try:
            self.wolfram_key = config['secret']['wolfram_api_key']
        except KeyError:
            self.wolfram_key = "XXXXXXXXXX"
        try:
            self.google_key_path = config['secret']['google_cloud_api_json_path']
        except KeyError:
            self.google_key_path = "XXXXXXXXXX"            
        credentials = service_account.Credentials.from_service_account_file(self.google_key_path) 
        self.translator = translate.Client(credentials=credentials)
        self.wolfram = wolframalpha.Client(self.wolfram_key)

    def get_answer(self, question):       
        try: 
            question = self.translator.translate('wer war der erste bundeskanzler von deutschland', target_language='en')
            print(question['translatedText'])
            params = (
                ('format', 'plaintext'),
                ('includepodid', 'Result'),
                ('podindex', '1'),
                ('units', 'metric'),
                ('async', 'false'),
            )
            res = self.wolfram.query(input=question['translatedText'], params=params)
            print('wolfram returned: ' + res['@success'])           
            text = TEXT_QUESTION_ERROR          
            if res['@success'] == 'true':
                text = res['pod']['subpod']['plaintext']                     
                text = text.replace(' |' , ',')
                for c in ['(', '[']:
                    if c in text: 
                        text = next(iter(text.split(c, 1)))
                text = text.rstrip()          
                if (text == ''): 
                    text = TEXT_ANSWER_ERROR
                else:
                    text = self.translator.translate(text, source_language='en', target_language='de')['translatedText']
            return text
        except:
            return TEXT_QUESTION_ERROR    