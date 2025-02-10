from googletrans import Translator
import arabic_reshaper
from bidi.algorithm import get_display

def translate(text, src_lang='en', dest_lang='ur'):
    translator = Translator()
    translated = translator.translate(text, src=src_lang, dest=dest_lang)
    
    # اردو کو صحیح ترتیب دینے کے لیے:
    reshaped_text = arabic_reshaper.reshape(translated.text)
    bidi_text = get_display(reshaped_text)

    return bidi_text