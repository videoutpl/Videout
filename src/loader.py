import lexer


while True:
    text = input('bitch> ')
    result , error = lexer.run('<stdin>',text)

    if error : print(error.as_string())
    elif result: print(result)
