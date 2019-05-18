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

# Global dictionary to hold all variables created or modified
env = {}

def p_videout(p): # Starting parser method.
    '''
     videout : var_assign
             | methodcall
             | NUMBER
             | BOOLEAN
             | empty
    '''
    # run(p[1])  # Run the parsed tree received from the parser.


# ====================================================================================================
# Assign Variables.
def p_var_assign(p):

    # This method permits the user assign something to a variable, declared as the lexer params (Init, STRING, etc)
    '''
    var_assign : IDENTIFIER ASSIGN Init
               | IDENTIFIER ASSIGN STRING
               | IDENTIFIER ASSIGN NUMBER
               | IDENTIFIER ASSIGN BOOLEAN
               | IDENTIFIER ASSIGN IDENTIFIER

    '''
    env[p[1]] = p[3]
    p[0] = p[1]


def p_init(p):


    # This method is used to create variables of said params and use them with the rest of the methods.
    '''
    Init : videoInit
         | photoInit
         | concatenateClip
    '''
    p[0]= p[1]

def p_videoInit(p):


    # Method used to create a video clip taken from your file directory. Path must be specified
    # and all 'slashes (/) must be double for the python parser to work and obtain the file.
    #
    # The user specifies the video from path and the run time. You select the start and end time of the clip
    # taken from the original video.
    '''
    videoInit : VIDEO FROM STRING BETWEEN INT COMMA INT AND INT COMMA INT
    '''
    p[0] = videoClip(clip=p[3],start_time=(p[5],p[7]),end_time=(p[9],p[11]),fps=23.98)


def p_photoInit(p):


    # Method used to create a photo clip from a picture on directory. Path must be specified
    # and all 'slashes (/) must be double for the python parser to work and obtain the file.
    #
    # The user specifies the picture from path and the run time (amount of time the picture will be on screen)
    '''
    photoInit : PHOTO FROM STRING LASTING INT
    '''

    p[0] = photoClip(image=p[3], duration=p[5])

def p_concatenateClip(p):


    # Method used to create a concatenated clip from clips or pics (identifiers/variables) already created
    # on the system. The method will concatenate the first identifier with the second by creating a new
    # identifier/variable.
    '''
    concatenateClip : CONCATENATE_CLIP IDENTIFIER AND IDENTIFIER
    '''
    final_out = finalVideo()
    final_out.concatenate_clip(env[p[2]])
    final_out.concatenate_clip(env[p[4]])
    p[0] = final_out


# =========================================================================================================
# Method Calls
def p_methodcall(p):  # Define all method calls
    '''
    methodcall : resizemethod
               | addTextmethod
               | renderVideo
               | renderGif
               | cropmethod
               | addAudiomethod
               | addExtractedAudiomethod
               | showVarmethod
               | showAllVarsmethod

    '''  # TODO add more method calls and implementations.
    p[0] = p[1]

def p_showVarmethod(p):

    # Stat method to show he value of a identifier/variable on system.
    """
    showVarmethod : IDENTIFIER

    """
    print(env[p[1]])
def p_showAllVarsmethod(p):

    # Stat method to show all stored variables and identifiers on the system at the moment.
    """
    showAllVarsmethod : SHOW_VARS

    """
    print(env)
def p_resizemethod(p):  # Create resize tree.


    # Method to resize/scale a clip on a identifier/variable by a given number. The resized clip will
    # be permanently changed.

    '''
    resizemethod : RESIZE IDENTIFIER BY NUMBER
    '''
    final_out = env[p[2]]
    final_out.resize(new_size=p[4])


def p_cropmethod(p):


    # Method to crop a clip by given aspect_ratios. These ratios are declared as strings and
    # will automatically be executed on call, as per the appropriate ratios defined beforehand.
    # The cropped clip will be permanently changed.

    '''
    cropmethod : CROP IDENTIFIER BY ASPECT_RATIO
    '''
    final_out = env[p[2]]
    final_out.crop(aspectRatio=p[4])

def p_addAudiomethod(p):


    # Method to add overlay audio to a clip. If the clip already has audio, it will be overwritten.
    #
    # Path must be specified and all 'slashes (/) must be double for the python parser
    # to work and obtain the file.
    #
    # The user specifies the path as a string and the time the audio will run (start and end time)
    # taken from the original audio file.
    '''
    addAudiomethod : ADD_AUDIO STRING TO IDENTIFIER BETWEEN NUMBER COMMA NUMBER
    '''
    final_out = env[p[4]]
    final_out.addAudioFromFile(audio=p[2],start_time=p[6],end_time=p[8])
    # p[0] = (p[1],p[2],('var',p[4]t), p[6],p[8])
def p_addExtractedAudiomethod(p):


    # Method to add overlay audio to a clip. If the clip already has audio, it will be overwritten.
    #
    # The user specifies the audio to extract as a variable/identifier and then the
    # clip to add the extracted audio as another variable/identifier, the time the audio will run (start and end time)
    # taken from the original audio file.
    '''
    addExtractedAudiomethod : EXTRACT_AUDIO IDENTIFIER TO IDENTIFIER BETWEEN NUMBER COMMA NUMBER

    '''
    final_out = env[p[4]]
    final_out.addAudioFromClip(clipToExtract=p[2], start_time=p[6], end_time=p[8])

def p_addTextmethod(p): # Adds the wanted text to the video or photo


    # Method to add text to a clip specified by a string on a position given by the user.
    # The position is defined as a string and will be applied automatically on call, as per
    # the appropriate ratios defined beforehand.
    '''
    addTextmethod : ADD_TEXT STRING TO IDENTIFIER TO POSITION
    '''
    final_out = env[p[4]]
    final_out.add_text(text=p[2], font_size=30, color='black',
                       font='Amiri-Bold', interline=-10, posString=p[6], duration=final_out.duration)


def p_renderVideo(p):  # Create renderVid tree.


    # Method to ultimately render a video. The user writes the renderVid call and the variable
    # to be rendered. Said video will be created and stored on source directory.
    '''
    renderVideo : RENDER_VIDEO IDENTIFIER
    '''

    final_out = env[p[2]]
    final_out.writeVideo("rendered.mp4")
    # p[0] = (p[1], ('var', p[2]))

def p_renderGif(p): # Create renderGif tree


    # Method to ultimately render a gif. The user writes the renderGif call and the variable
    # to be rendered. Said gif will be created and stored on source directory.
    '''
    renderGif : RENDER_GIF IDENTIFIER
    '''
    final_out = env[p[2]]
    final_out.create_gif("renderedGif.gif")

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



# ==========================================================================================================
# Instantiate parser.
parser = yacc.yacc()


# ===========================================================================================================
# Perpetual reading from the console
while True:
    try:
        input_string = input('>>')
    except EOFError:  # If you click Ctrl+D, stop reading from console.
        break
    parser.parse(input_string)