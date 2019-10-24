from translate import Translator

translator = Translator(to_lang = "ja")

try:
    with open('./test.txt', mode = 'r') as myFile:
        translator = Translator(to_lang = "zh")
        translation = translator.translate(myFile.read())
        print(translation)
except FileNotFoundError as err:
    print('Check your File path!')