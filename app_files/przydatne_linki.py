import json
import os
from app_files.secret import get_pass


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


def get_urls_list(out_type):
	#print('get_urls_list:',out_type)
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
		#print('urls_list',type(urls_list),urls_list)
		return urls_list


def check_password(pass_str,pstr):
	if pass_str != "":
		pass_gen = get_pass('urls',pstr)
		if pass_gen == pass_str:
			return "OK"
		else:
			return "Podane hasło jest błędne"
	else:
		return "Nie podano hasła"


def update_urls_in_json_file(url_str,opis_str,tags_str):

	urls_json = get_urls_list('json')
	return_resp = ''

	try:
		file_name = 'static/json/urls.json'
		comma_count = tags_str.count(',')
		space_count = tags_str.count(' ')
		words_count = len(tags_str.split(' '))
		#return_resp = str(comma_count)+'== 0 and '+str(space_count+1)+'== '+str(words_count)+' ==> '
		if comma_count == 0 and space_count+1 == words_count:
			return_resp+= '111 '
			tags_list = tags_str.split(' ')
		else:
			return_resp+= '222 '
			tags_list = tags_str.split(',')
		return_resp+= '333 '
		urls_json.append({'url':url_str, 'opis':opis_str, 'tagi':tags_list})
		return_resp+= '444 '
		new_list = []
		for item in urls_json:
			#return_resp+= '555='+str(item)+' \n\n'
			if item not in new_list:
				return_resp+= '\n\n555aaa=Add new record \n'+str(item)+'\n\n'+str(new_list)
				new_list.append(item)
		
		#return_resp+= '\n\n666='+str(type(item))+' file_name=>',str(type(file_name)),'   new_list==>',str(type(new_list)),' \n\n'
		if saveJsonStringToFile(file_name,new_list):
			return_resp = "Url został zapisany"

		return return_resp
	except ValueError as e:
		#return return_resp+" Błąd danych "+e
		return "Wystąpił błąd podczas zapisu danych"


def get_urls_tags_list(output_type):
	urls_json = get_urls_list('json')
	tags_list = []
	tags_dict = dict()
	licz = 0
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
	
	#print(tags_dict)
	if output_type == 'list':
		return tags_list
	elif output_type == 'dict':
		return tags_dict


def get_urls_tags_list_depricated():
	urls_json = get_urls_list('json')
	tags_list = []
	for item in urls_json:
		#print(type(item.get('tagi')),item.get('tagi'))
		for tag in item.get('tagi'):
			if tag not in tags_list:
				tags_list.append(tag)

	return tags_list

