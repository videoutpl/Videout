import ply.lex as lex
reserved = {
'if': 'IF',
'else': 'ELSE',

'for': 'FOR',
'in': 'IN',
'while': 'WHILE',
'exit': 'EXIT',

'fn': 'FUNCTION',
'ret': 'RETURN',

'var': 'VAR',

'resize':'RESIZE',
'addTxt':'addText',
'renderVid':'renderVID',
'renderGif':'renderGIF',

'say': 'PRINT',

'and': 'AND',
'or': 'OR',
'not': 'NOT',

}

tokens = ['KEYWORDS','INT','FLOAT','MINUS',
          'PLUS', 'DIV','MULT','EQUALS','SETTO',
          'LPAREN','RPAREN','IDENTIFIER','STRING'
] + list(reserved.values())

t_PLUS = r'\+'
t_MINUS = r'\-'
t_DIV = r'/'
t_MULT = r'\*'
t_SETTO = r'\=='
t_EQUALS = r'\='
t_LPAREN = r'\('
t_RPAREN = r'\)'

def t_NEWLINE(t):
    r'\n'
    t.lexer.lineno += 1
    t.lexer.linepos = 0
    pass

def t_IDENTIFIER(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, t.type)

    return t
def t_NUM_FLOAT(t):
    r'\d*\.\d+'
    t.value = float(t.value)
    return t
def t_NUM_INT(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_STRING(t):
    r'"(?:\\"|.)*?"'
    t.value = bytes(t.value.lstrip('"').rstrip('"'), "utf-8").decode("unicode_escape")
    return t

def t_error(t):
    raise exceptions.UnexpectedCharacter("Unexpected character '%s' at line %d" % (t.value[0], t.lineno))


lexer = lex.lex()
