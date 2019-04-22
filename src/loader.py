import lexer

while True:
    text = input('--> ')
>>>>>>> 2594524b64dbdb57d567e21d4d099ea170c43dcc
    result , error = lexer.run('<stdin>',text)

    if error : print(error.as_string())
    elif result: print(result)
