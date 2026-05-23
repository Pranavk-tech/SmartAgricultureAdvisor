from deep_translator import GoogleTranslator

language_map={

"English":"en",
"Hindi":"hi",
"Kannada":"kn",
"Tamil":"ta",
"Telugu":"te",
"Malayalam":"ml",
"Marathi":"mr",
"Gujarati":"gu",
"Punjabi":"pa",
"Bengali":"bn",
"Odia":"or",
"Urdu":"ur",
"Assamese":"as",
"Konkani":"gom",
"Sanskrit":"sa",
"Kashmiri":"ks",
"Manipuri":"mni",
"Nepali":"ne"

}

def translate_text(text,language):

    if language=="English":
        return text

    try:

        translated=GoogleTranslator(
            source="auto",
            target=language_map[language]
        ).translate(text)

        return translated

    except:

        return text