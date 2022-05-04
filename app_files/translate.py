import xml.etree.ElementTree as ET
from bs4 import BeautifulSoup
import re
from googletrans import Translator
# pip install googletrans==4.0.0rc1
from bs4 import BeautifulSoup
from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, BooleanField, SubmitField, TextAreaField, PasswordField, RadioField
from wtforms.validators import InputRequired, URL
from app_files.secret import get_key

from deep_translator import (
		GoogleTranslator,
		MicrosoftTranslator,
		PonsTranslator,
		LingueeTranslator,
		MyMemoryTranslator,
		YandexTranslator,
		DeeplTranslator,
		QcriTranslator    
)
from deep_translator.exceptions import ServerException, TooManyRequests, RequestError

#	elif t_gear == 'LibreTranslator':
#	supp_lang_list = {'English': 'en', 'Arabic': 'ar', 'Azerbaijani': 'az', 'Chinese': 'zh', 'Czech': 'cs', 'Dutch': 'nl', 'Finnish': 'fi', 'French': 'fr', 'German': 'de', 'Hindi': 'hi', 'Hungarian': 'hu', 'Indonesian': 'id', 'Irish': 'ga', 'Italian': 'it', 'Japanese': 'ja', 'Korean': 'ko', 'Polish': 'pl', 'Portuguese': 'pt', 'Russian': 'ru', 'Spanish': 'es', 'Swedish': 'sv', 'Turkish': 'tr', 'Ukranian': 'uk', 'Vietnamese': 'vi'}
		
translator = Translator()
class ltr_gears_lang_list():
	gears_lang_list = {
		'mymemory': {'afrikaans': 'af','albanian': 'sq','amharic': 'am','arabic': 'ar','armenian': 'hy','azerbaijani': 'az','basque': 'eu','belarusian': 'be','bengali': 'bn','bosnian': 'bs','bulgarian': 'bg','catalan': 'ca','cebuano': 'ceb','chichewa': 'ny','chinese (simplified)': 'zh-CN','chinese (traditional)': 'zh-TW','corsican': 'co','croatian': 'hr','czech': 'cs','danish': 'da','dutch': 'nl','english': 'en','esperanto': 'eo','estonian': 'et','filipino': 'tl','finnish': 'fi','french': 'fr','frisian': 'fy','galician': 'gl','georgian': 'ka','german': 'de','greek': 'el','gujarati': 'gu','haitian creole': 'ht','hausa': 'ha','hawaiian': 'haw','hebrew': 'iw','hindi': 'hi','hmong': 'hmn','hungarian': 'hu','icelandic': 'is','igbo': 'ig','indonesian': 'id','irish': 'ga','italian': 'it','japanese': 'ja','javanese': 'jw','kannada': 'kn','kazakh': 'kk','khmer': 'km','kinyarwanda': 'rw','korean': 'ko','kurdish': 'ku','kyrgyz': 'ky','lao': 'lo','latin': 'la','latvian': 'lv','lithuanian': 'lt','luxembourgish': 'lb','macedonian': 'mk','malagasy': 'mg','malay': 'ms','malayalam': 'ml','maltese': 'mt','maori': 'mi','marathi': 'mr','mongolian': 'mn','myanmar': 'my','nepali': 'ne','norwegian': 'no','odia': 'or','pashto': 'ps','persian': 'fa','polish': 'pl','portuguese': 'pt','punjabi': 'pa','romanian': 'ro','russian': 'ru','samoan': 'sm','scots gaelic': 'gd','serbian': 'sr','sesotho': 'st','shona': 'sn','sindhi': 'sd','sinhala': 'si','slovak': 'sk','slovenian': 'sl','somali': 'so','spanish': 'es','sundanese': 'su','swahili': 'sw','swedish': 'sv','tajik': 'tg','tamil': 'ta','tatar': 'tt','telugu': 'te','thai': 'th','turkish': 'tr','turkmen': 'tk','ukrainian': 'uk','urdu': 'ur','uyghur': 'ug','uzbek': 'uz','vietnamese': 'vi','welsh': 'cy','xhosa': 'xh','yiddish': 'yi','yoruba': 'yo','zulu': 'zu'},
		'google': {'afrikaans': 'af','albanian': 'sq','amharic': 'am','arabic': 'ar','armenian': 'hy','azerbaijani': 'az','basque': 'eu','belarusian': 'be','bengali': 'bn','bosnian': 'bs','bulgarian': 'bg','catalan': 'ca','cebuano': 'ceb','chichewa': 'ny','chinese (simplified)': 'zh-CN','chinese (traditional)': 'zh-TW','corsican': 'co','croatian': 'hr','czech': 'cs','danish': 'da','dutch': 'nl','english': 'en','esperanto': 'eo','estonian': 'et','filipino': 'tl','finnish': 'fi','french': 'fr','frisian': 'fy','galician': 'gl','georgian': 'ka','german': 'de','greek': 'el','gujarati': 'gu','haitian creole': 'ht','hausa': 'ha','hawaiian': 'haw','hebrew': 'iw','hindi': 'hi','hmong': 'hmn','hungarian': 'hu','icelandic': 'is','igbo': 'ig','indonesian': 'id','irish': 'ga','italian': 'it','japanese': 'ja','javanese': 'jw','kannada': 'kn','kazakh': 'kk','khmer': 'km','kinyarwanda': 'rw','korean': 'ko','kurdish': 'ku','kyrgyz': 'ky','lao': 'lo','latin': 'la','latvian': 'lv','lithuanian': 'lt','luxembourgish': 'lb','macedonian': 'mk','malagasy': 'mg','malay': 'ms','malayalam': 'ml','maltese': 'mt','maori': 'mi','marathi': 'mr','mongolian': 'mn','myanmar': 'my','nepali': 'ne','norwegian': 'no','odia': 'or','pashto': 'ps','persian': 'fa','polish': 'pl','portuguese': 'pt','punjabi': 'pa','romanian': 'ro','russian': 'ru','samoan': 'sm','scots gaelic': 'gd','serbian': 'sr','sesotho': 'st','shona': 'sn','sindhi': 'sd','sinhala': 'si','slovak': 'sk','slovenian': 'sl','somali': 'so','spanish': 'es','sundanese': 'su','swahili': 'sw','swedish': 'sv','tajik': 'tg','tamil': 'ta','tatar': 'tt','telugu': 'te','thai': 'th','turkish': 'tr','turkmen': 'tk','ukrainian': 'uk','urdu': 'ur','uyghur': 'ug','uzbek': 'uz','vietnamese': 'vi','welsh': 'cy','xhosa': 'xh','yiddish': 'yi','yoruba': 'yo','zulu': 'zu'},
		'yandex': {'afrikaans': 'af', 'albanian': 'sq', 'amharic': 'am', 'arabic': 'ar', 'armenian': 'hy', 'azerbaijani': 'az', 'bashkir': 'ba', 'basque': 'eu', 'belarusian': 'be', 'bengali': 'bn', 'bosnian': 'bs', 'bulgarian': 'bg', 'burmese': 'my', 'catalan': 'ca', 'cebuano': 'ceb', 'chinese': 'zh', 'chuvash': 'cv', 'croatian': 'hr', 'czech': 'cs', 'danish': 'da', 'dutch': 'nl', 'elvish (sindarin)': 'sjn', 'emoji': 'emj', 'english': 'en', 'esperanto': 'eo', 'estonian': 'et', 'finnish': 'fi', 'french': 'fr', 'galician': 'gl', 'georgian': 'ka', 'german': 'de', 'greek': 'el', 'gujarati': 'gu', 'haitian': 'ht', 'hebrew': 'he', 'hill mari': 'mrj', 'hindi': 'hi', 'hungarian': 'hu', 'icelandic': 'is', 'indonesian': 'id', 'irish': 'ga', 'italian': 'it', 'japanese': 'ja', 'javanese': 'jv', 'kannada': 'kn', 'kazakh': 'kk', 'kazakh (latin)': 'kazlat', 'khmer': 'km', 'korean': 'ko', 'kyrgyz': 'ky', 'lao': 'lo', 'latin': 'la', 'latvian': 'lv', 'lithuanian': 'lt', 'luxembourgish': 'lb', 'macedonian': 'mk', 'malagasy': 'mg', 'malay': 'ms', 'malayalam': 'ml', 'maltese': 'mt', 'maori': 'mi', 'marathi': 'mr', 'mari': 'mhr', 'mongolian': 'mn', 'nepali': 'ne', 'norwegian': 'no', 'papiamento': 'pap', 'persian': 'fa', 'polish': 'pl', 'portuguese': 'pt', 'punjabi': 'pa', 'romanian': 'ro', 'russian': 'ru', 'scottish gaelic': 'gd', 'serbian': 'sr', 'sinhalese': 'si', 'slovak': 'sk', 'slovenian': 'sl', 'spanish': 'es', 'sundanese': 'su', 'swahili': 'sw', 'swedish': 'sv', 'tagalog': 'tl', 'tajik': 'tg', 'tamil': 'ta', 'tatar': 'tt', 'telugu': 'te', 'thai': 'th', 'turkish': 'tr', 'udmurt': 'udm', 'ukrainian': 'uk', 'urdu': 'ur', 'uzbek': 'uz', 'uzbek (cyrillic)': 'uzbcyr', 'vietnamese': 'vi', 'welsh': 'cy', 'xhosa': 'xh', 'yakut': 'sah', 'yiddish': 'yi', 'zulu': 'zu'},
		'microsoft': {'afrikaans': 'af','amharic': 'am','arabic': 'ar','assamese': 'as','azerbaijani': 'az','bashkir': 'ba','bulgarian': 'bg','bangla': 'bn','tibetan': 'bo','bosnian': 'bs','catalan': 'ca','czech': 'cs','welsh': 'cy','danish': 'da','german': 'de','divehi': 'dv','greek': 'el','english': 'en','spanish': 'es','estonian': 'et','basque': 'eu','persian': 'fa','finnish': 'fi','filipino': 'fil','fijian': 'fj','faroese': 'fo','french': 'fr','french (canada)': 'fr-ca','irish': 'ga','galician': 'gl','gujarati': 'gu','hebrew': 'he','hindi': 'hi','croatian': 'hr','upper sorbian': 'hsb','haitian creole': 'ht','hungarian': 'hu','armenian': 'hy','indonesian': 'id','inuinnaqtun': 'ikt','icelandic': 'is','italian': 'it','inuktitut': 'iu','inuktitut (latin)': 'iu-latn','japanese': 'ja','georgian': 'ka','kazakh': 'kk','khmer': 'km','kurdish (northern)': 'kmr','kannada': 'kn','korean': 'ko','kurdish (central)': 'ku','kyrgyz': 'ky','lao': 'lo','lithuanian': 'lt','latvian': 'lv','chinese (literary)': 'lzh','malagasy': 'mg','māori': 'mi','macedonian': 'mk','malayalam': 'ml','mongolian (cyrillic)': 'mn-cyrl','mongolian (traditional)': 'mn-mong','marathi': 'mr','malay': 'ms','maltese': 'mt','hmong daw': 'mww','myanmar (burmese)': 'my','norwegian': 'nb','nepali': 'ne','dutch': 'nl','odia': 'or','querétaro otomi': 'otq','punjabi': 'pa','polish': 'pl','dari': 'prs','pashto': 'ps','portuguese (brazil)': 'pt','portuguese (portugal)': 'pt-pt','romanian': 'ro','russian': 'ru','slovak': 'sk','slovenian': 'sl','samoan': 'sm','somali': 'so','albanian': 'sq','serbian (cyrillic)': 'sr-cyrl','serbian (latin)': 'sr-latn','swedish': 'sv','swahili': 'sw','tamil': 'ta','telugu': 'te','thai': 'th','tigrinya': 'ti','turkmen': 'tk','klingon (latin)': 'tlh-latn','klingon (piqad)': 'tlh-piqd','tongan': 'to','turkish': 'tr','tatar': 'tt','tahitian': 'ty','uyghur': 'ug','ukrainian': 'uk','urdu': 'ur','uzbek (latin)': 'uz','vietnamese': 'vi','yucatec maya': 'yua','cantonese (traditional)': 'yue','chinese simplified': 'zh-hans','chinese traditional': 'zh-hant','zulu': 'zu'},
		'deepl': {'bulgarian': 'bg','czech': 'cs','danish': 'da','german': 'de','greek': 'el','english': 'en','spanish': 'es','estonian': 'et','finnish': 'fi','french': 'fr','hungarian': 'hu','italian': 'it','japanese': 'ja','lithuanian': 'lt','latvian': 'lv','dutch': 'nl','polish': 'pl','portuguese': 'pt','romanian': 'ro','russian': 'ru','slovak': 'sk','slovenian': 'sl','swedish': 'sv','chinese': 'zh'},
		'pons': {'english': 'en', 'french': 'fr', 'german': 'de', 'greek': 'el', 'italian': 'it', 'polish': 'pl', 'portuguese': 'pt', 'russian': 'ru', 'slovenian': 'sl', 'spanish': 'es', 'turkish': 'tr'}
	}

	shortllist = []
	longllist = []
	gvlist = []
	gklist = []
	lang_list = []
	gfulllist = dict()
	for k,v in gears_lang_list.items():
		tuple_list = v.items()
		for t1,t2 in tuple_list:
			lang_list.append((t2,t1))

		gfulllist[k] = v
		gvlist.append(k)
		gklist.append(v)
		gvlist.append(list(v.values()))
		gklist.append(list(v.keys()))
		for l in list(v.values()):
			shortllist.append(l)
		for l in list(v.keys()):
			longllist.append(l)
	
	form_lang_list = sorted(set(lang_list))
	gears_shortlist = sorted(set(shortllist))
	gears_longlist = sorted(set(longllist))
	gears_countrylist = gklist
	gears_langlist = gvlist
	
class ltr_gears_list():
	gears_list = [
	 	('mymemory',('MyMemory Translator','free')),
		('google',('Google Translator','free')),
		('yandex',('Yandex Translator','pay')),
		('microsoft',('Microsoft Translator','pay')),
		('deepl',('Deepl Translator','pay')),
		('pons',('Pons Translator','pay')),
		('compare',('Compare Translators',''))
	]  
	gears2_dict = dict()
	for v in gears_list:
		gears2_dict[str(v[1][0]).replace(' ','')] = v[0]
  
# Forms class
class ltr_form(FlaskForm):

	gears_list = ltr_gears_list.gears_list
	lang_list = ltr_gears_lang_list.form_lang_list
 	# [
	# 	('pl','Polski'),
	# 	('en','Angielski'),
	# 	('uk','Ukraiński')
	# ]
	text = 'Wklej tekst do tłumaczenia'
	ltr_textarea = TextAreaField(text)
	ltr_lang_from = SelectField('Z języka', default='pl', choices=lang_list)
	rev_lang_list = sorted(dict(lang_list).items(), key=lambda x: x[1])
	ltr_lang_to = SelectField('Na język', default='uk', choices=rev_lang_list)
	#gear_list.append('Porównaj ')
	ltr_gears = RadioField('', choices=gears_list)
	yt = StringField('Link do YouTube')
 
	button = SubmitField('Tłumacz')

def gears_list():
	return ltr_gears_list.gears_list

def xml_file(from_lang,file_path=''):

	print('==================== START Translate ==================================')

	file_name_input = 'acs-subsite.pl_PL.utf-8.xml' #'acs-lang.en_GB.ISO-8859-1.xml'
	with open(file_name_input, 'r') as f:
		lines_list = f.readlines()
	mc = BeautifulSoup(lines_list[1], features="lxml").message_catalog
	
	package_key = mc['package_key']
	locale = mc['locale']
	charset = mc['charset']
	ouput_lang = 'uk_UA'
 
	print(package_key, locale, charset)
	file_name_output = package_key+'.'+ouput_lang+'.'+charset+'.xml'
	dest_lang='uk'
	src_lang='pl'

	html_list = []
	nof_list = []
	nof_list.append('<?xml version="1.0" encoding="'+charset+'"?>')
	nof_list.append('<message_catalog package_key="'+package_key+'" package_version="5.3.0d1" locale="'+ouput_lang+'" charset="'+charset+'">')
	nof_list.append('')
	
	import xml.etree.ElementTree as ET
	root = ET.parse(file_name_input).getroot()
	licz = 0
	for type_tag in root.findall('*'):
		try:
			tag = type_tag.tag
			key = type_tag.get('key')
			val = type_tag.text
			if val != None:
				if licz%50 == 1:
					print(licz,'.\t',val.lower(), licz%50)
				translated = translator.translate(val, dest=dest_lang, src=src_lang)
				if BeautifulSoup(val, "html.parser").find():
					nof_list.append('\t<'+tag+' key="'+key+'"><![CDATA['+translated.text+']]></'+tag+'>')
					html_list.append('\t<'+tag+' key="'+key+'">'+val+'</'+tag+'>')
				else:
					nof_list.append('\t<'+tag+' key="'+key+'">'+translated.text+'</'+tag+'>')
				licz+= 1
				#if licz >= 15: break
		except:
			nof_list.append('\t<'+tag+' key="'+key+'">'+translated.text+'</'+tag+'>')
	 
	nof_list.append('')
	nof_list.append('</message_catalog>')
	#print(nof_list)
	
	fout = open(file_name_output, "w")
	fout.write('\n'.join(nof_list))
	fout.write('\n\n')
	fout.write('\n'.join(html_list))
	fout.close()
	
	print('==================== FINISH Translate ==>',file_name_output,'==================================')

	return file_name_output
 
def string_to_translate(gear,text,lang_from='pl',lang_to='uk'):
	#gears_list = [ ('mymemory',('MyMemory Translator','free')),
	gears_list = ltr_gears_list.gears_list
	text_list = text.split('\n')
	
	#print(gear, text_list, lang_to, lang_from)
	translated = t_start(gear, text_list, lang_from, lang_to)
	#translated = translator.translate(text, dest=lang_to, src=lang_from)
	return translated #[translated.text, translated.extra_data, translated.pronunciation]

def gear_support_lang(t_gear='', lang_from='', lang_to=''):
	if not t_gear:
		gears_list = ltr_gears_list.gears_list
		return gears_list
	
	ts_gear = dict(dict(ltr_gears_list.gears2_dict).items()).get(t_gear)
	if t_gear == 'MyMemoryTranslator':
		supp_lang_list = ltr_gears_lang_list.gfulllist[ts_gear]
  	#{'afrikaans': 'af','albanian': 'sq','amharic': 'am','arabic': 'ar','armenian': 'hy','azerbaijani': 'az','basque': 'eu','belarusian': 'be','bengali': 'bn','bosnian': 'bs','bulgarian': 'bg','catalan': 'ca','cebuano': 'ceb','chichewa': 'ny','chinese (simplified)': 'zh-CN','chinese (traditional)': 'zh-TW','corsican': 'co','croatian': 'hr','czech': 'cs','danish': 'da','dutch': 'nl','english': 'en','esperanto': 'eo','estonian': 'et','filipino': 'tl','finnish': 'fi','french': 'fr','frisian': 'fy','galician': 'gl','georgian': 'ka','german': 'de','greek': 'el','gujarati': 'gu','haitian creole': 'ht','hausa': 'ha','hawaiian': 'haw','hebrew': 'iw','hindi': 'hi','hmong': 'hmn','hungarian': 'hu','icelandic': 'is','igbo': 'ig','indonesian': 'id','irish': 'ga','italian': 'it','japanese': 'ja','javanese': 'jw','kannada': 'kn','kazakh': 'kk','khmer': 'km','kinyarwanda': 'rw','korean': 'ko','kurdish': 'ku','kyrgyz': 'ky','lao': 'lo','latin': 'la','latvian': 'lv','lithuanian': 'lt','luxembourgish': 'lb','macedonian': 'mk','malagasy': 'mg','malay': 'ms','malayalam': 'ml','maltese': 'mt','maori': 'mi','marathi': 'mr','mongolian': 'mn','myanmar': 'my','nepali': 'ne','norwegian': 'no','odia': 'or','pashto': 'ps','persian': 'fa','polish': 'pl','portuguese': 'pt','punjabi': 'pa','romanian': 'ro','russian': 'ru','samoan': 'sm','scots gaelic': 'gd','serbian': 'sr','sesotho': 'st','shona': 'sn','sindhi': 'sd','sinhala': 'si','slovak': 'sk','slovenian': 'sl','somali': 'so','spanish': 'es','sundanese': 'su','swahili': 'sw','swedish': 'sv','tajik': 'tg','tamil': 'ta','tatar': 'tt','telugu': 'te','thai': 'th','turkish': 'tr','turkmen': 'tk','ukrainian': 'uk','urdu': 'ur','uyghur': 'ug','uzbek': 'uz','vietnamese': 'vi','welsh': 'cy','xhosa': 'xh','yiddish': 'yi','yoruba': 'yo','zulu': 'zu'}
		if lang_from not in supp_lang_list.values():
			lang_from = ''
		if lang_to not in supp_lang_list.values():
			lang_to = ''
	elif t_gear == 'GoogleTranslator':
		supp_lang_list = ltr_gears_lang_list.gfulllist[ts_gear]
  	#{'afrikaans': 'af','albanian': 'sq','amharic': 'am','arabic': 'ar','armenian': 'hy','azerbaijani': 'az','basque': 'eu','belarusian': 'be','bengali': 'bn','bosnian': 'bs','bulgarian': 'bg','catalan': 'ca','cebuano': 'ceb','chichewa': 'ny','chinese (simplified)': 'zh-CN','chinese (traditional)': 'zh-TW','corsican': 'co','croatian': 'hr','czech': 'cs','danish': 'da','dutch': 'nl','english': 'en','esperanto': 'eo','estonian': 'et','filipino': 'tl','finnish': 'fi','french': 'fr','frisian': 'fy','galician': 'gl','georgian': 'ka','german': 'de','greek': 'el','gujarati': 'gu','haitian creole': 'ht','hausa': 'ha','hawaiian': 'haw','hebrew': 'iw','hindi': 'hi','hmong': 'hmn','hungarian': 'hu','icelandic': 'is','igbo': 'ig','indonesian': 'id','irish': 'ga','italian': 'it','japanese': 'ja','javanese': 'jw','kannada': 'kn','kazakh': 'kk','khmer': 'km','kinyarwanda': 'rw','korean': 'ko','kurdish': 'ku','kyrgyz': 'ky','lao': 'lo','latin': 'la','latvian': 'lv','lithuanian': 'lt','luxembourgish': 'lb','macedonian': 'mk','malagasy': 'mg','malay': 'ms','malayalam': 'ml','maltese': 'mt','maori': 'mi','marathi': 'mr','mongolian': 'mn','myanmar': 'my','nepali': 'ne','norwegian': 'no','odia': 'or','pashto': 'ps','persian': 'fa','polish': 'pl','portuguese': 'pt','punjabi': 'pa','romanian': 'ro','russian': 'ru','samoan': 'sm','scots gaelic': 'gd','serbian': 'sr','sesotho': 'st','shona': 'sn','sindhi': 'sd','sinhala': 'si','slovak': 'sk','slovenian': 'sl','somali': 'so','spanish': 'es','sundanese': 'su','swahili': 'sw','swedish': 'sv','tajik': 'tg','tamil': 'ta','tatar': 'tt','telugu': 'te','thai': 'th','turkish': 'tr','turkmen': 'tk','ukrainian': 'uk','urdu': 'ur','uyghur': 'ug','uzbek': 'uz','vietnamese': 'vi','welsh': 'cy','xhosa': 'xh','yiddish': 'yi','yoruba': 'yo','zulu': 'zu'}
		if lang_from not in supp_lang_list.values():
			lang_from = ''
		if lang_to not in supp_lang_list.values():
			lang_to = ''
	elif t_gear == 'YandexTranslator':
		supp_lang_list = ltr_gears_lang_list.gfulllist[ts_gear]
  	#{'Afrikaans': 'af', 'Albanian': 'sq', 'Amharic': 'am', 'Arabic': 'ar', 'Armenian': 'hy', 'Azerbaijani': 'az', 'Bashkir': 'ba', 'Basque': 'eu', 'Belarusian': 'be', 'Bengali': 'bn', 'Bosnian': 'bs', 'Bulgarian': 'bg', 'Burmese': 'my', 'Catalan': 'ca', 'Cebuano': 'ceb', 'Chinese': 'zh', 'Chuvash': 'cv', 'Croatian': 'hr', 'Czech': 'cs', 'Danish': 'da', 'Dutch': 'nl', 'Elvish (Sindarin)': 'sjn', 'Emoji': 'emj', 'English': 'en', 'Esperanto': 'eo', 'Estonian': 'et', 'Finnish': 'fi', 'French': 'fr', 'Galician': 'gl', 'Georgian': 'ka', 'German': 'de', 'Greek': 'el', 'Gujarati': 'gu', 'Haitian': 'ht', 'Hebrew': 'he', 'Hill Mari': 'mrj', 'Hindi': 'hi', 'Hungarian': 'hu', 'Icelandic': 'is', 'Indonesian': 'id', 'Irish': 'ga', 'Italian': 'it', 'Japanese': 'ja', 'Javanese': 'jv', 'Kannada': 'kn', 'Kazakh': 'kk', 'Kazakh (Latin)': 'kazlat', 'Khmer': 'km', 'Korean': 'ko', 'Kyrgyz': 'ky', 'Lao': 'lo', 'Latin': 'la', 'Latvian': 'lv', 'Lithuanian': 'lt', 'Luxembourgish': 'lb', 'Macedonian': 'mk', 'Malagasy': 'mg', 'Malay': 'ms', 'Malayalam': 'ml', 'Maltese': 'mt', 'Maori': 'mi', 'Marathi': 'mr', 'Mari': 'mhr', 'Mongolian': 'mn', 'Nepali': 'ne', 'Norwegian': 'no', 'Papiamento': 'pap', 'Persian': 'fa', 'Polish': 'pl', 'Portuguese': 'pt', 'Punjabi': 'pa', 'Romanian': 'ro', 'Russian': 'ru', 'Scottish Gaelic': 'gd', 'Serbian': 'sr', 'Sinhalese': 'si', 'Slovak': 'sk', 'Slovenian': 'sl', 'Spanish': 'es', 'Sundanese': 'su', 'Swahili': 'sw', 'Swedish': 'sv', 'Tagalog': 'tl', 'Tajik': 'tg', 'Tamil': 'ta', 'Tatar': 'tt', 'Telugu': 'te', 'Thai': 'th', 'Turkish': 'tr', 'Udmurt': 'udm', 'Ukrainian': 'uk', 'Urdu': 'ur', 'Uzbek': 'uz', 'Uzbek (Cyrillic)': 'uzbcyr', 'Vietnamese': 'vi', 'Welsh': 'cy', 'Xhosa': 'xh', 'Yakut': 'sah', 'Yiddish': 'yi', 'Zulu': 'zu'}
		if lang_from not in supp_lang_list.values():
			lang_from = ''
		if lang_to not in supp_lang_list.values():
			lang_to = ''
	elif t_gear == 'MicrosoftTranslator':
		supp_lang_list = ltr_gears_lang_list.gfulllist[ts_gear]
  	#{'afrikaans': 'af','amharic': 'am','arabic': 'ar','assamese': 'as','azerbaijani': 'az','bashkir': 'ba','bulgarian': 'bg','bangla': 'bn','tibetan': 'bo','bosnian': 'bs','catalan': 'ca','czech': 'cs','welsh': 'cy','danish': 'da','german': 'de','divehi': 'dv','greek': 'el','english': 'en','spanish': 'es','estonian': 'et','basque': 'eu','persian': 'fa','finnish': 'fi','filipino': 'fil','fijian': 'fj','faroese': 'fo','french': 'fr','french (canada)': 'fr-ca','irish': 'ga','galician': 'gl','gujarati': 'gu','hebrew': 'he','hindi': 'hi','croatian': 'hr','upper sorbian': 'hsb','haitian creole': 'ht','hungarian': 'hu','armenian': 'hy','indonesian': 'id','inuinnaqtun': 'ikt','icelandic': 'is','italian': 'it','inuktitut': 'iu','inuktitut (latin)': 'iu-latn','japanese': 'ja','georgian': 'ka','kazakh': 'kk','khmer': 'km','kurdish (northern)': 'kmr','kannada': 'kn','korean': 'ko','kurdish (central)': 'ku','kyrgyz': 'ky','lao': 'lo','lithuanian': 'lt','latvian': 'lv','chinese (literary)': 'lzh','malagasy': 'mg','māori': 'mi','macedonian': 'mk','malayalam': 'ml','mongolian (cyrillic)': 'mn-cyrl','mongolian (traditional)': 'mn-mong','marathi': 'mr','malay': 'ms','maltese': 'mt','hmong daw': 'mww','myanmar (burmese)': 'my','norwegian': 'nb','nepali': 'ne','dutch': 'nl','odia': 'or','querétaro otomi': 'otq','punjabi': 'pa','polish': 'pl','dari': 'prs','pashto': 'ps','portuguese (brazil)': 'pt','portuguese (portugal)': 'pt-pt','romanian': 'ro','russian': 'ru','slovak': 'sk','slovenian': 'sl','samoan': 'sm','somali': 'so','albanian': 'sq','serbian (cyrillic)': 'sr-cyrl','serbian (latin)': 'sr-latn','swedish': 'sv','swahili': 'sw','tamil': 'ta','telugu': 'te','thai': 'th','tigrinya': 'ti','turkmen': 'tk','klingon (latin)': 'tlh-latn','klingon (piqad)': 'tlh-piqd','tongan': 'to','turkish': 'tr','tatar': 'tt','tahitian': 'ty','uyghur': 'ug','ukrainian': 'uk','urdu': 'ur','uzbek (latin)': 'uz','vietnamese': 'vi','yucatec maya': 'yua','cantonese (traditional)': 'yue','chinese simplified': 'zh-hans','chinese traditional': 'zh-hant','zulu': 'zu'}
		if lang_from not in supp_lang_list.values():
			lang_from = ''
		if lang_to not in supp_lang_list.values():
			lang_to = ''
	elif t_gear == 'LibreTranslator':
		supp_lang_list = ltr_gears_lang_list.gfulllist[ts_gear]
  	#{'English': 'en', 'Arabic': 'ar', 'Azerbaijani': 'az', 'Chinese': 'zh', 'Czech': 'cs', 'Dutch': 'nl', 'Finnish': 'fi', 'French': 'fr', 'German': 'de', 'Hindi': 'hi', 'Hungarian': 'hu', 'Indonesian': 'id', 'Irish': 'ga', 'Italian': 'it', 'Japanese': 'ja', 'Korean': 'ko', 'Polish': 'pl', 'Portuguese': 'pt', 'Russian': 'ru', 'Spanish': 'es', 'Swedish': 'sv', 'Turkish': 'tr', 'Ukranian': 'uk', 'Vietnamese': 'vi'}
		if lang_from not in supp_lang_list.values():
			lang_from = ''
		if lang_to not in supp_lang_list.values():
			lang_to = ''
	elif t_gear == 'DeeplTranslator':
		supp_lang_list = ltr_gears_lang_list.gfulllist[ts_gear]
  	#{'bulgarian': 'bg','czech': 'cs','danish': 'da','german': 'de','greek': 'el','english': 'en','spanish': 'es','estonian': 'et','finnish': 'fi','french': 'fr','hungarian': 'hu','italian': 'it','japanese': 'ja','lithuanian': 'lt','latvian': 'lv','dutch': 'nl','polish': 'pl','portuguese': 'pt','romanian': 'ro','russian': 'ru','slovak': 'sk','slovenian': 'sl','swedish': 'sv','chinese': 'zh'}
		if lang_from not in supp_lang_list.values():
			lang_from = ''
		if lang_to not in supp_lang_list.values():
			lang_to = ''
	elif t_gear == 'PonsTranslator':
		supp_lang_list = ltr_gears_lang_list.gfulllist[ts_gear]
  	#{'English': 'en', 'French': 'fr', 'German': 'de', 'Greek': 'el', 'Italian': 'it', 'Polish': 'pl', 'Portuguese': 'pt', 'Russian': 'ru', 'Slovenian': 'sl', 'Spanish': 'es', 'Turkish': 'tr'}
		if lang_from not in supp_lang_list.values():
			lang_from = ''
		if lang_to not in supp_lang_list.values():
			lang_to = ''

	if lang_from and lang_to:
		return lang_from,lang_to
	else:
		if not lang_from and not lang_to:
			return 'Invalid','Invalid'
		elif not lang_from:
			return 'Invalid',lang_to
		elif not lang_to:
			return lang_from,'Invalid'

# lss = {'en': 'English','fr': 'French','de': 'German','el': 'Greek','it': 'Italian','pl': 'Polish','pt': 'Portuguese','ru': 'Russian','sl': 'Slovenian','es': 'Spanish','tr': 'Turkish', }
# nlss = [[v,k] for k,v in lss.items()]
#   #nlss.append([v,k])
#   #nlss.append(k)
# print(dict(nlss))

# raise SystemExit()

def t_start(t_gear='', t_list='', lang_from='pl',lang_to='uk'):

	finish_tl = []
	if t_gear == 'CompareTranslators':
		t_gears_list = ltr_gears_list.gears2_dict.keys() #['MyMemoryTranslator','GoogleTranslator']
	else:
		t_gears_list = [t_gear]

	if len(t_gears_list) > 1:
		finish_tl.append(['TextToTranslate',t_list])
	for t_gear in t_gears_list:
		finish_tl.append(['TranslateGear',t_gear])
		#lang_from,lang_to = 'qw','wq'
		lang_from,lang_to = gear_support_lang(t_gear, lang_from, lang_to)
		if 'Invalid' in (lang_from,lang_to):
			if lang_from == 'Invalid':
				return_str = t_gear+' - Invalid source language!'
			elif lang_to == 'Invalid':
				return_str = t_gear+' - Invalid target language!'
			#return ['Err', return_str]
			finish_tl.append(['Price','Free'])
			finish_tl.append(['Err',return_str])
		else:
			try:
				if len(t_gears_list) == 1:
					finish_tl.append(['TextToTranslate',t_list])
					# print('---------------------------')
					# print(finish_tl)
					# print('---------------------------')
				if t_gear == 'DeeplTranslator_test':
					translated = DeeplTranslator(get_key(t_gear)).translate_batch(t_list)
					finish_tl.append(['Price','<div class="table-head col1">DeepL API Free<br />For max. 500,000 characters/month</div><div class="table-head col2">DeepL API Pro €4.99 per month<br />+ Usage-based pricing</div><div class="clear-both"></div><div class="col1">&nbsp;</div><div class="col2">€20.00 per 1 million characters</div><div class="clear-both"></div>'])
					finish_tl.append(['OK',translated])
				elif t_gear == 'PonsTranslator':
					finish_tl.append(['Price','Free'])
					translated = PonsTranslator(source=lang_from, target=lang_to).translate_words(t_list)
					finish_tl.append(['OK',translated])
				else:
					for text in t_list:
						try:
							if t_gear == 'MyMemoryTranslator':
								finish_tl.append(['Price','Free'])
								translated = MyMemoryTranslator(source=lang_from, target=lang_to).translate(text)
							elif t_gear == 'GoogleTranslator':
								finish_tl.append(['Price','Free'])
								translated = GoogleTranslator(source=lang_from, target=lang_to).translate(text=text)
							elif t_gear == 'YandexTranslator':
								finish_tl.append(['Price','<div class="table-head col1">Number of characters in the requests for the Reporting period</div><div class="table-head col2">Rate (in US dollars per 1 million characters)</div><div class="clear-both"></div><div class="col1">less 50 000 000</div><div class="col2">15</div><div class="clear-both"></div><div class="col1">from 50 000 001 to 100 000 000</div><div class="col2">12</div><div class="clear-both"></div><div class="col1">from 100 000 001 to 200 000 000</div><div class="col2">10</div><div class="clear-both"></div><div class="col1">from 200 000 001 to 500 000 000</div><div class="col2">8</div><div class="clear-both"></div><div class="col1">from 500 000 001 to 1 000 000 000</div><div class="col2">6</div><div class="clear-both"></div>'])
								translated = YandexTranslator(get_key(t_gear)).translate(source=lang_from, target=lang_to, text=text)
								print('$'*30,translated)
							elif t_gear == 'MicrosoftTranslator':
								finish_tl.append(['Price','<div class="table-head">2M chars of any combination of standard translation and custom training free per month\n then $10 per 1M chars of standard translation</div><div class="clear-both"></div>'])
								translated = MicrosoftTranslator(api_key=get_key(t_gear), region='westeurope', source=lang_from, target=lang_to).translate(text=text)
							elif t_gear == 'LibreTranslator':
								finish_tl.append(['Price','Free'])
								translated = LibreTranslator(source=lang_from, target=lang_to, base_url='https://libretranslate.com/', api_key=get_key(t_gear)).translate(text=text)
							elif t_gear == 'DeeplTranslator':
								finish_tl.append(['Price','<div class="table-head col1">DeepL API Free<br />For max. 500,000 characters/month</div><div class="table-head col2">DeepL API Pro €4.99 per month<br />+ Usage-based pricing</div><div class="clear-both"></div><div class="col1">&nbsp;</div><div class="col2">€20.00 per 1 million characters</div><div class="clear-both"></div>'])
								translated = DeeplTranslator(api_key=get_key(t_gear), source=lang_from, target=lang_to, use_free_api=True).translate(text)

							if translated == 'TooManyRequests':
								finish_tl.append(['Err',translated])	
							else:
								finish_tl.append(['OK',translated])
						except ValueError as e:
							#print('t_start ==> ValueError:',e)
							finish_tl.append(['Err',e])

			except TooManyRequests as e:
				finish_tl.append(['Err','TooManyRequests'])
			except ServerException as e:
				#print('t_start ==> ValueError:',e)
				finish_tl.append(['Err','ServerException'])
			except RequestError as e:
				#print('t_start ==> ValueError:',e)
				finish_tl.append(['Err','RequestError'])
			except:
				finish_tl.append(['Err','Wystąpił błąd'])
			#print(finish_tl)
 
	return finish_tl

def compare_translators(translated_list):

	char_count = 0
	for ll in translated_list[0][1]:
		#print(len(ll),len(ll.replace(' ','')),len(re.sub(r'[^a-zA-Z]', '', ll)))
		char_count+= len(re.sub(r'[^a-zA-Z]', '', ll))

	nlista = []
	err_nlista = []
	for idx,l in enumerate(translated_list):
		if idx == 0:
			nlista.append(l)
		elif translated_list[idx][1] == 'CompareTranslators':
			break
		elif not idx%3:
			if l[idx%3] == 'OK' and translated_list[idx][1] != 'TooManyRequests':
				#print(idx,idx%3,l[idx%3],l, lista[idx-2])
				nlista.append([translated_list[idx-2][0], translated_list[idx-2][1].replace('Translator',' Translator')])
				nlista.append(translated_list[idx-1])
				nlista.append(translated_list[idx])
			else:
    		#print(idx,idx%3,l[idx%3])
				err_nlista.append([translated_list[idx-2][0], translated_list[idx-2][1].replace('Translator',' Translator')])
				err_nlista.append(translated_list[idx-1])
				err_nlista.append(translated_list[idx])

	nlista.extend(err_nlista)

	l = [['Charcount',char_count],translated_list[0][1],nlista]
	#print(l)

	return l
