from translate import Translator
translator= Translator(from_lang="chinese",to_lang="english")
translation = translator.translate("发行计划")
translation=translation[0].lower()+translation[1:]
list1=translation.split()
translation='_'.join(list1)
print(translation)