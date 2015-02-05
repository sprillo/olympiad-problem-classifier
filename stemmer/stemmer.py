from stemming.porter2 import stem
# package can be found here: https://pypi.python.org/pypi/stemming/1.0

def stemmear_enunciado(enunciado):
	enunciado = enunciado.split(",",2)
	res = []
	res.append(enunciado[0][3:-2])
	res.append(enunciado[1][2:-2])
	enunciado = enunciado[2]
	enunciado = enunciado[:-3]
	enunciado = enunciado.split(",")
	enunciado = map(lambda x: x[1:-1],enunciado)
	for palabra in enunciado:
		res.append(stem(palabra).lower())
	return res

def tokenize_all():
	input_file = open("../tokenizer/enunciados_tokenizados.txt","r")
	output_file = open("enunciados_stemmeados.txt","w")
	for enunciado in input_file:
		enunciado_stemmeado = stemmear_enunciado(enunciado)
		output_file.write(str(enunciado_stemmeado))
		output_file.write('\n')

tokenize_all()