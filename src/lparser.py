from animations.ClipClasses import *
from src.lexer import tokens

from ply import yacc

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
             | NUMBER
             | BOOLEAN
             | empty
    '''
    run(p[1])  # Run the parsed tree received from the parser.


# ====================================================================================================
# Assign Variables.
def p_var_assign(p):
    '''
    var_assign : IDENTIFIER ASSIGN Init
               | IDENTIFIER ASSIGN STRING
               | IDENTIFIER ASSIGN NUMBER
               | IDENTIFIER ASSIGN BOOLEAN
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
               | addTextmethod
               | renderVideo
               | renderGif
               | cropmethod
               | addAudiomethod

    '''  # TODO add more method calls and implementations.
    p[0] = p[1]


def p_resizemethod(p):  # Create resize tree.
    '''
    resizemethod : RESIZE IDENTIFIER BY NUMBER
    '''
    p[0] = (p[1], ('var', p[2]), p[4])


def p_trimmethod(p):  # TODO Doesn't currently exist in BaseClip methods.
    '''
    trimmethod : TRIM IDENTIFIER FROM NUMBER COMMA NUMBER TO NUMBER COMMA NUMBER
    '''
    p[0] = (p[1], ('var', p[2]), p[4], p[6], p[8], p[10])

def p_cropmethod(p):
    '''
    cropmethod : CROP IDENTIFIER BY ASPECT_RATIO
    '''
    p[0] = (p[1], ('var',p[2]), p[4])

def p_addAudiomethod(p):
    '''
    addAudiomethod : ADD_AUDIO STRING TO IDENTIFIER BETWEEN NUMBER COMMA NUMBER
    '''
    p[0] = (p[1],p[2],('var',p[4]), p[6],p[8])

def p_addTextmethod(p): # Adds the wanted text to the video or photo
    '''
    addTextmethod : ADD_TEXT STRING TO IDENTIFIER TO POSITION
    '''
    p[0] = (p[1], p[2], ('var',p[3]), p[5])

def p_renderVideo(p):  # Create renderVid tree.
    '''
    renderVideo : RENDER_VIDEO IDENTIFIER
    '''
    p[0] = (p[1], ('var', p[2]))

def p_renderGif(p): # Create renderGif tree
    '''
    renderGif : RENDER_GIF FROM IDENTIFIER
    '''
    p[0] = (p[1],('var',p[3]))

# =========================================================================================================
# Miscellaneous methods.

def p_BOOLEAN(p):
    '''
    BOOLEAN : BOOL
    '''
    p[0] = p[1]

def p_NUMBER(p):
    '''
    NUMBER : INT
           | FLOAT
    '''
    p[0] = p[1]


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

        #TODO: Add the methods for the tress of the other methods

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