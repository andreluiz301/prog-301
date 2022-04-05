import pyautogui as py


while True:
    try:
        a = input('Digite a conta: ')
        print(f'Resultado: {eval(a)}\n----------------------')

    except(SyntaxError, TypeError, NameError, EOFError):
        print('\nInformação inválida!\n----------------------')
        py.press('up')