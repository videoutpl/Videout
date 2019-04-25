import ply.lex as lex
import ply.yacc as yacc
import sys

# Defining list of tokens in the language
tokens = [

    'INT',
    'FLOAT',
    'STRING',
    'KEYWORDS',
    'INITIALIZATION',
    'METHOD',
    'DELIMITERS',
    'ASSIGN'
]



# Defining rules for lex to interprete tokens.

# Simple rules.
t_ASSIGN = r'\=='
t_ignore = r' '


# Elaborate rules requirirng functions to interpret
# values.

def t_FLOAT(t):
    r'\d+\.\d+'
    t.value = float(t.value)
    return t

def t_INT(t):
    r'\d+'
    t.value= int(t.value)
    return t



def t_STRING(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = 'STRING'
    return t

def t_error(t):
    print('Illegal characters:' + str(t))
    t.lexer.skip(1)


# Instantiating the lexer
lexer = lex.lex()

# Passing the lexer a test input.
lexer.input("Hello world 52.254 ")


# Test loop to evaluate the test input.
while True:
    current_token = lexer.token() #current_token is the current token the lexer is looking at.
    if not current_token: # break if it is null/empty
        break
    print(current_token) # If not empty, print it.