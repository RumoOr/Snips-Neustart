#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import os
import io
import shutil
import datetime
import ConfigParser
import wolframalpha

from hermes_python.hermes import Hermes
from hermes_python.ontology import *

from google.cloud import translate
from google.oauth2 import service_account

CONFIGURATION_ENCODING_FORMAT = "utf-8"
CONFIG_INI = "config.ini"

TEXT_QUESTION_ERROR = 'Ich habe die Frage leider nicht verstanden.'
TEXT_ANSWER_ERROR = 'Dazu habe ich leider keine Antwort.'

class SnipsConfigParser(ConfigParser.SafeConfigParser):
    def to_dict(self):
        return {section : {option_name : option for option_name, option in self.items(section)} for section in self.sections()}


def read_configuration_file(configuration_file):
    try:
        with io.open(configuration_file, encoding=CONFIGURATION_ENCODING_FORMAT) as f:
            conf_parser = SnipsConfigParser()
            conf_parser.readfp(f)
            return conf_parser.to_dict()
    except (IOError, ConfigParser.Error) as e:
        return dict()


def subscribe_intent_callback(hermes, intentMessage):
    config = read_configuration_file(CONFIG_INI)   
    action_wrapper(hermes, intentMessage, config)

		
def action_wrapper(hermes, intentMessage, config):
    waa_key = config['secret']['wolfram_api_key']
    wolfram = wolframalpha.Client(waa_key)
    gca_path = config['secret']['google_cloud_api_json_path']
    credentials = service_account.Credentials.from_service_account_file(gca_path) 
    translator = translate.Client(credentials=credentials)
    question = translator.translate("input message " + intentMessage.input, target_language='de')
    result_sentence = question['translatedText']
    current_session_id = intentMessage.session_id
    hermes.publish_end_session(current_session_id, result_sentence)
	

if __name__ == "__main__":
    with Hermes("localhost:1883") as h:
        h.subscribe_intent("RumoOr:question", subscribe_intent_callback).start()