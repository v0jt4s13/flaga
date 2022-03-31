
#from app_files.moje_biblioteki import *
from ast import Break
from app_files.random_python_code import showRandomPythonCode, pythonCodeExampleList, getRandomPythonExampleCode

def rpc():
	
	#print(pythonCodeExampleList(output_type="json"))
 
	err = ""
	try:
		print('*'*15,'try showRandomPythonCode()')
		#random_python_code_list = showRandomPythonCode()
		random_python_code_list = getRandomPythonExampleCode()
		print(type(list(random_python_code_list)),random_python_code_list)
	except ValueError as e:
		err = e

from app_files.random_python_code import *
from app_files.moje_biblioteki import *

file_name = flaga_root_folder()+'static/json/test_python_code.json'
json_str = pythonCodeExampleList(output_type="json")
#saveJsonStringToFile(file_name,json_str)
	
#rpc()


def move_zeros(arr):
    array = [i for i in arr if isinstance(i, bool) or i!=0]
    return array+[0]*(len(arr)-len(array))

arr = [1,0,0,0,2,3,2] #,0,3,1,0,0,0,2,3,2,0,3,1,0,0,0,2,3,2,0,3,1,0,0,0,2,3,2,0,3,1,0,0,0,2,3,2,0,3,1,0,0,0,2,3,2,0,3]
print(move_zeros(arr))

def move_zeros(arr):
	l = [i for i in arr if i > 0]
	while len(l)<len(arr): l.append(0)
	return l

print(move_zeros(arr))

#from app_files.random_python_code import pythonCodeExampleList
#print(pythonCodeExampleList(output_type="json"))


def program_pokaz_text():
	
	print('\n\n\n')
	i = input("\t\tCześć, jak sie masz? ")
	print('\n\t\tWięc mówisz że '+i+'.')

program_pokaz_text()

text = "powidła"
x = text.center(20, "+")
print(x)


ilosc_znakow_w_linii = 80
print()
print('*'*ilosc_znakow_w_linii)
txt1 = " text wycentrowany "
txt2 = "do "+str(ilosc_znakow_w_linii)+" znaków w linii"
x1 = txt1.center(ilosc_znakow_w_linii,'-')
x2 = txt2.center(ilosc_znakow_w_linii)
print(x1)
print(x2)
print('*'*ilosc_znakow_w_linii)
print()

def pytanie_o_cyfre():
	while True:
		i = input('wpisz cyfre ')
		if isinstance(int(i)*1, int):
			i = int(i)
			print('Świetnie, Twoja cyfra to:',i)
			break
		else:
			print('To nie jest cyfra typu intiger, spróbuj ponownie.')
			continue

	return i

i = pytanie_o_cyfre()
print(i)


def f_usun_wartosc(arr,i):
  arr.remove(i)
  return arr

arr = [1,2,3,4,5,6,7,8,9]
print('Tablica na wejsciu:',arr)
for i in arr:
  if i % 2 == 0:
    f_usun_wartosc(arr,i)
    #arr.remove(i)
print('Tablica na wyjsciu:',arr)


Telewizja = [{'nazwa': 'film1', 'start': 9, 'end': 12, 'czas': 3},
             {'nazwa': 'film2', 'start': 15, 'end': 17, 'czas': 2},
             {'nazwa': 'film3', 'start': 11, 'end': 16, 'czas': 5},
             {'nazwa': 'film4', 'start': 12, 'end': 14, 'czas': 2},
             {'nazwa': 'film5', 'start': 11.5, 'end': 12.5, 'czas': 1}]

def in_rangeA(film,min,tv_list):
	if int(film['start'])*10 not in range(int(min['start'])*10,int(min['end'])*10) and int(film['end'])*10 not in range(int(min['start'])*10,int(min['end'])*10):
		tv_list.append(film)
		print(tv_list)
	return tv_list

def in_rangeB(film,min,tv_list): #Funkcja która usuwa z tv_list nakładające sie programy na najkrotszy z nich(a - film który sprawdzamy, najkrotszy program, lista z której usuwamy)
	print(len(tv_list),' ===> ',film)
	#W funkcji sprawdzam czy poczatek lub koniec sprawdzanego programu zawiera sie w przedziale (poczatek najkrotszego programu i koniec najkrotszego programu)
	#Oraz czy poczatek lub koniec najkrotszego programu zawiera sie w przedziale (poczatek sprawdzanego programu,koniec sprawdzanego programu)
	#Pomnozone *10 żeby uniknąć floatów.
	#print('if ',film['start']*10,' in range(',int(min['start']*10),',',int(min['end']*10),')')
	if film['start']*10 in range(int(min['start']*10),int(min['end']*10)) \
		or film['end']*10 in range(int(min['start']*10),int(min['end']*10)) \
		or int(min['start']*10) in range(int(film['start']*10),int(film['end']*10)) \
		or int(min['end']*10) in range(int(film['start']*10),int(film['end']*10)):
		print(f'\tusuwanie {film}')
		tv_list.remove(film)
		print('\t\tpo usuwaniu',tv_list)
	return tv_list

def in_rangeC(film,min,tv_list): #Funkcja która usuwa z tv_list nakładające sie programy na najkrotszy z nich(a - film który sprawdzamy, najkrotszy program, lista z której usuwamy)
	#print(len(tv_list),' ===> ',film)
	remove_film = ""
	if film['start']*10 in range(int(min['start']*10),int(min['end']*10)):
		remove_film = str(film['start']*10)+' in '+str(range(int(min['start']*10),int(min['end']*10)))
	elif film['end']*10 in range(int(min['start']*10),int(min['end']*10)):
		remove_film = str(film['end']*10)+' in '+str(range(int(min['start']*10),int(min['end']*10)))
	elif int(min['start']*10) in range(int(film['start']*10),int(film['end']*10)):
		remove_film = str(int(min['start']*10))+' in '+str(range(int(film['start']*10),int(film['end']*10)))
	elif int(min['end']*10) in range(int(film['start']*10),int(film['end']*10)):
		remove_film = str(int(min['end']*10))+' in '+str(range(int(film['start']*10),int(film['end']*10)))
  
	if remove_film != "":
		print(f'\t\t\t\tin_rangeC ==> {remove_film} ==> do usuniecia {film}')
		return False

	return True

def in_rangeRemove(film,min,tv_list): #Funkcja która usuwa z tv_list nakładające sie programy na najkrotszy z nich(a - film który sprawdzamy, najkrotszy program, lista z której usuwamy)
	#print(len(tv_list),' ===> ',film)
	remove_film = ""
	if film['start']*10 in range(int(min['start']*10),int(min['end']*10)):
		remove_film = str(film['start']*10)+' in '+str(range(int(min['start']*10),int(min['end']*10)))
	elif film['end']*10 in range(int(min['start']*10),int(min['end']*10)):
		remove_film = str(film['end']*10)+' in '+str(range(int(min['start']*10),int(min['end']*10)))
	elif int(min['start']*10) in range(int(film['start']*10),int(film['end']*10)):
		remove_film = str(int(min['start']*10))+' in '+str(range(int(film['start']*10),int(film['end']*10)))
	elif int(min['end']*10) in range(int(film['start']*10),int(film['end']*10)):
		remove_film = str(int(min['end']*10))+' in '+str(range(int(film['start']*10),int(film['end']*10)))
  
	if remove_film != "":
		print(f'\t\t\t\tin_rangeRemove ==> {remove_film} ==> do usuniecia {film}')
		tv_list.remove(film)

	return tv_list
    
def alg_B(tv_list):
	#print('1. tv_list: ',tv_list)
	min = tv_list[0]
	watch = []
	for film in tv_list: #Tutaj jest wybór najkrótszego programu, jest wszystko git
		if film['end'] - film['start'] == min['end'] - min['start']:
			if film['end'] < min['end']:
				min = film
			if (film['end'] - film['start'])*10 < (min['end'] - min['start'])*10:
				min = film
	tv_list.remove(min)
	#print('2. tv_list: ',tv_list)
 
	for film in tv_list: #Iteruje po liście programów bez najkrótszego
		print(f'\t\t=TV len={len(tv_list)}===> {film} <=====')
		#watch = in_rangeB(film,min,tv_list) #Film z listy programów bez najkrotszego programu,najkrotszy program, Program telewizyjny bez najkrotszego programu
		if in_rangeC(film,min,tv_list):
			watch.append(film)		
  
	#watch.append(min) #Dodaje min do listy programów
	
	return watch #Zwraca liste programów które mozna obejrzec.

def alg_B2(tv_list):
	min = tv_list[0]
	watch = []
	for film in tv_list: #Tutaj jest wybór najkrótszego programu, jest wszystko git
		if film['end'] - film['start'] == min['end'] - min['start']:
			if film['end'] < min['end']:
				min = film
			if (film['end'] - film['start'])*10 < (min['end'] - min['start'])*10:
				min = film
	tv_list.remove(min)
 
	for film in tv_list: #Iteruje po liście programów bez najkrótszego
		print(f'\t\t=TV len={len(tv_list)}===> {film} <=====')
		#watch = in_rangeB(film,min,tv_list) #Film z listy programów bez najkrotszego programu,najkrotszy program, Program telewizyjny bez najkrotszego programu
		watch = in_rangeRemove(film,min,tv_list)
			
	watch.append(min) # ?? co ta linia ma robic ? dodac to co zostalo usuniete kilka linii wyzej -->> tv_list.remove(min)
  
	#watch.append(min) #Dodaje min do listy programów
	
	return watch #Zwraca liste programów które mozna obejrzec.

print('\tDane wejsciowe:',Telewizja,'\n')
print('\n\n','*-* '*25)
print('\t\t>>>> Telewizja alg_B <<<<'.center(75))
print('','*-* '*25,'\n')
print('\n\tKoniec ==> ',alg_B(Telewizja))

print('\n\n','*-* '*25)
print('\t\t>>>> Telewizja alg_B2 <<<<'.center(75))
print('','*-* '*25,'\n')
print('\n\tKoniec ==> ',alg_B2(Telewizja))