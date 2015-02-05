from __future__ import print_function # para stderr
import sys
import time

def console(*objs):
    print("> ", *objs, file=sys.stderr)
    
# crawler propiamente dicho:

delay = 1

import re, urllib

def get_tipo_str(tipo):
	tipo_str = 'None'
	if(tipo == 0):
		tipo_str = 'Algebra'
	elif(tipo == 1):
		tipo_str = 'Combinatorics'
	elif(tipo == 2):
		tipo_str = 'Geometry'
	elif(tipo == 3):
		tipo_str = 'Number Theory'
	assert tipo_str != 'None'
	return tipo_str

def crawl_problem_statement(tipo,url_problema):
	global delay
	
	f = open('enunciados.txt','a')
	
	while True:
		try:
			pagina = urllib.urlopen(url_problema)
			delay = max(1,delay/2)
			break
		except IOError:
			print('\nIOError: Delaying ' + str(delay) + ' time.\n')
			time.sleep(delay)
			delay = min(2 * delay,256)

	contenido = pagina.read()
	
	contenido = re.sub('\\t','       ',contenido)
	contenido = re.sub('\\n','       ',contenido)
	
	# view-source:http://www.artofproblemsolving.com/Forum/viewtopic.php?f=37&t=5560
	# http://www.regular-expressions.info/lookaround.html
	enunciados = re.findall('\<div class="postbody"\>.*?\</div\>       ',contenido,re.S)
	
	assert len(enunciados) > 0
	
	tipo_str = get_tipo_str(tipo)				
	enunciado = enunciados[0]
	#f.write(enunciado)
	#f.write(str(len(enunciados)))
	#f.write('\n')
	#f.close()
	
	enunciado = re.sub('\\xc3\\xa1','a',enunciado)
	enunciado = re.sub('\\xc3\\x81','A',enunciado)
	enunciado = re.sub('\\xc3\\xa9','e',enunciado)
	enunciado = re.sub('\\xc3\\x89','E',enunciado)
	enunciado = re.sub('\\xc3\\xad','i',enunciado)
	enunciado = re.sub('\\xc3\\x93','o',enunciado)
	enunciado = re.sub('\\xc3\\xb3','o',enunciado)
	enunciado = re.sub('\\xc3\\xba','u',enunciado)
	
	enunciado = re.sub('\\xc3\\xb1','ENIE',enunciado)
	enunciado = re.sub('\\xc3\\x91','ENIE',enunciado)
	enunciado = re.sub('\\xc3\\x97',' X ',enunciado)

	enunciado = re.sub('\\xc3a','a',enunciado)
	enunciado = re.sub('\\xc3e','e',enunciado)
	enunciado = re.sub('\\xc3i','i',enunciado)
	enunciado = re.sub('\\xc3o','o',enunciado)
	enunciado = re.sub('\\xc3u','u',enunciado)

	enunciado = re.sub('\\xc2\\xba',' DEG ',enunciado) # simbolo ^circ
	enunciado = re.sub('\\xc2\\xb0',' DEG ',enunciado) # simbolo ^circ

	enunciado = re.sub('\\xc2\\xbf','',enunciado) # signos de pregunta invertidos
	enunciado = re.sub('\\xc2\\xa1',' ',enunciado) # signos de exclamacion invertidos

	enunciado = re.sub('\\xc2\\xb7',' BULLET ',enunciado) # bullets
	enunciado = re.sub('\\xe2\\x80\\x9c',' ',enunciado) # "
	enunciado = re.sub('\\xe2\\x80\\x9d',' ',enunciado) # "
	enunciado = re.sub('\\xc2\\xb1',' PLUSMINUS ',enunciado) # +-
	
	latex = ''
	for x in re.findall('title="[^"]+"',enunciado,re.I):
		latex = latex + ' $' + x[7: len(x) - 1] + '$ '
	enunciado = re.sub('\<[^\>]+\>',' ',enunciado)
	
	enunciado = enunciado + latex
	
	datos_problema = (url_problema,tipo_str,enunciado)
	datos_problema_str = str(datos_problema)
	f.write(datos_problema_str)
	f.write('\n')


def crawl_problem_list(tipo,url_problem_list):
	global delay
	
	print('Crawling ' + str(url_problem_list) + '\n')
	
	while True:
		try:
			pagina = urllib.urlopen(url_problem_list)
			delay = max(1,delay/2)
			break
		except IOError:
			print('\nIOError: Delaying ' + str(delay) + ' time.\n')
			time.sleep(delay)
			delay = min(2 * delay,256)
	
	contenido = pagina.read()
	lineas_con_hyperrefs_a_problemas = re.findall('\<a title="Posted:.*\</a\>',contenido)
	longitud = len(lineas_con_hyperrefs_a_problemas)
	for linea in lineas_con_hyperrefs_a_problemas[max(0,longitud - 40):max(0,longitud)]:#porque los primeros posts son stickies
		hyperrefs = re.findall('href="[^"]+"',linea)
		assert len(hyperrefs) == 1
		hyperref = re.sub('&amp;','&',hyperrefs[0][7:(len(hyperrefs[0]) - 6)])
		url_problema = 'http://www.artofproblemsolving.com/Forum' + hyperref
		#print(url_problem)
		crawl_problem_statement(tipo,url_problema)

valor_de_f_tipo = 		[[-1,38,-1,37,-1],[-1,42,-1,44,-1],[-1,47,-1,49,-1],[-1,57,-1,59,-1]]
cantidad_paginas_tipo = [[-1,112,-1,25,-1],[-1,112,-1,8,-1],[-1,112,-1,38,-1],[-1,112,-1,19,-1]]

def crawl():
	for tipo in range(4):
		for start_idx in range(0,40 * cantidad_paginas_tipo[tipo][1],40):
			url = 'http://www.artofproblemsolving.com/Forum/viewforum.php?f=' + str(valor_de_f_tipo[tipo][1]) + '&start=' + str(start_idx)
			crawl_problem_list(tipo,url)

crawl()
