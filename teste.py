import pyautogui as py
import time, os


class Aplicativo(object):

    def push(self):

        rep = input('\nDigite o nome do repositório que deseja acessar: ')
        arq = input('Digite o arquivo ou pasta que deseja enviar: ')
        msg = input('Digite a mensagem que deseja colocar no commit: ')
        nav = input('Digite o nome do seu navegador: ')

        py.hotkey('ctrl', 'alt', 't')
        time.sleep(5)
        py.write(f'cd {rep}')
        time.sleep(1)
        py.press('enter')
        py.write(f'git add {arq}')
        time.sleep(1)
        py.press('enter')
        time.sleep(1)
        py.write(f'git commit -m {time.strftime(f""" "{msg} (%d/%m/%Y %H:%M:%S)" """, time.localtime())}')
        time.sleep(1)
        py.press('enter')
        time.sleep(3)
        py.write('git push')
        time.sleep(1)
        py.press('enter')
        time.sleep(5)
        py.write(f'start {nav} https://github.com/')
        time.sleep(1)
        py.press('enter')


    def pull(self):

        rep = input('\nDigite o nome do repositório que deseja acessar: ')

        py.hotkey('ctrl', 'alt', 't')
        time.sleep(5)
        py.write(f'cd {rep}')
        time.sleep(1)
        py.press('enter')
        time.sleep(1)
        py.write('git pull')
        time.sleep(1)
        py.press('enter')

    
    def exibir_menu(self):

        print('--------- MENU ---------')
        print('|                      |')
        print('|       1 - Push       |')
        print('|       2 - Pull       |')
        print('|       0 - Sair       |')
        print('|                      |')
        print('------------------------')


    def menu(self):

        while True:
            self.exibir_menu()
            try:
                n = int(input('O que deseja fazer: '))
                if n == 1:
                    self.push()
                elif n == 2:
                    self.pull()
                elif n == 0:
                    print('Saindo...')
                    sair = True
                    break
                else:
                    print('Insira uma opção válida')
            except(ValueError):
                print("Insira uma opção válida!")

if __name__ == "__main__":
    app = Aplicativo()
    app.menu()
    