#from moje_biblioteki import log_setup
import random
import json	

try:
	from moje_biblioteki import convertListToJsonString
except:
	def convertListToJsonString(input_list="",extra_para=""):

		print('*'*30,'convertListToJsonString(',type(input_list),len(input_list),', '+extra_para+')','*'*30)
		
		wrap_json_list = ""
		prep_json_str = ""
		prep_json_list = []
		
		if input_list == "":
			input_list = ["Value1", "Value2", "Value3"]
			append_new_list = []
			for item in input_list:
				more_details_list = ["More details1", "More details2", "More details3"] #extended_list_function(item)
				if extra_para == "test":
					append_new_list.append({'Len':len(more_details_list),'Detail1':more_details_list[0],'DetailLast':more_details_list[-1]})
				else:
					append_new_list.append({'Detail1':more_details_list[0],'Detail2':more_details_list[1],'DetailLast':more_details_list[-1]})
			
			wrap_json_list = {'MainName':append_new_list}

			return wrap_json_list

		else:
			prep_json_str = ""
			json_str_list = []
			output_list = []
			yy = 0

			# class CodeExamples:
			# 	def __init__(self, type, name, syntax, parameters, example, output):
			# 		self.name = name
			# 		self.type = type
			# 		self.syntax = syntax
			# 		self.parameters = parameters
			# 		self.example = example
			# 		self.output = output

   
			# print("New short list:",type(input_list))
			# tmp_list = []
			# for tmp_item in input_list:
			# 	print('\n',len(tmp_item),type(tmp_item),' '.join(tmp_item[0])) #.replace('[[','[{').replace('[','{').replace(']','}'))
			# 	xx = 0
			# 	len_list = len(tmp_item)
			# 	while xx < len_list:
			# 		print(tmp_item[xx])
			# 		xx+= 1

			# #tmp_list.append(tmp_item)
			# print("End new short list")
			# print("***********************************************************")
			# raise SystemExit
			# input_list = tmp_item

			#print(type(input_list),len(input_list),input_list)
			list_len = len(input_list)
			for item in input_list:
				#print(item)
				#if yy > 0: break
				#yy+= 1
				wielkosc_listy = len(item)
				print('\n\n *','* '*20,'Element',str(yy),' ==> ',item[1][1],'==> List count:=',wielkosc_listy,'* '*20)
				print(' *\n *',item[0],item[2],item[-1])
				print(' *',item[-2])
				print(' *\n *','* '*67)
				#print('\t\t\t',item[1][1])

				if wielkosc_listy > 0:
					xx = 0
					
					#prep_json_list.clear()
					#raise SystemExit
					#while xx < wielkosc_listy:
					for item_val in item:

						#if xx > 0: prep_json_str+= ', '
						#print(len(item[xx]),item[xx])
						#if xx in (0,3) or xx == wielkosc_listy-1: print('\n\t\t',xx,'/',yy,'==========',item[xx][1],type(item[xx][1]),'\n')
						#print(len(item[xx]),'==> if type(item['+str(xx)+'][1]) ==',type(item[xx][1]),' ==> wielkosc_listy:',wielkosc_listy)

						#if type(item[xx][1]) == list:
						if isinstance(item_val[1],list):
							#print('pass',len(item[xx][1]),item[xx][1])
							zz = 0
							prep_json_str = ""
							tmp_str_pun_list = []
							while zz < len(item_val[1]):
								key = item_val[1][zz][0]
								val = item_val[1][zz][1]

								prep_json_str = {
									key:val
								}
								tmp_str_pun_list.append(prep_json_str)
								zz+= 1
							#print('A!A!A!A!A ==> ',prep_json_str)
							prep_json_list.append({item_val[0]:tmp_str_pun_list})
       
						else:
							
							key = item_val[0]
							val = item_val[1]
							#print('\t\t\t','===>',key,val)
							prep_json_str = {
								key:val
							}
							prep_json_list.append(prep_json_str)
							#print('B!B!B!B!B! ==> ',prep_json_str)
							#print('22==>',prep_json_str)

						if xx == wielkosc_listy-1:
							print('\n\n *','-_-'*20,len(output_list),' el. w output_list','-_-'*20)
							print(' *\n *',output_list)
							print(' *\n *\n *','* '*16,'Dodajemy elementy do nowej listy => output_list.append()','* '*16)
							print(' *\n *\n *',prep_json_list[1])
							print(' *\n * type na output_list:',type(output_list),' i type na prep_json_list:',type(prep_json_list),' oraz type na list(prep_json_list):',type(list(prep_json_list)))
							output_list.append(list(prep_json_list))
							print(' *\n * lista output_list ==>',output_list)
							print(' *\n *\n *','-_-'*17,len(output_list),' el. po output_list.append()','-_-'*17)
							print(' *\n *\n *',output_list)
							print(' *\n *','* '*67)
							if yy < list_len-1:
								print('\n\n\t\t \t\t-------======== Wracamy na gore  =========---------\n\n')
							else:
								print('\n\n\t\t -------======== Koniec wykonywania skryptu =========---------\n\n')
							del prep_json_list[:]
						xx+= 1
					yy+= 1

			print('*************\n'*5,output_list,'\n*************'*5)
   
		return output_list

def flaga_root_folder():
  return "/var/www/flaga/"

def getRandomPythonExampleCode():
	print('*'*15,'getRandomPythonExampleCode() - wszedl')
	#import logging

	#log_setup()
	#logging.info('== getRandomPythonExampleCode - START3 ==')
	print('*'*15,'try getRandomPythonExampleCode()')
	filename = flaga_root_folder()+'static/json/test_python_code.json'
	fileObject = open(filename,'r')
	#logging.info('== getRandomPythonExampleCode ==> open('+filename+',+r)')
	tmp_data_json = fileObject.read()


	#print('\n\n AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA \n\n')
	#file_data_json = json.loads(tmp_data_json) #.replace("\"", "'")
	#print(type(file_data_json),len(file_data_json))
	#print(file_data_json[0])
	#print('\n\n AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA \n\n')

	file_data = json.loads(tmp_data_json)
	json_length = len(file_data)
	print('len(file_data)',json_length)
	if json_length > 0:
		#logging.info('== getRandomPythonExampleCode ==> len(file_data):'+len(file_data))
		rand_num = random.randrange(json_length)
		print('rand_num ==>',rand_num)
		print('\n\n')
		print(file_data[0])
		print(file_data[2])
  
		print(file_data[rand_num])
		print('\n\n')
		return file_data[rand_num]

	else:
		example_item_list = pythonCodeExampleList()
		rand_num = random.randrange(len(example_item_list))

		return example_item_list[rand_num]

def showRandomPythonCode(output_type="html"):
	#print('*'*15,'showRandomPythonCode('+output_type+')')
	if output_type == "html":
		#print('*'*15,'if output_type == "html" => getRandomPythonExampleCode()')
		code_list = getRandomPythonExampleCode()
		#print('AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA')
		#code_list.append("AAAAAAAAAAA")
		#print(code_list)
		return code_list
  
	else:
		licz = 0
		start = True
		while start:
			if licz > 0:
				if input("Wylosować kolejny przykład (T/N) ? ") not in ("T","t", ""):
					break
			licz+= 1
			print('\t\t\t ******** Losowanie nr: %i *******' %licz)
			
		code_list = getRandomPythonExampleCode()
		

		try:
			method_list = [code_list[0][1],code_list[0][0]]
		except:
			method_list = []
		try:
			name_list = [code_list[1][1],code_list[1][0]]
		except:
			name_list = []
		try:  
			syntax_list = [code_list[2][1],code_list[2][0]]
		except:
			syntax_list = []
		try:
			parameters_list = code_list[3][1]
		except:
			parameters_list = []
		try:
			use_examples_list = code_list[4][1]
		except:
			use_examples_list = []
		try:
			example_return_list = code_list[5]
		except:
			example_return_list = []

		renderRandomPythonCodeConsoleOutput(method_list, name_list, syntax_list, parameters_list, use_examples_list, example_return_list)
		

def renderRandomPythonCodeConsoleOutput(method_list, name_list, syntax_list, parameters_list, use_examples_list, example_return_list):

		if method_list[0] not in ("Others"):
			print('\n\n\n\t'+'*'*6,method_list[0]+':',name_list[0]+'() ****\n')
		else:
			print('\n\n\n\t'+'*'*6,name_list[0]+' ****\n')
		
		if len(syntax_list) > 0:
			print('\t'+syntax_list[1]+': '+syntax_list[0])

		if len(parameters_list) > 0:
			print('')
			#print('\tParameters type is %s and length: %i ' %(type(parameters_list),len(parameters_list)))
			print('\t'+'_ '*30,'\n')
			print('\tParameter\tDescription')
			print('\t'+'_ '*30,'\n')
			xx = 0
			for val in parameters_list:
				if xx > 0: print()
				print('\t'+val[0]+'\t\t'+val[1])
				xx+= 1

		#print('')
		xx = 0
		while xx < len(use_examples_list):
			if xx == 0: print('\t'+'_ '*30,'\n')
			elif xx > 0: print('')
			print('\t| Example description:',use_examples_list[xx][0])
			print('\t'+'_ '*30)
			print('\n\t| ',use_examples_list[xx][1].replace('\n','\n\t|  '))
			print('\t'+'_ '*30)
			if len(example_return_list) > 1:
				try:
					example_return_info_list = example_return_list[1]
				except:
					example_return_info_list = []
				print()
				print('\t'+example_return_info_list[0][0]+':',example_return_info_list[0][1])
				print('\t'+example_return_info_list[1][0]+':',example_return_info_list[1][1])
				example_return_info_list.clear()
			xx+= 1
	
		print('\n\n')
		
def renderRandomPythonCodeWebsiteOutput(method_list, name_list, syntax_list, parameters_list, use_examples_list, example_return_list):

	return method_list, name_list, syntax_list, parameters_list, use_examples_list, example_return_list


"""
def chwilowa():
	output_str = ""
	if method_list[0] not in ("Others"):
		print('\n\n\n\t'+'*'*6,method_list[0]+':',name_list[0]+'() ****\n')
		output_str = '\n\n\n\t'+'*'*6,method_list[0]+':',name_list[0]+'() ****\n'
	else:
		print('\n\n\n\t'+'*'*6,name_list[0]+' ****\n')
		output_str = '\n\n\n\t'+'*'*6,name_list[0]+' ****\n'
	
	if len(syntax_list) > 0:
		print('\t'+syntax_list[1]+': '+syntax_list[0])
		output_str = '\t'+syntax_list[1]+': '+syntax_list[0]

	if len(parameters_list) > 0:
		print('')
		#print('\tParameters type is %s and length: %i ' %(type(parameters_list),len(parameters_list)))
		print('\t'+'_ '*30,'\n')
		print('\tParameter\tDescription')
		print('\t'+'_ '*30,'\n')
		output_str = '\t'+'_ '*30,'\n'
		output_str = '\tParameter\tDescription'
		output_str = '\t'+'_ '*30,'\n'
		xx = 0
		for val in parameters_list:
			if xx > 0: print()
			print('\t'+val[0]+'\t\t'+val[1])
			output_str = '\t'+val[0]+'\t\t'+val[1]
			xx+= 1

	#print('')
	xx = 0
	while xx < len(use_examples_list):
		if xx == 0: print('\t'+'_ '*30,'\n')
		elif xx > 0: print('')
		print('\t| Example description:',use_examples_list[xx][0])
		print('\t'+'_ '*30)
		print('\n\t| ',use_examples_list[xx][1].replace('\n','\n\t|  '))
		print('\t'+'_ '*30)
		output_str = '\t| Example description:',use_examples_list[xx][0]
		output_str = '\n\t| ',use_examples_list[xx][1].replace('\n','\n\t|  '
		if len(example_return_list) > 1:
			try:
				example_return_info_list = example_return_list[1]
			except:
				example_return_info_list = []
			print()
			print('\t'+example_return_info_list[0][0]+':',example_return_info_list[0][1])
			print('\t'+example_return_info_list[1][0]+':',example_return_info_list[1][1])
			output_str = '\t'+example_return_info_list[0][0]+':',example_return_info_list[0][1]
			output_str = '\t'+example_return_info_list[1][0]+':',example_return_info_list[1][1]
			example_return_info_list.clear()
		xx+= 1

		print('\n\n')

	return output_str
	"""
	
def pythonCodeExampleList(output_type="list"):
	print('','*'*30,'\npythonCodeExampleList('+output_type+')\n','*'*30)
	example_item_list = []

	example_item_list.append([["Type","Metoda"],["Name","String center()"],["Syntax","string.center(length, character)"],["ParameterValue",
									 	[
										 ["length","Required. The length of the returned string"],
										 ["character","Optional. The character to fill the missing space on each side. Default is \" \" (space)"]
										]
									],["UseExample",
										[
										 ["Using the char \"+_\" as the padding character:", "text = \"powidła\"\n\nx = text.center(20, \"+_\")"]
										]
									],["Return","String"]])

	example_item_list.append([["Type","Metoda"],["Name","randrange()"],["Syntax","random.randrange(start, stop, step)"],["ParameterValue",
									 	[
										 ["start","Optional. An integer specifying at which position to start. Default 0"],
										 ["stop","Required. An integer specifying at which position to end."],
										 ["step","Optional. An integer specifying the incrementation. Default 1"]
										]
									],["UseExample",
										[
										 ["Return a number between 0 and 5", "import random\n\nprint(random.randrange(0, 5))"]
										]
									],["Return",""]])
 
	example_item_list.append([["Type","Metoda"],["Name","Sort()"],["Syntax","list.sort(reverse=True|False, key=myFunc)"],["ParameterValue",
									 	[
										 ["reverse","Optional. reverse=True will sort the list descending. Default is reverse=False"],
										 ["key","Optional. A function to specify the sorting criteria(s)"]
										]
									],["UseExample",
										[
										 ["Sort the list descending", "numbers_list = [5, 1, 4]<br><br>numbers_list.sort(reverse=True)"]
										]
									],["Return",
									 	[
											["ReturnType","list"],
											["ReturnValue","[1, 4, 5]"]
										]
									]])
	#print('len:',len(example_item_list),example_item_list[-1][0])
	
	example_item_list.append([["Type","Others"],["Name","Change List Items"],["Syntax",""],["ParameterValue",""
                    ],["UseExample",
										[
										 ["Change second item value", "pisaki_list = [\"pióro\", \"oliwa\", \"długopis\", \"ołówek\"]\n\npisaki_list[1] = \"mazak\""],
										 ["Change a Range of Item Values", "pisaki_list = [\"pióro\", \"oliwa\", \"burak\", \"ołówek\"]\n\npisaki_list[1:3] = [\"mazak\",\"długopis\"]"]
										]
									],["Return",""]])
	
	if output_type == "json":
		print('\n\n\t\t\t','*'*20)
		print('\t\t\t\t convertListToJsonString() - START')
		resp_example_json_str = convertListToJsonString(example_item_list)
		print(resp_example_json_str)
		print('\t\t\t\t convertListToJsonString() - KONIEC')
		print('\n\n\t\t\t','*'*20)
		return resp_example_json_str
	else:
		return example_item_list
