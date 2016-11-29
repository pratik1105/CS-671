#!/usr/bin/env python2.7

#this code has been created with the appropriate modification and complete understanding of code from https://github.com/stefanbehr/cky .
import re
def print_tree(parse):
    
    string = parse[0]
    open_paren = 1
    depth = 1
    index = 1
    
    while open_paren > 0 and index < len(parse):
        if not re.match(r"'", parse[index]):
            string += '\n' + '  ' * depth + parse[index]
            open_paren += 1
            depth = open_paren
        else:
            string += ' ' + re.sub("'", "", parse[index])
            open_paren -= close_paren(parse[index])
            depth = open_paren
            
        index += 1
                
    return string

def close_paren(string):
    num = 0
    index = -1
    
    while string[index] == ')':
        num += 1
        index -= 1

    return num

if __name__ == "__main__":
	import nltk, sys
	from parser import CKYParser
	
        
	try:
		sentence_path = sys.argv[1]
	except IndexError:
		exit("Please give a path to a file of sentences.")

	try:
		grammar_path = sys.argv[2]
	except IndexError:
		exit("Please give a path to a file with a grammar.")

	with open(sentence_path) as sentence_file:
		sentence_data = sentence_file.read()

	sentences = sentence_data.strip().split("\n")
	sentences = [nltk.wordpunct_tokenize(sentence) for sentence in sentences]
        
        parser = CKYParser(grammar_path)
        

	
	for sentence in sentences:
	    sentence = ["'{0}'".format(token) for token in sentence]	# make sure tokens are single-quoted
	    parses = parser.get_parses(sentence)
		
            output = ''
    
            for parse in parses:
                parse = parse.split()
                output += print_tree(parse)
                output += '\n\n'
        
            sys.stdout.write(output)
	    
            
