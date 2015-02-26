from __future__ import print_function # para stderr
import sys
import tokenizer
import stemmer
import vectorizer

def console(*objs):
    print("> ", *objs, file=sys.stderr)

import re

def read_statements():
	print("Reading raw statements ...")
	input_file = open('statements_raw.txt','r')
	res = []
	for statement in input_file:
		res.append(statement)
	input_file.close()
	return res

## Dictionary

def create_dictionary(statements_stemmed):
	print("Creating dictionary ...")
	LOWER_BOUND = 20
	word_appearances = dict()
	for statement in statements_stemmed:
		statement = statement[2:]
		words = set(statement)
		for word in words:
			if word in word_appearances:
				word_appearances[word] = word_appearances[word] + 1
			else:
				word_appearances[word] = 1
	res = []
	for word in word_appearances:
		if word_appearances[word] >= LOWER_BOUND:
			res.append(word)
	res.sort()
	output_file = open("dictionary.txt","w")
	for word in res:
		output_file.write(word)
		output_file.write("\n")
	output_file.close()
	return res



def write_data(statements_vectorized, dictionary):
	print("Writing processed statements to file ...")
	output_file = open("statements_processed.txt","w")
	output_file.write("url class ")
	for word in dictionary:
		output_file.write(word)
		output_file.write(" ")
	output_file.write("\n")
	for statement in statements_vectorized:
		for word in statement:
			output_file.write(str(word).replace(" ",""))
			output_file.write(" ")
		output_file.write("\n")
	output_file.close()

def process():
	statements = read_statements()
	statements_tokenized = tokenizer.tokenize(statements)
	statements_stemmed = stemmer.stem_all(statements_tokenized)
	dictionary = create_dictionary(statements_stemmed)
	statements_vectorized = vectorizer.vectorize_statements(statements_stemmed, dictionary)
	write_data(statements_vectorized, dictionary)

process()

