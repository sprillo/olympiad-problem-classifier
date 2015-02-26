import re

def read_weights():
	weights_file = open("weights.txt","r")
	weights_string = weights_file.read()
	sp = weights_string.split()
	nx4 = len(sp)
	assert nx4 % 4 == 0
	n = nx4 / 4
	weights = [[0] * n for i in range(4)]
	for i in range(n):
		for j in range(4):
			weights[j][i] = float(sp[4 * i + j])
	return weights
	
import tokenizer
import stemmer
import vectorizer

def read_dictionary():
	dictionary_file = open("dictionary.txt","r")
	dictionary = []
	for line in dictionary_file:
		dictionary.append(re.sub('\n','',line))
	dictionary_file.close()
	return dictionary

def read_statement():
	statement_file = open("statement.txt","r")
	statement = statement_file.read()
	statement_file.close()
	return statement

def inner_product(u, v):
	return sum(map(lambda i: u[i] * v[i], range(len(u))))

import math

def classify(statement, weights):
	probabilities = map(lambda i: 1. / (1 + math.exp(-inner_product(weights[i],statement))), range(4))
	mp = max(probabilities)
	problem_class = None
	if probabilities[0] == mp:
		problem_class = "Algebra"
	elif probabilities[1] == mp:
		problem_class = "Combinatorics"
	elif probabilities[2] == mp:
		problem_class = "Geometry"
	elif probabilities[3] == mp:
		problem_class = "Number Theory"
	else:
		assert False
	normalized_probabilities = map(lambda p: p / sum(probabilities), probabilities)
	normalized_mp = mp / sum(probabilities)
	assert abs(sum(normalized_probabilities) - 1.) < .001
	print normalized_probabilities
	print "Problem belongs to", problem_class, "with probability", str(int(100 * normalized_mp)) + " %"


def doit():
	weights = read_weights()
	dictionary = read_dictionary()
	statement = read_statement()
	statement = tokenizer.tokenize_statement(statement)
	statement = stemmer.stem_statement2(statement)
	statement = vectorizer.vectorize_statement2(statement,dictionary)
	statement = [1] + statement
	classify(statement,weights)
	

doit()