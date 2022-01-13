import translate
from translate import Translator

translator = Translator(to_lang="pl", from_lang='ru')
translation = translator.translate("Люди на самом деле прекрасно знают, что надо экономить.")
print(translation)
