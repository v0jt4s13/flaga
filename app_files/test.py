import json, os
from moje_biblioteki import mainPageMenuList, get_urls_list, check_password, update_urls_in_json_file, get_urls_tags_list

def get_urls_list(out_type):
	print('get_urls_list:',out_type)
	file_name = 'urls.json'
	urls_list = ""
	json_data = ""
	if os.path.exists('static/json/'+file_name):
		with open('static/json/'+file_name, 'r') as file:
			#json_data = json.load(file)
			file_data = file.read()
			json_data = json.loads(file_data)
	else:
		print('File not exist')

	if out_type == 'json':
		return json_data
		#return json_data
	else:
		urls_list = [val for val in json_data]
		print('urls_list',type(urls_list),urls_list)
		return urls_list


def update_urls_in_json_file(url_str,opis_str):

	urls_json = get_urls_list('json')
	new_list = []
	for item in urls_json:
		if item not in new_list:
			new_list.append(item)

	print(new_list)


	#print(type(urls_json),set(dict(urls_json)))

	urls_json.append({'url':url_str, 'opis':opis_str})
	#print(type(urls_json),urls_json)

	try:
	
		return '1. ' #+json.dumps(urls_json, indent=4) #+' len:'+str(len(urls_json))
	except:
		try:
			return '2. ==> '+json.dumps(urls_json[2], indent=4) #urls_json[2] #+' '+urls_json[1]+' \n urls_json:'+json.dumps(urls_json[2])
		except:
			try:
				urls_json.append({'url':url_str, 'opis':opis_str})
				file_name = 'static/json/urls.json'
				
				#urls_json = list(set(urls_json))

				#return_resp = saveJsonStringToFile(file_name,urls_json)
				return '3. last:'+str(urls_json[-1])
			except:
				return '4. urls_json:'+str(urls_json)

def get_urls_tags_count_list():
	urls_json = get_urls_list('json')
	tags_count_dict = dict()
	odd_even = 'odd'
	max_num = 1
	licz = 0
	for item in urls_json:
		for t in item.get('tagi'):
			if t in tags_count_dict.keys():
				c = tags_count_dict.get(t)['count']+1
				tags_count_dict[t]['count'] = c #{'nr':licz,'odd_even':odd_even,'count':c}
				if c > max_num: max_num = c
			else:
				if odd_even == 'odd': odd_even = 'even'
				else: odd_even = 'odd'
				licz+= 1
				tags_count_dict.update({t:{'nr':licz,'odd_even':odd_even,'count':1}})

	return [max_num, tags_count_dict]

def qq():
	for item in urls_json:
		#print(type(item.get('tagi')),item.get('tagi'))
		for tag in item.get('tagi'):
			if tag not in tags_list:
				licz+= 1
				if licz % 2:
					tags_dict.update({tag:{'nr':licz,'odd_even':'odd'}})
				else:
					tags_dict.update({tag:{'nr':licz,'odd_even':'even'}})
					
				tags_list.append(tag)
	if output_type == 'list':
		return tags_list
	elif output_type == 'dict':
		return tags_dict

#print(update_urls_in_json_file('url','opis'))
o_dict = get_urls_tags_count_list()
print(o_dict)
print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
print(get_urls_tags_list('dict'))


# tags_str = "Flask,Jinja,Templates,Python"
# comma_count = tags_str.count(',')
# space_count = tags_str.count(' ')
# words_count = len(tags_str.split(' '))
# if comma_count == 0 and space_count+1 == words_count:
# 	tags_list = tags_str.split(' ')
# else:
# 	tags_list = tags_str.split(',')

# print(tags_str.count(','),tags_str.count(' '),len(tags_str.split(' ')),tags_list)

# [{'url': 'https://learngitbranching.js.org/?locale=pl', 'opis': 'Naucz się branchingu', 'tagi': ['GIT']}, {'url': 'https://favtutor.com/blogs/string-to-dict-python', 'opis': 'String to dictionary', 'tagi': ['Python', 'String', 'Dictionary']}, {'url': 'https://docs.rackspace.com/support/how-to/block-an-ip-address-on-a-Linux-server/', 'opis': 'Block an IP address on a Linux server', 'tagi': ['Server', 'Linux', 'Security']}, {'url': 'https://www.educba.com/linux-jq/', 'opis': 'Linux jq - json', 'tagi': ['Linux', 'json']}, {'url': 'https://londynek.https://www.tutorialguruji.com/python/flask-jinja2-parse-json/', 'opis': 'Flask ninja', 'tagi': ['Python', 'Flask', 'ninja', 'json']}, {'url': 'https://colab.research.google.com/drive/1yrS6E2oafvGeO5AITlrar_amJL3WoQHd#scrollTo=FGCW4tJQn7-P', 'opis': 'Codelabs testy pythona', 'tagi': ['Codelabs', 'cooperate', 'Python']}, {'url': 'https://webrtc.github.io/samples/src/content/getusermedia/getdisplaymedia/', 'opis': 'Screen sharing WebRTC getDisplayMedia', 'tagi': ['WebRTC', 'Screen', 'Sharing', 'javaScript', 'DisplayMedia']}, {'url': 'https://docs.python.org/3/library/tkinter.html', 'opis': 'Python Tkinker - interface to the Tcl/Tk GUI toolkit', 'tagi': ['Python', 'Screen', 'library', 'GUI']}, {'url': 'https://www.programcreek.com/python/index/module/list', 'opis': 'Top pythons API', 'tagi': ['Python', 'API']}]
# [{'url': 'https://learngitbranching.js.org/?locale=pl', 'opis': 'Naucz się branchingu', 'tagi': ['GIT']}, {'url': 'https://favtutor.com/blogs/string-to-dict-python', 'opis': 'String to dictionary', 'tagi': ['Python', 'String', 'Dictionary']}, {'url': 'https://docs.rackspace.com/support/how-to/block-an-ip-address-on-a-Linux-server/', 'opis': 'Block an IP address on a Linux server', 'tagi': ['Server', 'Linux', 'Security']}, {'url': 'https://www.educba.com/linux-jq/', 'opis': 'Linux jq - json', 'tagi': ['Linux', 'json']}, {'url': 'https://londynek.https://www.tutorialguruji.com/python/flask-jinja2-parse-json/', 'opis': 'Flask ninja', 'tagi': ['Python', 'Flask', 'ninja', 'json']}, {'url': 'https://colab.research.google.com/drive/1yrS6E2oafvGeO5AITlrar_amJL3WoQHd#scrollTo=FGCW4tJQn7-P', 'opis': 'Codelabs testy pythona', 'tagi': ['Codelabs', 'cooperate', 'Python']}, {'url': 'https://webrtc.github.io/samples/src/content/getusermedia/getdisplaymedia/', 'opis': 'Screen sharing WebRTC getDisplayMedia', 'tagi': ['WebRTC', 'Screen', 'Sharing', 'javaScript', 'DisplayMedia']}, {'url': 'https://docs.python.org/3/library/tkinter.html', 'opis': 'Python Tkinker - interface to the Tcl/Tk GUI toolkit', 'tagi': ['Python', 'Screen', 'library', 'GUI']}, {'url': 'https://www.programcreek.com/python/index/module/list', 'opis': 'Top pythons API', 'tagi': ['Python', 'API']}]
# [{'url': 'https://learngitbranching.js.org/?locale=pl', 'opis': 'Naucz się branchingu', 'tagi': ['GIT']}, {'url': 'https://favtutor.com/blogs/string-to-dict-python', 'opis': 'String to dictionary', 'tagi': ['Python', 'String', 'Dictionary']}, {'url': 'https://docs.rackspace.com/support/how-to/block-an-ip-address-on-a-Linux-server/', 'opis': 'Block an IP address on a Linux server', 'tagi': ['Server', 'Linux', 'Security']}, {'url': 'https://www.educba.com/linux-jq/', 'opis': 'Linux jq - json', 'tagi': ['Linux', 'json']}, {'url': 'https://londynek.https://www.tutorialguruji.com/python/flask-jinja2-parse-json/', 'opis': 'Flask ninja', 'tagi': ['Python', 'Flask', 'ninja', 'json']}, {'url': 'https://colab.research.google.com/drive/1yrS6E2oafvGeO5AITlrar_amJL3WoQHd#scrollTo=FGCW4tJQn7-P', 'opis': 'Codelabs testy pythona', 'tagi': ['Codelabs', 'cooperate', 'Python']}, {'url': 'https://webrtc.github.io/samples/src/content/getusermedia/getdisplaymedia/', 'opis': 'Screen sharing WebRTC getDisplayMedia', 'tagi': ['WebRTC', 'Screen', 'Sharing', 'javaScript', 'DisplayMedia']}, {'url': 'https://docs.python.org/3/library/tkinter.html', 'opis': 'Python Tkinker - interface to the Tcl/Tk GUI toolkit', 'tagi': ['Python', 'Screen', 'library', 'GUI']}, {'url': 'https://www.programcreek.com/python/index/module/list', 'opis': 'Top pythons API', 'tagi': ['Python', 'API']}]