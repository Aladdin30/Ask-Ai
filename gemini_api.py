import google.generativeai as genai
import os
from deep_translator import GoogleTranslator
from capture_voice import get_audio
from PIL import Image
from dotenv import dotenv_values
from tts import voice_cloning,split_text
GEMINI_KEY = dotenv_values('.env').get('gemini_api')

genai.configure(api_key='AIzaSyAzpGtYoTPejKxBObs1N2w9o3ghFYC6hEw')

model =  genai.GenerativeModel("gemini-pro")
vision_model = genai.GenerativeModel("models/gemini-pro-vision")

def gemini_response(query):
    en_translated_query = GoogleTranslator(source='auto', target='en').translate(query)

    response = model.generate_content("Answery briefly, \n" + en_translated_query).text

    ar_translated_rsponse = GoogleTranslator(source='auto', target='ar').translate(response)

    return ar_translated_rsponse


def All():
    query=get_audio(lang='ar')
    print(query)
    responed=gemini_response(query)
    print(responed)
    chunks=split_text(responed)
    result=voice_cloning(chunks)
    return result
All()