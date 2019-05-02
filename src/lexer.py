import ply.lex as lex

# Defining list of generic tokens in the language.
# NOTE: Ply's Lexer will use the list named "tokens" to tokenize
# automatically based on the regex rules they have.

#TODO: Add more tokens as necessary

tokens = [
    'INT',
    'FLOAT',
    'IDENTIFIER',
    'STRING',
    'ASSIGN',
    'LPAREN',
    'RPAREN',
    'ASPECT_RATIO',
    'COMMA',
    'KEYWORD',
    'METHOD',
    'DELIMITERS'
]

#TODO: Add more reserved words as necessary

# Defining dictionary of specific reserved words and their token values.
# NOTE: this is done to match all strings and identify keywords afterwards
# using a dictionary mapping.
reserved = {
    'video'         : 'VIDEO',
    'photo'         : 'PHOTO',
    'resize'        : 'RESIZE',
    'trim'          : 'TRIM',
    'renderVid'     : 'RENDERVIDEO',
    'renderGif'     : 'RENDERGIF',
    'to'            : 'TO',
    'by'            : 'BY',
    'from'          : 'FROM',
    'lasting'       : 'LASTING',
    'and'           : 'AND',
    'between'       : 'BETWEEN',
    'position'      : 'POSITION',
    'addText'       : "ADDTEXT",
    'addAudio'      : 'ADDAUDIO',
    'crop'          : 'CROP',
    'extractAudio'  : 'EXTRACTAUDIO'
}

tokens += reserved.values()
# =================================================================================
# Defining rules for lex to interpret tokens.

# Simple rules.
# NOTE: Ply's lexer maps the regex of anything preceded by "t_"
# to the token that follows it.
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


def t_ASPECT_RATIO(t):
    r'vertical|phone|square|letterbox|widescreen|cinemascope|anamorphic|DCI|Digital IMAX'
    return t


def t_POSITION(t):
    r'top|left|bottom|right|center|top-left|top-right|bottom-left|bottom-right|top-center|bottom-center'
    return t

#TODO: Either modify definition or add a new on to influde Filepaths
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
