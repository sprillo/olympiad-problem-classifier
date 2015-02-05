from __future__ import print_function # para stderr
import sys

def console(*objs):
    print("> ", *objs, file=sys.stderr)

import re

# TESTEAR ''TODAS'' LAS REGEX!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

	features_extra = ''
	
	enunciado = re.sub('\\\\\\\\','\\\\',enunciado)
	enunciado = re.sub('&lt;','<',enunciado)
	enunciado = re.sub('&gt;','>',enunciado)
	
	# saco los caracteres molestos
	# los pesos y llaves los saco al final porque me sirven para identificar cosas de geometria con certeza
	enunciado = re.sub('\\\\bigl\(','(',enunciado)
	enunciado = re.sub('\\\\bigr\)',')',enunciado)
	enunciado = re.sub('\\\\left\(','(',enunciado)
	enunciado = re.sub('\\\\right\)',')',enunciado)
	
	enunciado = re.sub('co-prime','coprime',enunciado)
	enunciado = re.sub('positive[ ]+integers?',' __POSITIVEINTEGERS ',enunciado)
	enunciado = re.sub('(non-?)?[ ]*negative[ ]+integers?',' __NONNEGATIVEINTEGERS ',enunciado)
	enunciado = re.sub('positive[ ]+reals?[ ]+(numbers?)?',' __POSITIVEREALNUMBERS ',enunciado)
	enunciado = re.sub('(non-?)?[ ]*negative[ ]+reals?[ ]+(numbers?)?',' __NONNEGATIVEREALNUMBERS ',enunciado)
	enunciado = re.sub('pairwise[ ]+neighbour(ing)?',' __PAIRWISENEIGHBOURING ',enunciado)
	enunciado = re.sub('relatively([ ]+(co)?(prime))?',' __RELATIVELYPRIME ',enunciado)
	enunciado = re.sub('perfect[ ]+squares?',' __PERFECTSQUARES ',enunciado)
	enunciado = re.sub('perfect[ ]+cubes?',' __PERFECTCUBES ',enunciado)
	enunciado = re.sub('perfect[ ]+powers?',' __PERFECTPOWERS ',enunciado)
	enunciado = re.sub('inte(ger|gral)[ ]+sides?[ ]*(lengths?)?',' __INTEGERSIDELENGTH ',enunciado)
	
	enunciado = re.sub('\\\\pmod',' __LATEXPMOD ',enunciado)
	enunciado = re.sub('\\\\equiv',' __LATEXEQUIV ',enunciado)
	enunciado = re.sub('\\\\sqrt',' __LATEXSQRT ',enunciado)
	enunciado = re.sub('\^\{\\\\circ\}',' __LATEXPOWCIRC ',enunciado)
	enunciado = re.sub('\\\\d?frac',' __LATEXFRACT ',enunciado)
	enunciado = re.sub('\\\\prod(_\{[^\}]*\}\^\{[^\}]*\})?',' __LATEXPRODUCT ',enunciado)
	enunciado = re.sub('\\\\sum(_\{[^\}]*\}\^\{[^\}]*\})?',' __LATEXSUM ',enunciado)
	
	# $ 2014! $
	#enunciado = re.sub('\$[^\$]+![^\$]+\$',' __LATEXFACTORIAL ',enunciado)
	if re.search('\$[^\$]+![^\$]+\$',enunciado,0):
		features_extra = features_extra + ' __LATEXFACTORIAL '
	
	
	
	################## DECLARACION DE FUNCIONES #########################
	# TIENE QUE VENIR ANTES QUE EXPONENCIACION
	
	# $f : \mathbb Z \rightarrow \mathbb N_{\ge 0}$
	enunciado = re.sub('[a-z,A-Z]+[ ]*:[^\$]*\{?(Z|N)\}?((\^|_)?((\+)|(\{[^\}]\})))?[ ]*\\\\((rightarrow)|(to))[^\$]*\{?(Z|N)\}?((\^|_)?((\+)|(\{[^\}]\})))?',' __LATEXINTEGRALFUNCIONDEFINITION ',enunciado)	
	#if re.search('[a-z,A-Z]+[ ]*:[^\$]*\{?R\}?(\^(\+|(\{\+\})))?[ ]*\\\\((rightarrow)|(to))[^\$]*\{?R\}?(\^(\+|(\{\+\})))?',enunciado,0):
		#features_extra = features_extra + ' __LATEXREALFUNCIONDEFINITION '
	
	# $f : \mathbb R \rightarrow \mathbb R_{\ge 0}$
	enunciado = re.sub('[a-z,A-Z]+[ ]*:[^\$]*\{?R\}?((\^|_)?((\+)|(\{[^\}]\})))?[ ]*\\\\((rightarrow)|(to))[^\$]*\{?R\}?((\^|_)?((\+)|(\{[^\}]\})))?',' __LATEXREALFUNCIONDEFINITION ',enunciado)	
	#if re.search('[a-z,A-Z]+[ ]*:[^\$]*\{?R\}?(\^(\+|(\{\+\})))?[ ]*\\\\((rightarrow)|(to))[^\$]*\{?R\}?(\^(\+|(\{\+\})))?',enunciado,0):
		#features_extra = features_extra + ' __LATEXREALFUNCIONDEFINITION '
		
	# $f : \mathbb Z \rightarrow \mathbb N_{\ge 0}$
	enunciado = re.sub('[a-z,A-Z]+[ ]*:[^\$]*\{?(Z|N|Q)\}?((\^|_)?((\+)|(\{[^\}]\})))?[ ]*\\\\((rightarrow)|(to))[^\$]*\{?(Z|N|Q)\}?((\^|_)?((\+)|(\{[^\}]\})))?',' __LATEXRATIONALFUNCIONDEFINITION ',enunciado)	
	#if re.search('[a-z,A-Z]+[ ]*:[^\$]*\{?R\}?(\^(\+|(\{\+\})))?[ ]*\\\\((rightarrow)|(to))[^\$]*\{?R\}?(\^(\+|(\{\+\})))?',enunciado,0):
		#features_extra = features_extra + ' __LATEXREALFUNCIONDEFINITION '
	
	# $f : \mathbb R \rightarrow \mathbb N_{\ge 0}$
	enunciado = re.sub('[a-z,A-Z]+[ ]*:[^\$]*\{?(R|Z|N|Q)\}?((\^|_)?((\+)|(\{[^\}]\})))?[ ]*\\\\((rightarrow)|(to))[^\$]*\{?(R|Z|N|Q)\}?((\^|_)?((\+)|(\{[^\}]\})))?',' __LATEXGENERALFUNCIONDEFINITION ',enunciado)	
	#if re.search('[a-z,A-Z]+[ ]*:[^\$]*\{?R\}?(\^(\+|(\{\+\})))?[ ]*\\\\((rightarrow)|(to))[^\$]*\{?R\}?(\^(\+|(\{\+\})))?',enunciado,0):
		#features_extra = features_extra + ' __LATEXREALFUNCIONDEFINITION '
	
	
	################## DECLARACION DE TIPOS #########################
	# TIENE QUE VENIR DESPUES DE DECLARACION DE FUNCIONES Y ANTES QUE EXPONENCIACION
	
	# y\\in\\mathbb{Z_{\\ge 0}}
	enunciado = re.sub('[a-z,A-Z][ ]*\\\\in[ ]*[^\$]*\{?Z(\^|_)((\+)|(\{[^\}]*\}))\}?',' __LATEXVARINZSOMETHING ',enunciado)
	#if re.search('[a-z,A-Z][ ]*\\\\in[ ]*\\\\mathbb[ ]*\{?Z(\^(\+|(\{\+\})))\}?',enunciado,0):
		#features_extra = features_extra + ' __LATEXVARINR '
	
	# \\mathbb Z^{\\ge 0}
	enunciado = re.sub('\\\\mathbb[ ]*\{?Z(\^|_)((\+)|(\{[^\}]*\}))\}?',' __LATEXZSOMETHING ',enunciado)
	#if re.search('\\\\mathbb[ ]*\{?Z\}?((\^|_)(\{?\+\}?))?',enunciado,0):
		#features_extra = features_extra + ' __LATEXINTEGERSPOSITIVE '
	
	# y\\in\\mathbb{Z}
	enunciado = re.sub('[a-z,A-Z][ ]*\\\\in[ ]*[^\$]*\{?Z\}?',' __LATEXVARINZ ',enunciado)
	#if re.search('[a-z,A-Z][ ]*\\\\in[ ]*\\\\mathbb[ ]*\{?Z(\^(\+|(\{\+\})))\}?',enunciado,0):
		#features_extra = features_extra + ' __LATEXVARINR '
	
	# \\mathbb Z
	enunciado = re.sub('\\\\mathbb[ ]*\{?Z\}?',' __LATEXZ ',enunciado)
	#if re.search('\\\\mathbb[ ]*\{?Z\}?((\^|_)(\{?\+\}?))?',enunciado,0):
		#features_extra = features_extra + ' __LATEXINTEGERSPOSITIVE '
	
	
	# y\\in\\mathbb{R_{\\ge 0}}
	enunciado = re.sub('[a-z,A-Z][ ]*\\\\in[ ]*[^\$]*\{?R(\^|_)((\+)|(\{[^\}]*\}))\}?',' __LATEXVARINRSOMETHING ',enunciado)
	#if re.search('[a-R,A-R][ ]*\\\\in[ ]*\\\\mathbb[ ]*\{?R(\^(\+|(\{\+\})))\}?',enunciado,0):
		#features_extra = features_extra + ' __LATEXVARINR '
	
	# \\mathbb R^{\\ge 0}
	enunciado = re.sub('\\\\mathbb[ ]*\{?R(\^|_)((\+)|(\{[^\}]*\}))\}?',' __LATEXRSOMETHING ',enunciado)
	#if re.search('\\\\mathbb[ ]*\{?R\}?((\^|_)(\{?\+\}?))?',enunciado,0):
		#features_extra = features_extra + ' __LATEXINTEGERSPOSITIVE '
	
	# y\\in\\mathbb{R}
	enunciado = re.sub('[a-z,A-Z][ ]*\\\\in[ ]*[^\$]*\{?R\}?',' __LATEXVARINR ',enunciado)
	#if re.search('[a-R,A-R][ ]*\\\\in[ ]*\\\\mathbb[ ]*\{?R(\^(\+|(\{\+\})))\}?',enunciado,0):
		#features_extra = features_extra + ' __LATEXVARINR '
	
	# \\mathbb R
	enunciado = re.sub('\\\\mathbb[ ]*\{?R\}?',' __LATEXR ',enunciado)
	#if re.search('\\\\mathbb[ ]*\{?R\}?((\^|_)(\{?\+\}?))?',enunciado,0):
		#features_extra = features_extra + ' __LATEXINTEGERSPOSITIVE '
		
	
	# y\\in\\mathbb{Q_{\\ge 0}}
	enunciado = re.sub('[a-z,A-Z][ ]*\\\\in[ ]*[^\$]*\{?Q(\^|_)((\+)|(\{[^\}]*\}))\}?',' __LATEXVARINQSOMETHING ',enunciado)
	#if re.search('[a-Q,A-Q][ ]*\\\\in[ ]*\\\\mathbb[ ]*\{?Q(\^(\+|(\{\+\})))\}?',enunciado,0):
		#features_extra = features_extra + ' __LATEXVARINR '
	
	# \\mathbb Q^{\\ge 0}
	enunciado = re.sub('\\\\mathbb[ ]*\{?Q(\^|_)((\+)|(\{[^\}]*\}))\}?',' __LATEXQSOMETHING ',enunciado)
	#if re.search('\\\\mathbb[ ]*\{?Q\}?((\^|_)(\{?\+\}?))?',enunciado,0):
		#features_extra = features_extra + ' __LATEXINTEGERSPOSITIVE '
	
	# y\\in\\mathbb{Q}
	enunciado = re.sub('[a-z,A-Z][ ]*\\\\in[ ]*[^\$]*\{?Q\}?',' __LATEXVARINQ ',enunciado)
	#if re.search('[a-Q,A-Q][ ]*\\\\in[ ]*\\\\mathbb[ ]*\{?Q(\^(\+|(\{\+\})))\}?',enunciado,0):
		#features_extra = features_extra + ' __LATEXVARINR '
	
	# \\mathbb Q
	enunciado = re.sub('\\\\mathbb[ ]*\{?Q\}?',' __LATEXQ ',enunciado)
	#if re.search('\\\\mathbb[ ]*\{?Q\}?((\^|_)(\{?\+\}?))?',enunciado,0):
		#features_extra = features_extra + ' __LATEXINTEGERSPOSITIVE '
	
	
	########################## EXPONENCIACION ###########################
	
	# ^2 OJO QUE LOS \{? \}? MATCHEAN COSAS COMO x^{2t}!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
	#enunciado = re.sub('\^(2)',' __LATEXEXPTWO ',enunciado)
	if re.search('\^(2)',enunciado,0):
		features_extra = features_extra + ' __LATEXEXPTWO '
		enunciado = re.sub('\^(2)',' ',enunciado)
	
	#enunciado = re.sub('\^(\{2\})',' __LATEXEXPTWO ',enunciado)
	if re.search('\^(\{2\})',enunciado,0):
		features_extra = features_extra + ' __LATEXEXPTWO '
		enunciado = re.sub('\^(\{2\})',' ',enunciado)
	
	# ^3
	#enunciado = re.sub('\^(\d)',' __LATEXEXPGETHREE ',enunciado)
	if re.search('\^(\d)',enunciado,0):
		features_extra = features_extra + ' __LATEXEXPGETHREE '
		enunciado = re.sub('\^(\d)',' ',enunciado)
		
	#enunciado = re.sub('\^(\{\d+\})',' __LATEXEXPGETHREE ',enunciado)
	if re.search('\^(\{\d+\})',enunciado,0):
		features_extra = features_extra + ' __LATEXEXPGETHREE '
		enunciado = re.sub('\^(\{\d+\})',' ',enunciado)
	
	# ^m
	#enunciado = re.sub('\^((m|n))',' __LATEXEXPMorN ',enunciado)
	if re.search('\^((m|n))',enunciado,0):
		features_extra = features_extra + ' __LATEXEXPMorN '
		enunciado = re.sub('\^((m|n))',' ',enunciado)

	#enunciado = re.sub('\^(\{(m|n)\})',' __LATEXEXPMorN ',enunciado)
	if re.search('\^(\{(m|n)\})',enunciado,0):
		features_extra = features_extra + ' __LATEXEXPMorN '
		enunciado = re.sub('\^(\{(m|n)\})',' ',enunciado)
	
	# ^p
	#enunciado = re.sub('\^(p)',' __LATEXEXPP ',enunciado)
	if re.search('\^(p)',enunciado,0):
		features_extra = features_extra + ' __LATEXEXPP '
		enunciado = re.sub('\^(p)',' ',enunciado)
	
	#enunciado = re.sub('\^(\{p\})',' __LATEXEXPP ',enunciado)
	if re.search('\^(\{p\})',enunciado,0):
		features_extra = features_extra + ' __LATEXEXPP '
		enunciado = re.sub('\^(\{p\})',' ',enunciado)
	
	# ^r
	#enunciado = re.sub('\^((q|r))',' __LATEXEXPQ ',enunciado)
	if re.search('\^((q|r))',enunciado,0):
		features_extra = features_extra + ' __LATEXEXPQ '
		enunciado = re.sub('\^((q|r))',' ',enunciado)
	
	#enunciado = re.sub('\^(\{(q|r)\})',' __LATEXEXPQ ',enunciado)
	if re.search('\^(\{(q|r)\})',enunciado,0):
		features_extra = features_extra + ' __LATEXEXPQ '
		enunciado = re.sub('\^(\{(q|r)\})',' ',enunciado)
	
	# ^z
	#enunciado = re.sub('\^((x|y|z))',' __LATEXEXPXorYorZ ',enunciado)
	if re.search('\^((x|y|z))',enunciado,0):
		features_extra = features_extra + ' __LATEXEXPXorYorZ '
		enunciado = re.sub('\^((x|y|z))',' ',enunciado)

	#enunciado = re.sub('\^(\{(x|y|z)\})',' __LATEXEXPXorYorZ ',enunciado)
	if re.search('\^(\{(x|y|z)\})',enunciado,0):
		features_extra = features_extra + ' __LATEXEXPXorYorZ '
		enunciado = re.sub('\^(\{(x|y|z)\})',' ',enunciado)
	
	# ^s
	#enunciado = re.sub('\^([a-z,A-Z])',' __LATEXEXPSTRANGELETTER ',enunciado)
	if re.search('\^([a-z,A-Z])',enunciado,0):
		features_extra = features_extra + ' __LATEXEXPSTRANGELETTER '
		enunciado = re.sub('\^([a-z,A-Z])',' ',enunciado)
	
	#enunciado = re.sub('\^(\{[a-z,A-Z]\})',' __LATEXEXPSTRANGELETTER ',enunciado)
	if re.search('\^(\{[a-z,A-Z]\})',enunciado,0):
		features_extra = features_extra + ' __LATEXEXPSTRANGELETTER '
		enunciado = re.sub('\^(\{[a-z,A-Z]\})',' ',enunciado)
	
	# ^{a_n}
	#enunciado = re.sub('\^(\{[^\}]\})',' __LATEXEXPOTHER ',enunciado)
	if re.search('\^(\{[^\}]*\})',enunciado,0):
		features_extra = features_extra + ' __LATEXEXPOTHER '
		#enunciado = re.sub('\^(\{[^\}]*\})',' ',enunciado)
	
	# los ^ que queden... No deberian quedar mas, o si?
	enunciado = re.sub('\^',' ',enunciado)
	#enunciado = re.sub('\^',' __LATEXEXP ',enunciado)
	#if re.search('\^',enunciado,0):
		#features_extra = features_extra + ' __LATEXEXP '
		#enunciado = re.sub('\^',' ',enunciado)
	
	
	
	
	
	# h(x)
	enunciado = re.sub('[f,g,h]\((x|y|z)\)',' __LATEXFUNCTIONOFXYZ ',enunciado)
	#if re.search('[f,g,h]\((x|y|z)\)',enunciado,0):
		#features_extra = features_extra + ' __LATEXFUNCTIONOFXYZ '
	
	# h(m)
	enunciado = re.sub('[f,g,h]\((n|m)\)',' __LATEXFUNCTIONOFNM ',enunciado)
	#if re.search('[f,g,h]\((n|m)\)',enunciado,0):
		#features_extra = features_extra + ' __LATEXFUNCTIONOFNM '
	
	# h(1)
	enunciado = re.sub('[f,g,h]\(0|1\)',' __LATEXFUNCTIONONZEROORONE ',enunciado)
	#if re.search('[f,g,h]\(0|1\)',enunciado,0):
		#features_extra = features_extra + ' __LATEXFUNCTIONONZEROORONE '
	
	# 0.5
	enunciado = re.sub('\d+\.\d+',' __FLOAT ',enunciado)
	##if re.search(,enunciado,0):
	#	features_extra = features_extra + 
	
	# 1
	enunciado = re.sub('\d+',' __INTEGER ',enunciado)
	##if re.search(,enunciado,0):
	#	features_extra = features_extra + 
	
	# d_7
	enunciado = re.sub('\{?d\}?_\{?([ ]*((__INTEGER)|([a-z,A-Z]))[ ]*)\}?',' __LATEXPROBABLYDIVISOR ',enunciado)
	#if re.search('\{?d\}?_\{?([ ]*((__INTEGER)|([a-z,A-Z]))[ ]*)\}?',enunciado,0):
		#features_extra = features_extra + ' __LATEXPROBABLYDIVISOR '
	
	# R(z)
	enunciado = re.sub('[P,Q,R]\((x|y|z)\)',' __LATEXPOLYNOMIALOFXYZ ',enunciado)
	#if re.search('[P,Q,R]\((x|y|z)\)',enunciado,0):
		#features_extra = features_extra + ' __LATEXPOLYNOMIALOFXYZ '
	
	# R(m)
	enunciado = re.sub('[P,Q,R]\((n|m)\)',' __LATEXPOLYNOMIALOFNM ',enunciado)
	#if re.search('[P,Q,R]\((n|m)\)',enunciado,0):
		#features_extra = features_extra + ' __LATEXPOLYNOMIALOFNM '
	
	# R(x + y^2) # se puede mejorar para que tenga alcance maximo/minimo/(correcto :P) etc
	enunciado = re.sub('[P,Q,R]\([^\)]+\)',' __LATEXPOLYNOMIALGENERIC ',enunciado)
	#if re.search('[P,Q,R]\([^\)]+\)',enunciado,0):
		#features_extra = features_extra + ' __LATEXPOLYNOMIALGENERIC '
	
	# g(n)
	enunciado = re.sub('[f,g,h]\([ ]*__INTEGER[ ]*\)',' __LATEXFUNCTIONONINTEGER ',enunciado)
	#if re.search('[f,g,h]\([ ]*__INTEGER[ ]*\)',enunciado,0):
		#features_extra = features_extra + ' __LATEXFUNCTIONONINTEGER '
	
	# g(x + y)
	enunciado = re.sub('[f,g,h]\([^\)]+\)',' __LATEXFUNCTIONGENERIC ',enunciado)
	#if re.search('[f,g,h]\([^\)]+\)',enunciado,0):
		#features_extra = features_extra + ' __LATEXFUNCTIONGENERIC '
	
	# b_m // b_5
	enunciado = re.sub('\{?[a-z,A-Z]\}?_\{[^\}]*\}',' __LATEXSEQUENCEELEMENT ',enunciado)
	enunciado = re.sub('\{?[a-z,A-Z]\}?_\{?([ ]*((__INTEGER)|([a-z,A-Z]))[ ]*)\}?',' __LATEXSEQUENCEELEMENT ',enunciado)
	#if re.search('\{?[a-z,A-Z]\}?_\{?([ ]*((__INTEGER)|([a-z,A-Z]))[ ]*)\}?',enunciado,0):
		#features_extra = features_extra + ' __LATEXSEQUENCEELEMENT '
	
	# m \ge 3 # Tiene que venir despues de __INTEGER y antes de \\\\ge y de n m
	enunciado = re.sub('(n|m)[ ]*((\\\\ge)|(\<)|(\<=)|(=\<))[ ]*__INTEGER',' __MorNLEQBOUND ',enunciado)
	#if re.search('(n|m)[ ]*((\\\\ge)|(\<)|(\<=)|(=\<))[ ]*__INTEGER',enunciado,0):
		#features_extra = features_extra + ' __MorNLEQBOUND '
	
	# m \le 3 # Tiene que venir despues de __INTEGER y antes de \\\\ge y de n m
	enunciado = re.sub('(n|m)[ ]*((\\\\le)|(\>)|(\>=)|(=\>))[ ]*__INTEGER',' __MorNGEQBOUND ',enunciado)
	#if re.search('(n|m)[ ]*((\\\\le)|(\>)|(\>=)|(=\>))[ ]*__INTEGER',enunciado,0):
		#features_extra = features_extra + ' __MorNGEQBOUND '
	
	enunciado = re.sub('\{(n|m)\}',' __LATEXINTEGERVAR ',enunciado)
	enunciado = re.sub('\{(x|y|z)\}',' __LATEXNONSPECIFICVAR ',enunciado)
	
	enunciado = re.sub('\$[A-Z][A-Z][A-Z][A-Z][A-Z]\$',' __LATEXPOLYGON ',enunciado)
	#if re.search(,enunciado,0):
	#	features_extra = features_extra + 
	enunciado = re.sub('\$[A-Z][A-Z][A-Z][A-Z]\$',' __LATEXQUADRILATERAL ',enunciado)
	#if re.search(,enunciado,0):
	#	features_extra = features_extra + 
	enunciado = re.sub('\\\\angle[ ]*[A-Z][A-Z][A-Z]',' __LATEXANGLE ',enunciado)
	#if re.search(,enunciado,0):
	#	features_extra = features_extra + 
	enunciado = re.sub('\$[A-Z][A-Z][A-Z]\$',' __LATEXTRIANGLE ',enunciado)
	#if re.search(,enunciado,0):
	#	features_extra = features_extra + 
	enunciado = re.sub('\$[A-Z][A-Z]\$',' __LATEXSEGMENT ',enunciado)
	#if re.search(,enunciado,0):
	#	features_extra = features_extra + 
	enunciado = re.sub('\\Gamma',' __LATEXGAMMA ',enunciado)
	#if re.search(,enunciado,0):
	#	features_extra = features_extra + 
	enunciado = re.sub('\\omega',' __LATEXOMEGA ',enunciado)
	#if re.search(,enunciado,0):
	#	features_extra = features_extra + 
	
	
	
	
	enunciado = re.sub('\\\\lfloor',' __LATEXLFLOOR ',enunciado)
	#if re.search('\\\\lfloor',enunciado,0):
		#features_extra = features_extra + ' __LATEXLFLOOR '
	enunciado = re.sub('\\\\rfloor',' __LATEXRFLOOR ',enunciado)
	#if re.search('\\\\rfloor',enunciado,0):
		#features_extra = features_extra + ' __LATEXRFLOOR '
	enunciado = re.sub('\\\\lceil',' __LATEXLCEIL ',enunciado)
	#if re.search('\\\\lceil',enunciado,0):
		#features_extra = features_extra + ' __LATEXLCEIL '
	enunciado = re.sub('\\\\rceil',' __LATEXRCEIL ',enunciado)
	#if re.search('\\\\rceil',enunciado,0):
		#features_extra = features_extra + ' __LATEXRCEIL '
	
	enunciado = re.sub('\\\\mathbb[ ]*\{?N\}?',' __LATEXNATURALS ',enunciado)
	#if re.search('\\\\mathbb[ ]*\{?N\}?',enunciado,0):
		#features_extra = features_extra + ' __LATEXNATURALS '
	
	enunciado = re.sub('\|\|',' __LATEXPARALELORDIVIDESEXACTLY ',enunciado)
	#if re.search('\|\|',enunciado,0):
		#features_extra = features_extra + ' __LATEXPARALELORDIVIDESEXACTLY '
	enunciado = re.sub('\|',' __LATEXDIVIDESORABSVAL ',enunciado)
	#if re.search('\|',enunciado,0):
		#features_extra = features_extra + ' __LATEXDIVIDESORABSVAL '
	enunciado = re.sub('\\\\bigcup',' __LATEXUNION ',enunciado)
	#if re.search('\\\\bigcup',enunciado,0):
		#features_extra = features_extra + ' __LATEXUNION '
	enunciado = re.sub('\\\\cup',' __LATEXUNION ',enunciado)
	#if re.search('\\\\cup',enunciado,0):
		#features_extra = features_extra +' __LATEXUNION ' 
	enunciado = re.sub('\\\\bigcap',' __LATEXINTERSECTION ',enunciado)
	#if re.search('\\\\bigcap',enunciado,0):
		#features_extra = features_extra + ' __LATEXINTERSECTION '
	enunciado = re.sub('\\\\cap',' __LATEXINTERSECTION ',enunciado)
	#if re.search('\\\\cap',enunciado,0):
		#features_extra = features_extra + ' __LATEXINTERSECTION '
	enunciado = re.sub('\\\\bot',' __LATEXPERPENDICULAR ',enunciado)
	#if re.search('\\\\bot',enunciado,0):
		#features_extra = features_extra + ' __LATEXPERPENDICULAR '
	enunciado = re.sub('\\\\angle',' __LATEXANGLE ',enunciado)
	#if re.search('\\\\angle',enunciado,0):
		#features_extra = features_extra + ' __LATEXANGLE '
	enunciado = re.sub('\\\\hat',' __LATEXANGLE ',enunciado)
	#if re.search('\\\\hat',enunciado,0):
		#features_extra = features_extra + ' __LATEXANGLE '
	enunciado = re.sub('\\\\triangle',' __LATEXTRIANGLE ',enunciado)
	#if re.search('	\\\\triangle',enunciado,0):
		#features_extra = features_extra + ' __LATEXTRIANGLE '
	enunciado = re.sub('\\\\elem',' __LATEXELEM ',enunciado)
	#if re.search('\\\\elem',enunciado,0):
		#features_extra = features_extra + ' __LATEXELEM '
	enunciado = re.sub('\\\\in',' __LATEXIN ',enunciado)
	#if re.search('\\\\in',enunciado,0):
		#features_extra = features_extra + ' __LATEXIN '
	enunciado = re.sub('\\\\ni',' __LATEXNI ',enunciado)
	#if re.search('\\\\ni',enunciado,0):
		#features_extra = features_extra + ' __LATEXNI '
	enunciado = re.sub('\\\\times',' __LATEXTIMES ',enunciado)
	#if re.search('\\\\times',enunciado,0):
		#features_extra = features_extra + ' __LATEXTIMES '
	
	enunciado = re.sub('\\\\begin\{array\}\{[^\}]*\}',' __LATEXARRAY ',enunciado)
	#if re.search('\\\\begin\{array\}\{[^\}]*\}',enunciado,0):
		#features_extra = features_extra + ' __LATEXARRAY '
	
	enunciado = re.sub('\>',' __LATEXG ',enunciado)
	#if re.search('\>',enunciado,0):
		#features_extra = features_extra + ' __LATEXG '
	enunciado = re.sub('\<',' __LATEXL ',enunciado)
	#if re.search('\<',enunciado,0):
		#features_extra = features_extra + ' __LATEXL '
	enunciado = re.sub('=',' __LATEXEQ ',enunciado)
	#if re.search('=',enunciado,0):
		#features_extra = features_extra + ' __LATEXEQ '
	enunciado = re.sub('\-',' __LATEXMINUSORDASH ',enunciado)
	#if re.search('\-',enunciado,0):
		#features_extra = features_extra + ' __LATEXMINUSORDASH '
	enunciado = re.sub('\+',' __LATEXPLUS ',enunciado)
	#if re.search('\+',enunciado,0):
		#features_extra = features_extra + ' __LATEXPLUS '
	enunciado = re.sub('\*',' __LATEXTIMES ',enunciado)
	#if re.search('\*',enunciado,0):
		#features_extra = features_extra + ' __LATEXTIMES '
	enunciado = re.sub('/',' __LATEXDIV ',enunciado)
	#if re.search('/',enunciado,0):
		#features_extra = features_extra + ' __LATEXDIV '
	enunciado = re.sub('\>=',' __LATEXGE ',enunciado)
	#if re.search('\>=',enunciado,0):
		#features_extra = features_extra + ' __LATEXGE '
	enunciado = re.sub('=\<',' __LATEXLE',enunciado)
	#if re.search('=\<',enunciado,0):
		#features_extra = features_extra + ' __LATEXLE'
	enunciado = re.sub('\\\\ge ',' __LATEXGE ',enunciado)
	#if re.search('\\\\ge ',enunciado,0):
		#features_extra = features_extra + ' __LATEXGE '
	enunciado = re.sub('\\\\le ',' __LATEXLE ',enunciado)
	#if re.search('\\\\le ',enunciado,0):
		#features_extra = features_extra + ' __LATEXLE '
	
	enunciado = re.sub('\\\\t',' ',enunciado)
	enunciado = re.sub('\\\\n',' ',enunciado)
	enunciado = re.sub('\[',' ',enunciado)
	enunciado = re.sub('\]',' ',enunciado)
	enunciado = re.sub('\?',' ',enunciado)
	enunciado = re.sub('!',' ',enunciado)
	enunciado = re.sub('"',' ',enunciado)
	              
	enunciado = re.sub('\\\\rightarrow',' __LATEXRIGHTARROW ',enunciado)
	#if re.search('\\\\rightarrow',enunciado,0):
		#features_extra = features_extra + ' __LATEXRIGHTARROW '
	
	# Saco los pesos
	enunciado = re.sub('\$',' ',enunciado)
	enunciado = re.sub('{',' ',enunciado)
	enunciado = re.sub('}',' ',enunciado)

	# ahora saco todos los caracteres que quedan, slvo espacios
	
	#  @$/#.-:&*+=[]?!(){},''"><;%
	enunciado = re.sub('@',' ',enunciado)
	enunciado = re.sub('\$',' ',enunciado)
	enunciado = re.sub('\.',' ',enunciado)
	enunciado = re.sub('/',' ',enunciado)
	enunciado = re.sub('#',' ',enunciado)
	enunciado = re.sub('\-',' ',enunciado)
	enunciado = re.sub(':',' ',enunciado)
	enunciado = re.sub('&',' ',enunciado)
	enunciado = re.sub('\*',' ',enunciado)
	enunciado = re.sub('\+',' ',enunciado)
	enunciado = re.sub('=',' ',enunciado)
	enunciado = re.sub('\[',' ',enunciado)
	enunciado = re.sub('\]',' ',enunciado)
	enunciado = re.sub('\?',' ',enunciado)
	enunciado = re.sub('!',' ',enunciado)
	enunciado = re.sub('\(',' ',enunciado)
	enunciado = re.sub('\)',' ',enunciado)
	enunciado = re.sub('\{',' ',enunciado)
	enunciado = re.sub('\}',' ',enunciado)
	enunciado = re.sub(',',' ',enunciado)
	enunciado = re.sub('\'',' ',enunciado)
	enunciado = re.sub('"',' ',enunciado)
	enunciado = re.sub('\>',' ',enunciado)
	enunciado = re.sub('\<',' ',enunciado)
	enunciado = re.sub(';',' ',enunciado)
	enunciado = re.sub('%',' ',enunciado)
	enunciado = re.sub('\\\\',' ',enunciado)
	
	# appendeo los features extra, como __LATEXFACTORIAL
	enunciado = enunciado + features_extra
	
	# colapso todos los whitespaces a uno solo
	enunciado = re.sub('[ ]+',' ',enunciado)
	
	# Falta tokenizar!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
	
	#g = open('omaforos_enunciados_tokenizados_uno_solo.txt','w')
	#g.write(str(enunciado))
	#g.write('\n')
	enunciado_tokenizado = enunciado.split()
	#g.write(str(enunciado_tokenizado))
	#g.write('\n')
	#g.close()
	
	return enunciado_tokenizado

def doit():
	
	print('Tokenizing enunciados.txt...\n')
	
	f = open('../crawler/enunciados.txt','r')
	g = open('enunciados_tokenizados.txt','w')
	while True:
		line = f.readline()
		if line == "":
			break
		line = line[1: len(line) - 2]
		data = line.split(',',2)
		#g.write(str(data[2]))
		#g.write('\n')
		#console("Este problema tiene " + str(len(data)) + " datos.")
		
		data[2] = tokenize(data[2])
		
		#data[2] = tokenize(data[2])
		data = str(re.sub('[ ]+','',str(data)))
		g.write(str(data))
		g.write('\n')
	g.close()

doit()

#print(str(tokenize("f\\left(x\\right)")))

