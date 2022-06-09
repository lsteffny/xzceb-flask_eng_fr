"""
This module is used to translate textstrings from english to french and french to englisch
"""

import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']
version_lt=os.environ['version']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(version=version_lt,authenticator=authenticator)
language_translator.set_service_url(url)


def translate(text_string, model_id):
    """
    :param engtext_string:
    :param model_id:
    """
    translation_response = language_translator.translate(text=text_string, model_id=model_id)
    translation=translation_response.get_result()
    return translation['translations'][0]['translation']


def english_to_french(english_text):
    """
    :param englisch_text:
    """
    #write the code here
    french_text = translate(text_string=english_text, model_id='en-fr')
    return french_text


def french_to_english(french_text):
    """
    :param french_text:
    """
    #write the code here
    french_text = translate(text_string=french_text, model_id='fr-en')
    return french_text
