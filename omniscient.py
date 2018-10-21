# -*- coding: utf-8 -*-

import os
import io
import datetime
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

    def get_answer(self, question):
        try: 
            question = self.translator.translate("input message " + question, target_language='de')
            return question['translatedText']
        except:
            return TEXT_QUESTION_ERROR  
  