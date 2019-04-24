import ply.lex as lex

# List of token names
tokens = (
    'INT',
    'FLOAT',
    'IDENTIFIER',
    'STRING',
    'ASSIGN',
    'LPAREN',
    'RPAREN',
    'ASPECT_RATIO',
    'COMMA',
    'RESIZE',
    'CROP',
    'TRIM',
    'KEYWORD',
    'EXTRACT_AUDIO',
    'ADD_AUDIO',
    'ADD_TEXT',
    'POSITION',
    'RENDER_GIF',
    'RENDER_VID'
)

# Regular expresion rules for simple tokens
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_COMMA = ','
t_ASSIGN = '='

# A string containing ignored characters (spaces and tabs)
t_ignore = ' \t'


# Rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


def t_FLOAT(t):
    r'\d*\.\d+'
    t.value = float(t.value)
    return t


def t_INT(t):
    r'\d+'
    t.value = int(t.value)
    return t


def t_RESIZE(t):
    r'resize'
    return t


def t_CROP(t):
    r'crop'
    return t


def t_EXTRACT_AUDIO(t):
    r'extractAudio'
    return t


def t_ADD_AUDIO(t):
    r'addAudio'
    return t


def t_ADD_TEXT(t):
    r'addText'
    return t


def t_TRIM(t):
    r'trim'
    return t


def t_RENDER_GIF(t):
    r'renderGif'
    return t


def t_RENDER_VID(t):
    r'renderVid'
    return t


def t_KEYWORD(t):
    r'from|to|by|between|and|at'
    return t


def t_ASPECT_RATIO(t):
    r'vertical|phone|square|letterbox|widescreen|cinemascope|anamorphic|DCI|Digital IMAX'
    return t


def t_POSITION(t):
    r'top|left|bottom|right|center|top-left|top-right|bottom-left|bottom-right|top-center|bottom-center'
    return t


def t_STRING(t):
    r'"(?:\\"|.)*?"'
    t.value = bytes(t.value.lstrip('"').rstrip('"'), "utf-8").decode("unicode_escape")
    return t


def t_IDENTIFIER(t):
    r'\w+'
    t.value = str(t.value)
    # t.type = reserved.get(t.value, t.type)
    return t


# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


lexer = lex.lex()
#
# Test it out
data = 'resize clip by 0.6 ' \
       'crop clip to cinemascope ' \
       'Clip1 = video from "test.mp4" between 2, 30 and 2, 45 ' \
       'trim clip from 1, 30 to 2, 50 ' \
       'Music = extractAudio from "test2.mp4" between 0, 10 and 0, 45 ' \
       'addAudio Music to Clip1 ' \
       'addText "Text" between 4, 50 and 5, 0 at center ' \
       'renderGif Clip1 ' \
       'renderVid Clip1'

# Give the lexer some input
lexer.input(data)

for tok in lexer:
    print(tok)
