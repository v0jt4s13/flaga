from flask import Flask, render_template, url_for, redirect
from flask import request
import json
from app_files.py_terminal_app_run import runAppInsideScript
from app_files.moje_biblioteki import mainPageMenuList, get_client_ip
from app_files.przydatne_linki import get_urls_list, get_urls_tags_list, update_urls_in_json_file, check_password, get_urls_tags_count_list
from app_files.password_generator import password_generator
from app_files.random_python_code import showRandomPythonCode
from app_files.pykruter import random_question_from_csv
from app_files.translate import string_to_translate, ltr_form, gear_support_lang, gears_list, compare_translators
from datetime import datetime
from os import path, walk
import random

app=Flask(__name__)
app.secret_key = 'app-py-pr-xd'
# source flagaenv/bin/activate
# deactivate

import logging
import logging.handlers
import time

def log_setup():
	log_file_name = "output.log"
	log_handler = logging.handlers.WatchedFileHandler('output.log')
	formatter = logging.Formatter( 
	    '%(asctime)s program [%(process)d]: %(message)s',
	    '%b %d %H:%M:%S')
	
	formatter.converter = time.gmtime  # if you want UTC time
	log_handler.setFormatter(formatter)
	logger = logging.getLogger()
	logger.addHandler(log_handler)
	logger.setLevel(logging.DEBUG)
#log_setup()

@app.route('/')
def index():

	text = open('domain.txt').read()
	li_list = mainPageMenuList()
	#random_python_code_list = showRandomPythonCode()
	#logging.info('== / - wizyta na stronie glownej')
	#method_list, name_list, syntax_list, parameters_list, use_examples_list = getRandomPythonExampleCode('html')
	return render_template("index.html", text=text, li_list=li_list) #, random_python_code_list=random_python_code_list)


@app.route('/newspage')
def newspage():
	return render_template("newspage.html")

#@app.route('/translated-to-ukrainien')
#def uk_translated():
#	return render_template("index.html")

@app.route('/rpc')
def rpc():
	
	err = ""
	try:
		random_python_code_list = showRandomPythonCode()
		#random_python_code_list = [['Type', 'Metoda'], ['Name', 'Sort'], ['Syntax', 'list.sort(reverse=True|False, key=myFunc)'], ['ParameterValue', [['reverse', 'Optional. reverse=True will sort the list descending. Default is reverse=False'], ['key', 'Optional. A function to specify the sorting criteria(s)']]], ['UseExample', [['Sort the list descending', 'numbers_list = [5, 1, 4]\n\nnumbers_list.sort(reverse=True)']]], ['Return', [['ReturnType', 'list'], ['ReturnValue', '[1, 4, 5]']]]]
		#qq = type(showRandomPythonCode())
	except KeyError as e:
		raise KeyError(e)
		# Exception ValueError BaseException
		#print(e)
		#err = e
		random_python_code_list = ["blad1", type(e), e]
	except:
		random_python_code_list = ["blad2", "jakis"]

	rpc = json.loads(json.dumps(random_python_code_list))
	rpc2 = random_python_code_list
	rpc1 = "json.loads(random_python_code_list) "
	
 
	type = rpc[0]['Type']
	name = rpc[1]['Name']
	syntax = rpc[2]['Syntax']
	parameter = rpc[3]['ParameterValue']
	example = rpc[4]['UseExample']
	output = rpc[5]['Return']
 
	#rpc = random_python_code_list
	test_list = ['Return', ['String1','String2']]
	#random_python_code_list = ["poz1", "poz2"]
	img_url = "https://pythonbasics.org/wp-content/uploads/2019/10/flask_template.png"
	return render_template("rpc/index.html.jinja", err=err, rpc=rpc, rpc1=rpc1, rpc2=rpc2, img_url=img_url, type=type, name=name, syntax=syntax, example=example, output=output, parameter=parameter)

@app.route('/xd')
def xd():
	text = open('domain.txt').read()
	inny_text = "????????, ??l????a, b????d"
	return render_template("xd.html", text='http://'+text.strip(), inny_text=inny_text)
	
@app.route('/doc')
def doc():
	text = open('domain.txt').read()
	return render_template("doc.html", text=text)

@app.route('/kubus_puchatek')
def kubus_puchatek():
	return render_template("kubus_puchatek.html")

@app.route('/flagi')
def flagi():
	return render_template("flagi.html")

@app.route('/flaga-dla-ukrainy')
def flaga_dla_ukrainy():
	return render_template("flaga-dla-ukrainy.html")

@app.route('/pass-generator', methods=['GET','POST'])
def pass_generator():
		
	pass_rendered = ""
	try:
		if request.method == 'GET':
			cc = int(request.args.get('char_count'))
		elif request.method == 'POST':
			cc = int(request.form['char_count'])
			pass_rendered = password_generator(cc)
		else:
			cc = 0
	except ValueError as e:
		cc = "Error "+request.form['char_count']
	except:
		cc = "Still errors occurs"
	
	return render_template("pass-generator/index.html", pass_rendered=pass_rendered)

@app.route('/app-run', methods=['GET','POST'])
def py_terminal_app_run():
		
	try:
		if request.method == 'GET':
			text = request.args.get('term_text')
		elif request.method == 'POST':
			text = request.form['linia1']
			text_list = text.split('\n')
			text_kolejny = runAppInsideScript(text)
		else:
			text = "NO_GET"
	except ValueError as e:
		text = "Noting to declare "+request.form['linia1']
	except:
		text = "Same b????dy w kodzie ... ;/ \n<br>Zaraz wracam i to poprawie ..."

	return render_template("app-run/index.html", text_list=text_list, text_kolejny=text_kolejny)

@app.route('/py-terminal', methods = ['POST','GET'])
def py_terminal():
	return render_template("py-terminal/index.html")

@app.route('/py-terminal2')
def py_terminal2():
	return render_template("py-terminal2/index.html")

@app.route('/py-command')
def py_command():
	return render_template("py-command.html")


@app.route('/cam')
def py_cam():
	return render_template("cam.html")

@app.route('/pykruter')
def pykruter():
	
	question_answer_list = random_question_from_csv()
	question = question_answer_list[0]
	answer_list = question_answer_list[1]
 
	return render_template("pykruter/index.html", question=str(question), answer_list=answer_list)

@app.route('/urls/add', methods = ['POST','GET'])
def urls_add():
	pass_str = ""
	return_resp = ""
	# = ""
	#return redirect(url_for('found', return_resp='return_resp'))
	if request.method == 'POST':
		pass_str = request.form['pass_str']
		url_str = request.form['url_str']
		opis_str = request.form['opis_str']
		tagi_str = request.form['tagi_str']
		#logging.info('urls() ==> url:'+url_str+'; opis:'+opis_str+'; tagi:'+tagi_str)
		if check_password(pass_str,opis_str) == 'OK':
			#logging.info('== urls - inside POST == przed update_urls_in_json_file')
			return_resp+= update_urls_in_json_file(url_str,opis_str,tagi_str)
			#logging.info('== urls - inside POST == update_urls_in_json_file resp:'+return_resp)
			err_nr = 0
		else:
			logging.info('== urls - inside POST == pass:'+pass_str)
			err_nr = 1
			return_resp = "B????dne has??o"

	return '{"err_nr":"'+str(err_nr)+'", "message":"'+return_resp+'"}'

		#return render_template("urls/index.html", add=add, return_resp=return_resp, \
		#items=[], tags_count=0, max_tag_count=0, tags='', date_part=date_part)
		#return redirect(url_for('found', return_resp=return_resp))
	#else:
	#	return_resp+= "POST fail"


@app.route('/urls', methods = ['POST','GET'])
def urls():

		return_resp = ""
		items = get_urls_list('lista')
		tags_list = get_urls_tags_count_list() # 
		max_tag_count = tags_list[0]
		tags = tags_list[1]
		tags_count = len(tags)
		now = datetime.now()
		date_part = now.strftime('%Y%m')+' '+now.strftime('%H')

		return render_template("urls/index.html", return_resp=return_resp, \
		items=items, tags_count=tags_count, max_tag_count=max_tag_count, tags=tags, \
		date_part=date_part)

@app.route('/video')
def video():
	#return 'abc'
	return render_template("index.html")


@app.route('/translator-compare')
def translator_compare():
	trl = test_translate_output()

	return render_template("translator/compare.html", artc=trl[0], art=trl[1], tra=trl[2])

@app.route('/translator', methods=["GET", "POST"])
def translate(text_to_translate='',lang_from='',lang_to=''):
	#print('SSSSSSSSSSSSSSSSSSSSSSS')
	yt = ''
	translated_text = ''
	form = ltr_form()

	if request.method == 'POST':
		#logging.info('request method == POST')
		try:
			lang_from = form.ltr_lang_from.data
			lang_to = form.ltr_lang_to.data
			text_to_translate = form.ltr_textarea.data
			ltr_gears = form.ltr_gears.data
			gear = dict(gears_list())[ltr_gears][0]
			gear = gear.replace(' ', '')
			if gear == 'CompareTranslators':
				#return_translated_list = [['TextToTranslate', ['Wklej tekst do t??umaczenia']], ['TranslateGear', 'MyMemoryTranslator'], ['Price', 'Free'], ['OK', '?????????????? ?????????? ?????? ??????????????????'], ['TranslateGear', 'GoogleTranslator'], ['Price', 'Free'], ['OK', '?????????????? ??????????, ???????? ???????????????? ????????????????????'], ['TranslateGear', 'YandexTranslator'], ['Price', '<div class="table-head col1">Number of characters in the requests for the Reporting period</div><div class="table-head col2">Rate (in US dollars per 1 million characters)</div><div class="clear-both"></div><div class="col1">less 50 000 000</div><div class="col2">15</div><div class="clear-both"></div><div class="col1">from 50 000 001 to 100 000 000</div><div class="col2">12</div><div class="clear-both"></div><div class="col1">from 100 000 001 to 200 000 000</div><div class="col2">10</div><div class="clear-both"></div><div class="col1">from 200 000 001 to 500 000 000</div><div class="col2">8</div><div class="clear-both"></div><div class="col1">from 500 000 001 to 1 000 000 000</div><div class="col2">6</div><div class="clear-both"></div>'], ['Err', 'ServerException(\'ERR_KEY_INVALID\')'], ['TranslateGear', 'MicrosoftTranslator'], ['Price', '<div class="table-head">2M chars of any combination of standard translation and custom training free per month\n then $10 per 1M chars of standard translation</div><div class="clear-both"></div>'], ['OK', '???????????????????? ???????????? ?????? ??????????????????'], ['TranslateGear', 'DeeplTranslator'], ['Err', 'DeeplTranslator - Invalid target language!'], ['TranslateGear', 'PonsTranslator'], ['Err', 'PonsTranslator - Invalid target language!'], ['TranslateGear', 'CompareTranslators'], ['Err', 'CompareTranslators - Invalid target language!']]
				return_translated_list = string_to_translate(gear,text_to_translate,lang_from,lang_to)
			
				#print('\n\n\n\n*******************************************\n\n\n\n')
				#print(return_translated_list)
				#print('\n\n\n\n*******************************************\n\n\n\n')
				new_translated_list = []
				err = 0
				for idx,l in enumerate(return_translated_list):
					if idx == 0:
						new_translated_list.append(l)
					elif l[0] == 'TranslateGear':
						if idx > 1:
							translated_article_str = ' '.join(translated_article_list)
							new_translated_list.append(['OK', translated_article_str])
						new_translated_list.append(l)
						translated_article_list = []
						if err == 1:
							err = 0
							#new_translated_list.append(['Price', '&nbsp;'])
					elif l[0] == 'Price' and return_translated_list[idx-1][0] == 'TranslateGear':
						new_translated_list.append(l)
					elif l[0] == 'OK' and 'Invalid target language' not in l[1]:
						translated_article_list.append(l[1])
						#print(translated_article_list)
					elif l[0] == 'Err' or 'Invalid target language' in l[1] or 'TooManyRequests' in l[1]:
						translated_article_list.append(l[1])
						err = 1
					#print('\n\n+++++++++++++++',idx,'++++++++++++++++++\n',l,'\n+++++++++++++++++++++++++++++++++')
				new_translated_list.append(translated_article_list)
				#print('\n\n\n\n*******************************************\n\n\n\n')

				#print(new_translated_list[0])
				# for idx,li in enumerate(new_translated_list):
				# 	if idx > 0:
				# 		print(idx,new_translated_list[idx])
				

				trl = compare_translators(new_translated_list)

				return render_template("translator/compare.html", trl=trl, artc=trl[0], art=trl[1], tra=trl[2:])
  
			else:
				prev_translated = check_translated(gear,text_to_translate)
				if not prev_translated:
					return_translated_list = string_to_translate(gear,text_to_translate,lang_from,lang_to)
					translated_gear = return_translated_list[0][1]
					if return_translated_list[-1][0] == 'OK':
						translated_text = return_translated_list[-1][1]
					else:
						translated_text = 'Wyst??pi?? b????d podczas t??umaczenia.'
				else:
					translated_text = prev_translated
    
		except ValueError as e:
			#logging.info('POST Error')
			try:
				translated_text = e
			except:
				translated_text = 'B??????'
	
	if not form.ltr_textarea.data:
		form.ltr_textarea.data = ''

	support_gear = gear_support_lang()

	#if not translated_text:
	if form.validate_on_submit():
		
		ltr_textarea = form.ltr_textarea.data
		ltr_lang_from = form.ltr_lang_from.data
		ltr_lang_to = form.ltr_lang_to.data
		yt = form.yt.data
		ltr_gears = form.ltr_gears.data
		#print(ltr_textarea)
		#print(' * '*50)
		output_data = '{}\n{}\n{}\n'.format(translated_gear,ltr_textarea,translated_text)
		#print(output_data)
		save_data(output_data)
		if yt:
			ytl = yt.split('=')
			yt = ytl[-1]
		if not yt:
			ytl = ['xM5LrjHPgnI','rxDxuATpZrA','no660i3aIsc','cXYdqalrrRk','CbMoTLmq3Do','JdfSvYkEArc','6tOuW8m08EU','ti5dboE4Iyo']
			yt = ytl[random.randrange(0,len(ytl)-1)]
	 
		#return redirect( url_for("translate", ltr_textarea=ltr_textarea, ltr_lang_from=ltr_lang_from, ltr_lang_to=ltr_lang_to, yt=yt, ytl=ytl) )
		#logging.info('return render_template ==> 11111')
		return render_template("translator/index.html", met=request.method, form=form, text_translated=translated_text, \
																										ltr_textarea=ltr_textarea, ltr_lang_from=ltr_lang_from, ltr_lang_to=ltr_lang_to, \
																										yt=yt, ltr_gears=ltr_gears)

	return render_template("translator/index.html", form=form, text_translated=translated_text, yt=yt, support_gear=support_gear)


# Errors
@app.errorhandler(404)
def handle_404(e):
		return render_template('404.html'), 404
@app.errorhandler(500)
def handle_500(e):
		return render_template('500.html'), 500

if __name__=="__main__":

	app.run(debug=True)

	#urls()
	#app.run()
