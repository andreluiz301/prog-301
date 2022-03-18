from ast import Return
import pyautogui as py
import time, os


diretorio = input('Digite o nome do diretório que deseja acessar: ')
obs = input('Digite a observação que deseja colocar no commit: ')
nav = input('Digite o primeiro nome do seu navegador: ')

a = 15

time.sleep(1)
py.hotkey('ctrl', 'alt', 't')
time.sleep(5)
py.write(f'cd {diretorio}')
time.sleep(0.5)
py.press('enter')
time.sleep(0.5)
py.write('git add *')
time.sleep(0.5)
py.press('enter')
time.sleep(1)
py.write(f'git commit -m {time.strftime(f""" "{obs} (%d/%m/%Y %H:%M:%S)" """, time.localtime())}')
time.sleep(0.5)
py.press('enter')
time.sleep(5)
py.write('git push')
time.sleep(0.5)
py.press('enter')
time.sleep(6)
py.write(f'start {nav} https://github.com/')
time.sleep(0.5)
py.press('enter')
time.sleep(20)
for a in range(a):
    py.press('tab')
time.sleep(0.5)
py.press('enter')