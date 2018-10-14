#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import os
import io
import shutil
import datetime
import ConfigParser

from hermes_python.hermes import Hermes
from hermes_python.ontology import *

from google.cloud import translate
from google.oauth2 import service_account

CONFIGURATION_ENCODING_FORMAT = "utf-8"
CONFIG_INI = "config.ini"

wolfram_api_key = None
google_cloud_api_json_path = None

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


def read_google_credentials():
    filename = os.path.join(os.path.dirname(__file__), 'gca.json')
    if not os.path.exists(filename):
        shutil.copyfile(google_cloud_api_json_path, filename)  
    return service_account.Credentials.from_service_account_file(filename) 


def subscribe_intent_callback(hermes, intentMessage):
    conf = read_configuration_file(CONFIG_INI)
    wolfram_api_key = conf['secret']['wolfram_api_key']
    google_cloud_api_json_path = conf['secret']['google_cloud_api_json_path']
    print(wolfram_api_key)
    print(google_cloud_api_json_path)
    action_wrapper(hermes, intentMessage)

		
def action_wrapper(hermes, intentMessage):
    translator = translate.Client(credentials=read_google_credentials())
    question = translator.translate('who is the leader of china?', target_language='de')
    result_sentence = question['translatedText']
    current_session_id = intentMessage.session_id
    hermes.publish_end_session(current_session_id, result_sentence)
	

if __name__ == "__main__":
    with Hermes("localhost:1883") as h:
        h.subscribe_intent("RumoOr:question", subscribe_intent_callback).start()