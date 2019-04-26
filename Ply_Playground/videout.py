import ply.lex as lex
import ply.yacc as yacc
from animations.ClipClasses import *
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
    'ASSIGN',
    'COMMA'
]
# TODO: Add more tokens as necessary.

# Defining dictionary of specific reserved words and their token values.
# NOTE: this is done to match all strings and identify keywords afterwards
# using a dictionary mapping.

reserved = {
    'video'     : 'VIDEO',
    'photo'     : 'PHOTO',
    'resize'    : 'RESIZE',
    'trim'      : 'TRIM',
    'renderVid' : 'RENDERVIDEO',
    'renderGif' : 'RENDERGIF',
    'to'        : 'TO',
    'by'        : 'BY',
    'from'      : 'FROM',
    'lasting'   : 'LASTING',
    'and'       : 'AND',
    'between'   : 'BETWEEN'
}
# TODO: Add more reserved words and tokens as necessary.

# Putting all tokens together.
tokens += reserved.values()

# =================================================================================
# Defining rules for lex to interpret tokens.

# Simple rules.
# NOTE: Ply's lexer maps the regex of anything preceded by "t_"
# to the token that follows it.
t_ASSIGN = r'\='
t_ignore = r' '
t_COMMA = r'\,'


# Elaborate rules requiring functions to interpret values.
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
    r'[a-zA-Z_][a-zA-Z_0-9.]*'  #TODO: Either moddify this definition or add a new one to include Filepaths.
    if t.value in reserved:  # If the string matched is a reserved word, match it to that.
        t.type = reserved[t.value]
    else:
        t.type = 'STRING'
    return t


# Handle any unknown characters/tokens.
def t_error(t):
    print('Illegal characters:' + str(t))
    t.lexer.skip(1)


# Instantiating the lexer
lexer = lex.lex()

# ======================================================================================
# Defining parser methods

# NOTE: language grammar rules must be written as the docstring for these methods.
# The 'p' parameter is a python tuple, interpreted as a tree.

# NOTE: p[0] represents the non-terminal on the left of the colon ":"
# p[1->n] are the terminals/non-terminals to the right of the colon.
# these can have multiple values specified between "or"s "|".
# The idea is to pass up predicable tuples with predictable values inside them up to p_videout.

# NOTE: will cause errors trying to build parser if grammar contains terminals/non-terminals
# that have not yet been implemented.
# =================================================================================================


# =================================================================================================
# Main parse method.
def p_videout(p): # Starting parser method.
    '''
     videout : var_assign
             | methodcall
             | empty
    '''
    run(p[1])  # Run the parsed tree received from the parser.


# ====================================================================================================
# Assign Variables.
def p_var_assign(p):
    '''
    var_assign : STRING ASSIGN Init
               | STRING ASSIGN STRING
    '''
    if type(p[3]) is tuple: # If p[3] is a tuple, it is a Init tree.
        p[0] = (p[2], p[1], p[3])
    else:
        p[0] = (p[2], p[1], ('var', p[3])) # If it's not a tuple, it's a variable, so assign it a variable tree.

# Initializations
def p_init(p):
    '''
    Init : videoInit
         | photoInit
    '''
    p[0]= p[1]

def p_videoInit(p):
    '''
    videoInit : VIDEO FROM STRING BETWEEN INT COMMA INT AND INT COMMA INT
    '''
    p[0] = (p[1], p[3], p[5], p[7], p[9], p[11])

def p_photoInit(p):
    '''
    photoInit : PHOTO FROM STRING LASTING INT
    '''
    p[0] = (p[1], p[3], p[5])


# =========================================================================================================
# Method Calls
def p_methodcall(p):  # Define all method calls
    '''
    methodcall : resizemethod
               | trimmethod
               | renderVideo

    '''  # TODO add more method calls and implementations.
    p[0] = p[1]


def p_resizemethod(p):  # Create resize tree.
    '''
    resizemethod : RESIZE STRING BY INT
                 | RESIZE STRING BY FLOAT
    '''
    p[0] = (p[1], ('var', p[2]), p[4])


def p_trimmethod(p):  # TODO Doesn't currently exist in BaseClip methods.
    '''
    trimmethod : TRIM STRING FROM INT COMMA INT TO INT COMMA INT
    '''
    p[0] = (p[1], ('var', p[2]), p[4], p[6], p[8], p[10])


def p_renderVideo(p):  # Create renderVid tree.
    '''
    renderVideo : RENDERVIDEO STRING
    '''
    p[0] = (p[1], ('var', p[2]))

# =========================================================================================================
# Miscellaneous methods.


def p_empty(p):  # Define what an emtpy terminal is.
    '''
    empty :
    '''
    p[0] = None


def p_error(p):  # Print generic syntax error.
    print("Syntax error found!")


# ==========================================================================================================
# Instantiate parser.
parser = yacc.yacc()

env = {}  # Global dictionary to hold all variables created or modified within the run method.


# ==========================================================================================================
# Define the run method.
def run(p):  # This method essentially traverses the tuple trees created by parser and executes them.
    global env

    print(p)  # Print for debugging.

    # If what the run method is getting is a tuple, evaluate it's contents.
    if type(p) is tuple:  # If it is a tuple, check the first item in the tuple to determine what to do.

        if p[0] == '=':   # Handle variable assignment.
            env[p[1]] = run(p[2])
        elif p[0] == 'var':  # Handle variable retrieval.
            if p[1] not in env:
                return "Undeclared variable found!"
            else:
                return env[p[1]]

        elif p[0] == 'video': # Handle videoClip object instantiation.
            return videoClip(clip=p[1], start_time=(p[2], p[3]), end_time=(p[4], p[5]))

        elif p[0] == 'renderVid':  # Handle rendering variable to video file.
            final_out = run(p[1])  # Retrieve the variable from the env dictionary.
            final_out.writeVideo("renderedVideo.mp4")  # TODO: Make this filename dynamic from method call

    else:  # If the parameter is not a tuple, simply return it.
        return p


# ===========================================================================================================
# Perpetual reading from the console
while True:
    try:
        input_string = input('>>')
    except EOFError:  # If you click Ctrl+D, stop reading from console.
        break
    parser.parse(input_string)