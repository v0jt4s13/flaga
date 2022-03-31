from flask import Flask, render_template, url_for
from flask import request
import json
from app_files.py_terminal_app_run import runAppInsideScript
from app_files.moje_biblioteki import mainPageMenuList
from app_files.password_generator import password_generator
from app_files.random_python_code import showRandomPythonCode
from app_files.py_kruter import random_question_from_csv

app=Flask(__name__)
# source flagaenv/bin/activate
# deactivate

@app.route('/')
def index():

	text = open('domain.txt').read()
	li_list = mainPageMenuList()
	#random_python_code_list = showRandomPythonCode()
	
	#method_list, name_list, syntax_list, parameters_list, use_examples_list = getRandomPythonExampleCode('html')
	return render_template("index.html", text=text, li_list=li_list) #, random_python_code_list=random_python_code_list)


@app.route('/newspage')
def newspage():
	return render_template("newspage.html")


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
	inny_text = "żółć, ślęża, błąd"
	return render_template("xda.html", text='http://'+text.strip(), inny_text=inny_text)
  
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
		text = "Same błędy w kodzie ... ;/ \n<br>Zaraz wracam i to poprawie ..."

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
	
	question, answer = random_question_from_csv()
 
	return render_template("pykruter/index.html", question=question, answer=answer)

if __name__=="__main__":
	app.run()
