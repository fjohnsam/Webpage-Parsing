
#Copyright: Febin John Sam (fjohnsam96@gmail.com)

###TASK1

import urllib.request, urllib.error, urllib.parse
import os
import http.client as http

http.HTTPConnection._http_vsn = 10
http.HTTPConnection._http_vsn_str = 'HTTP/1.0'



###TASK2

import ply.lex as lex
import ply.yacc as yacc

#TOKENS

tokens= [
	"AUTHORS"
	,"AUTHORE"
	,"TITLES"
	,"TITLEE"
	,"TYPES"
	,"TYPEE"
	,"VENUES"
	,"VENUEE"
	,"YEARS"
	,"YEARE"
	,"TEXT"
	]

t_AUTHORS = r'<title>dblp:'

t_AUTHORE = r'</title>'

t_TITLES = r'<span\ class\=\"title\"\ itemprop\=\"name\">'

t_TITLEE = r'</span>'

t_TYPES = r'<div\ class\=\"nr\"\ id\=\"'

t_TYPEE = r'\">'

t_VENUES = r'<span\ itemprop\=\"name\">'

t_VENUEE = r'</span></span>'

t_YEARS = r'<li\ class\=\"year\">'

t_YEARE = r'</li>'

t_TEXT = r'[a-zA-Z0-9()-/:.& ]+'

def t_error(t) :
	t.lexer.skip(1)

lexer = lex.lex()

# GRAMMAR

database=[]

def p_author(p):
	'''s : AUTHORS TEXT AUTHORE'''
	global profname
	profname = p[2]

def p_title(p):
	'''s : TITLES TEXT TITLEE'''
	global ptitle
	ptitle = p[2]

def p_type(p):
	'''s : TYPES TEXT TYPEE'''
	pp=p[2]
	global ptype
	ptype = pp[0]

def p_venue(p):
	'''s : VENUES TEXT VENUEE'''
	global pvenue
	pvenue = p[2]
	database.append([profname,ptitle,ptype,pvenue,pyear])
	print(database[len(database)-1])

def p_year(p):
	'''s : YEARS TEXT YEARE'''
	global pyear
	pyear = p[2]
	
def p_error(p):
	print("",end="")

parser = yacc.yacc()

#PROBLEM IMPLEMENTATION

ip=['f','j','k','u',0]

def clean(c):
	for index in range(len(c)):
		if(c[index].isdigit() or c[index].isalpha() or c[index]==" "):
			continue
		else:
			c = c.replace(c[index]," ")
	c=c.replace(" ","")
	return c.upper()

def main():

	print("Saving profile pages")

	fileno = 0
	f = open("professors.txt","r")
	while(((url = f.readLine()) != null) && !("".equals(line))):
		fileno +=1
		response = urllib.request.urlopen(url)
		webcontent = response.read()
		filename = str(fileno)+'.html'
		fp = open(filename, 'wb')
		fp.write(webcontent)
		fp.close
		print(filename,"saved")
	

	print("Processing files")

	prev=0
	no=0

	for index in range(fileno):
		no+=1
		filename=str(no)+'.html'
		f = open(filename,'r')
		data=f.read()
		f.close()
		parser.parse(data)
		length=len(database)
		print(filename.replace(".html","")," --> ",len(database)-prev,"publications")
		prev=len(database)

	while True:
		print("")
		ip[0]=input("--->Enter Profile name =>   ")
		ip[1]=input("--->Enter Title of paper =>   ")
		ip[2]=input("--->Enter Type of publication =>   ")
		ip[3]=input("--->Enter Venue of paper =>   ")
		ip[4]=input("--->Enter Year of publication  =>   ")
		print("")

		present = 0

		for index in range(len(database)):
			if((clean(database[index][0])==clean(ip[0])) or (ip[0].replace(" ","")=='')):
				if((clean(database[index][1])==clean(ip[1])) or(ip[1].replace(" ","")=='')):
					if((clean(database[index][2])==clean(ip[2])) or (ip[2].replace(" ","")=='')):
						if((clean(database[index][3])==clean(ip[3])) or (ip[3].replace(" ","")=='')):
							if((clean(database[index][4])==clean(ip[4])) or (ip[4].replace(" ","")=='')):
								present = 1
								print(database[index][0],",",database[index][1],",",database[index][2],",",database[index][3],",",database[index][4])
		if(present==0):
			print('No search result found')

if __name__ == "__main__":
	main()
