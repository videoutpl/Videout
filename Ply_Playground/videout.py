import ply.lex as lex
import ply.yacc as yacc
import sys

# Defining list of generic tokens in the language.
# NOTE: Ply's Lexer will use the list named "tokens" to tokenize
# automatically based on the regex rules they have.
tokens = [
    'INT',
    'FLOAT',
    'STRING',
    'KEYWORDS',
    'METHOD',
    'DELIMITERS',
    'ASSIGN'
]

# Defining dictionary of specific reserved words and their token values.
# NOTE: this is done to match all strings and identify keywords afterwards
# using a dictionary mapping.
reserved = {
    'video': 'VIDEO',
    'photo': 'PHOTO'
}

methods = [
    'renderVid',
    'renderGif'
]

# Putting all tokens together.
tokens += reserved.values()

# =================================================================================
# Defining rules for lex to interprete tokens.

# Simple rules.
# NOTE: Ply's lexer maps the regex of anything preceded by "t_"
# to the token that follows it.
t_ASSIGN = r'\='
t_ignore = r' '
t_KEYWORDS = r'\from' #Todo add more keywords
# t_METHOD = r'\renderVid' #TODO add more methods


# Elaborate rules requirirng functions to interpret values.
# NOTE: regex expression MUST be included as method Docstring.

# Match any sequence of digits followed by a point and another series of digits.
def t_FLOAT(t):
    r'\d+\.\d+'
    t.value = float(t.value)
    return t


# Match any sequence of digits.
# NOTE: Ply's lexer will check in order from top of the file to the bottom, so
# any token regexes defined above will be matched before the ones below.
def t_INT(t):
    r'\d+'
    t.value= int(t.value)
    return t


# Match any sequence starting with a letter or underscore,
# followed by letters, underscores, or numbers.
def t_STRING(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'

    # If the string matched is a reserved word, match it to that.
    if t.value in reserved:
        t.type = reserved[t.value]
    elif t.value in methods:
        t.type = 'METHOD'
    else:
        t.type = 'STRING'
    return t


# Handle any unknown characters/tokens.
def t_error(t):
    print('Illegal characters:' + str(t))
    t.lexer.skip(1)

#======================================================================================
# Instantiating the lexer
lexer = lex.lex()

# Passing the lexer a test input.
lexer.input("video renderVid = world 52.254 ")

# Test loop to evaluate the test input.
while True:
    current_token = lexer.token() #current_token is the current token the lexer is looking at.
    if not current_token: # break if it is null/empty
        break
    print(current_token) # If not empty, print it.