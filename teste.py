import pyautogui as py
import time, os


class Aplicativo(object):

    def push(self):

        rep = input('Digite o nome do repositório que deseja acessar: ')
        arq = input('Digite o arquivo ou pasta que deseja enviar: ')
        msg = input('Digite a mensagem que deseja colocar no commit: ')
        nav = input('Digite o nome do seu navegador: ')

        py.hotkey('ctrl', 'alt', 't')
        time.sleep(5)
        py.write(f'cd {rep}')
        time.sleep(0.5)
        py.press('enter')
        py.write(f'git add {arq}')
        time.sleep(0.5)
        py.press('enter')
        time.sleep(1)
        py.write(f'git commit -m {time.strftime(f""" "{msg} (%d/%m/%Y %H:%M:%S)" """, time.localtime())}')
        time.sleep(0.5)
        py.press('enter')
        time.sleep(3)
        py.write('git push')
        time.sleep(0.5)
        py.press('enter')
        time.sleep(5)
        py.write(f'start {nav} https://github.com/')
        time.sleep(0.5)
        py.press('enter')


if __name__ == "__main__":
    app = Aplicativo()
    app.push()