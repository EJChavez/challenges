from translate import Translator
translator = Translator(to_lang='ja')
translation = translator.translate('This is a pen')
print(translation)

try:
    with open(r'C:\Users\Ethan\Desktop\translate.txt', mode='r+') as my_file:
        text = my_file.read()
        print(translator.translate(text))
except FileNotFoundError as err:
    print('wrong file path idiot.')
