#!/usr/bin/env python2.7

#this code has been created with the appropriate modification and complete modification of code from https://github.com/stefanbehr/cky .
import re

class CNFGrammar:
    
    def __init__(self, path):
        
        self.lexical = {}  
        self.phrasal = {}  
        self.start = None 

        with open(path) as grammar_file:
            grammar_text = grammar_file.read()

        grammar_text = grammar_text.strip()
        grammar_lines = grammar_text.split("\n")

        production = r"""^(\w+)\s*->\s*(\w+\s+\w+|'\S+'|"\S+")$"""
        quoted = r"""^"\S+"|'\S+'$"""
        PRODUCTION = re.compile(production)
        QUOTED = re.compile(quoted)

        for line in grammar_lines:
            prod_match = PRODUCTION.match(line)
            if prod_match:
                lhs, rhs = prod_match.group(1), prod_match.group(2)
                if not self.start:
                    self.start = lhs
                quot_match = QUOTED.match(rhs)
                if quot_match:
                    prod_type = "lexical"
                else:
                    prod_type = "phrasal"
                    rhs = rhs.split()
                rule_map = getattr(self, prod_type)
                if lhs not in rule_map:
                    rule_map[lhs] = []
                rule_map[lhs].append(rhs)

    def lhs_for_rhs(self, rhs, structure_type):
        
        nonterminals = []
        productions = getattr(self, structure_type)
        for lhs in productions:
            if rhs in productions[lhs]:
                nonterminals.append(lhs)
        #print rhs
        #print nonterminals
        return nonterminals

class Node:
    
    def __init__(self, symbol, left=None, right=None, terminal=None):
        
        self.symbol = symbol
        self.left = left
        self.right = right
        self.terminal = terminal

    def __str__(self):
        
        return """({0} -> {1} {2})""".format(self.symbol, str(self.left), str(self.right))

class CKYParser:
    
    def __init__(self, path):
        
        self.grammar = CNFGrammar(path)

    def parse(self, sentence):
        
        N = len(sentence)

        # initializes (N+1)x(N+1) matrix to None.
        self.chart = [(N+1)*[None] for row_label in xrange(N+1)]
        for j in xrange(1, N+1):
            token = sentence[j-1]
            self.chart[j-1][j] = map(lambda preterm: Node(preterm, terminal=token), self.grammar.lhs_for_rhs(token, "lexical"))
            for i in reversed(xrange(0, j-1)): 
                for k in xrange(i+1, j):       
                    left = self.chart[i][k]  
                    right = self.chart[k][j]  
                    
                    if left and right:
                        for lnode in left:
                            lsymbol = lnode.symbol
                            for rnode in right:
                                rsymbol = rnode.symbol
                                
                                msymbols = self.grammar.lhs_for_rhs([lsymbol, rsymbol], "phrasal")
                                if msymbols and self.chart[i][j] is None:
                                    self.chart[i][j] = []
                                for msymbol in msymbols:
                                    self.chart[i][j].append(Node(msymbol, lnode, rnode))
                    

    def parse_to_string(self, node):
        
        if node.left and node.right:
            inside = "{0} {1}".format(self.parse_to_string(node.left), self.parse_to_string(node.right))
        else:
            inside = "{0}".format(node.terminal)
        return "({0} {1})".format(node.symbol, inside)

    def get_parses(self, sentence):
        
        self.parse(sentence)
        N = len(sentence)
        parse_roots = self.chart[0][N]
        result = []
        if parse_roots: # guard against None
            for root in parse_roots:
                if root.symbol == self.grammar.start:
                    result.append(self.parse_to_string(root))  
        return result
