import xml.etree.ElementTree as ET
from bs4 import BeautifulSoup
from googletrans import Translator
# pip install googletrans==4.0.0rc1
from bs4 import BeautifulSoup
from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, BooleanField, SubmitField, TextAreaField, PasswordField
from wtforms.validators import InputRequired, URL

translator = Translator()

# Forms class
class ltr_form(FlaskForm):
	lang_list = [
		('pl','Polski'),
		('uk','Український'),
		('en','English')
	]
	text = 'Wklej text do przetłumaczenia.'
	ltr_textarea = TextAreaField(text, validators=[InputRequired()])
	ltr_lang_from = SelectField('Tłumacz z języka:', choices=lang_list)
	rev_lang_list = sorted(dict(lang_list).items(), key=lambda x: x[1],reverse=True)
	ltr_lang_to = SelectField('Tłumacz na język:', choices=rev_lang_list) 
	yt = StringField('You Tube:')
 
	button = SubmitField('Tłumacz')

 
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
 
def string_text(text,lang_from='pl',lang_to='uk'):
	#from_lang = 'pl|en'
	#print(text, lang_to, lang_from)
	translated = translator.translate(text, dest=lang_to, src=lang_from)
	#print(f"The Actual Text was {text}")
	#print(f"The Translated Text is: {translated.text}")
	#print(f"The Translated Text pronunciation is {translated.pronunciation}")
	#print('\n\n******************************************\n\n')
	return translated.text

def test():
	# opening the file in read mode
	#file_name_input = 'acs-subsite.en_US.ISO-8859-1.xml'
	#file_name_output = 'repl-acs-subsite.en_US.ISO-8859-1.xml'
	#file = open("acs-lang.ukr_UA.utf-8.xml", "r")
	#src_lang='en'
	
	file_name_input = 'acs-lang.pl_PL.utf-8.xml'
	file_name_output = 'repl-acs-lang.ukr_UA.utf-8.xml'
	src_lang='pl'

	file_name_input = 'acs-kernel.en_US.ISO-8859-1.xml' #'acs-lang.en_GB.ISO-8859-1.xml'
	file_name_output = 'repl-acs-kernel.ukr_UA.utf-8.xml'
	src_lang='en'
	
	file = open(file_name_input, "r")
	replacement = ""
	# using the for loop
	translated_list = []
	untranslated_list = []
	for lidx,line in enumerate(file):
		soup = BeautifulSoup(line, 'html.parser')
		#print(ssoup.getText())
		#if lidx > 10: break
		lista1 = line.split('\"')
		#print(line)
		if lidx >= 3 and len(lista1) >= 2:
			key = lista1[1]
			value = ' '.join(lista1[2:])
			val = value.lstrip('>').replace('</msg>','')
			#print(lidx,key,'===>',val)
			
			try:
			#if 1 == 1:  
				text = soup.getText() #val.replace('\n','')
				print('===>',text)
				#text = 'Access to the page is no longer available or the website has been moved.'
				translated = translator.translate(text, dest='uk', src=src_lang)
				text_translated = translated.text
				text_translated = text_translated.replace('\n','')
				translated_list.append('<msg key="'+key+'">'+text_translated+'</msg>')
			except:
			#else:
				translated_list.append('<msg key="'+key+'">'+val+'</msg>')
				print(key,'===>',val)
				
		
		#print(przed+'">'+str_replaced+'</msg>')
		#changes = line.replace("hardships", "situations")
		#replacement = replacement + changes + "\n"

	file.close()
	# opening the file in write mode
	fout = open(file_name_output, "w")
	fout.write('\n'.join(translated_list))
	fout.close()
 
	pass
	# jdpersonals.Ads_list	Ads list	Not translated
	# jdpersonals.Button_desc_page_1	Proceed in order to add image<br />and preview your ad	Not translated
	# jdpersonals.Button_desc_page_2a	Back to Edit your ad	Not translated
	# jdpersonals.Button_desc_page_2b	Your ad summary	Not translated
	# jdpersonals.Button_desc_page_2c	Save and proceed to Ads list	Not translated
	# jdpersonals.Button_desc_page_3a	Back to the previous page	Not translated
	# jdpersonals.Chart_Header	Monthly and daily statistics: impressions and clicks	Not translated
	# jdpersonals.Chart_No_stats	Statistics for the selected period not found	Not translated
	# jdpersonals.Edit_ad	Edit	Not translated
	# jdpersonals.List_of_ads	List of ads	Not translated
	# jdpersonals.My_ads	My ads	Not translated
	# jdpersonals.online_ads	online ads	Not translated
	# jdpersonals.Our_offer	Our offer	Not translated
	# jdpersonals.Personals	Personals	Not translated
	# jdpersonals.Post_new_ad	Post new ad	Not translated
	# jdpersonals.Preview_of_ad	Preview of ad	Not translated
	# jdpersonals.Progress_bar	Form|Image ad and ad review|Ad verify|Payment online|Confirmation	Not translated
	# jdpersonals.Progress_bar_2	Ad verify|Payment online|Confirmation	Not translated
	# jdpersonals.Start_page	Start page	Not translated
 
#print('string_text:',string_text('Testowy text do tłumaczenia'))