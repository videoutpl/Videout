import ast
import parser as p
import pprint
import sys

from src import enviroment


def execute(source, show_ast: bool = False, disable_warnings: bool = True):
    p.disable_warnings = disable_warnings

    try:
        res = p.get_parser().parse(source)
        enviroment.declare_env(ast.symbols)

        for node in res.children:
            node.eval()

        if show_ast:
            print("\n\n" + '=' * 80, ' == Syntax tree ==')

            pp = pprint.PrettyPrinter()
            pp.pprint(res.children)
            pp.pprint(ast.symbols.table())
    except Exception as e:
        print(e.__class__.__name__ + ': ' + str(e), file=sys.stderr)
        if not disable_warnings:
            raise e
