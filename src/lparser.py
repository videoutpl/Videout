import ply.yacc as yacc
import ast
from animations import BaseClip, ClipClasses as vclip
import os
from src.lexer import *

precedence = (
    ('left', 'NOT'),
    ('left', 'PLUS', 'MINUS'),
    ('left', 'MUL', 'DIV'),
)

def p_statement_list(p):
    '''
    statement_list : statement
                   | statement_list statement
    '''
    if len(p) == 2:
        p[0] = ast.InstructionList([p[1]])
    else:
        p[1].children.append(p[2])
        p[0] = p[1]

def p_statement(p):
    '''
    statement : identifier
              | expression
              | if_statement
    '''
    p[0] = p[1]

def p_primitive(p):
    '''
    primitive : NUM_INT
              | NUM_FLOAT
              | STRING
    '''
    if isinstance(p[1], ast.BaseExpression):
        p[0] = p[1]
    else:
        p[0] = ast.Primitive(p[1])

def p_boolean_operators(p):
    '''
    boolean : expression EQUALS expression
    '''
    p[0] = ast.BinaryOperation(p[1], p[3], p[2])

def p_assignable(p):
    '''
    assignable : primitive
               | expression
    '''
    p[0] = p[1]

def p_assign(p):
    '''
    expression : identifier SETTO assignable
    '''
    p[0] = ast.Assignment(p[1], p[3])

def p_ifstatement(p):
    '''
    if_statement : IF expression LPAREN statement_list RPAREN
    '''
    p[0] = ast.If(p[2], p[4])

def p_ifstatement_else_if(p):
    '''
    if_statement : IF expression LPAREN statement_list RPAREN ELSE if_statement
    '''
    p[0] = ast.If(p[2], p[4], p[7])

def p_in_expressions(p):
    '''
    expression : expression IN exprew
    '''

def p_create_video(p):

    clip = os.getenv('USERPROFILE') + '\\Videos\\llama_transformation.mp4'
    vclip.videoClip(clip=clip, start_time=(0, 1), end_time=(0, 60), fps=23.98)
    vclip.writeVideo(filename=('Test.mp4'))
    vclip.create_gif(filename="testgif.gif")
