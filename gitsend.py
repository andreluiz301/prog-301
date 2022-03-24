from ast import Return
import pyautogui as py
import time, os


print('\nOlá! O programa está começando!')
time.sleep(0.5)
print('...')
time.sleep(0.5)
print('...')
time.sleep(0.5)
print('...')

pasta = input('Digite o nome do diretório que deseja acessar: ')
obs = input('Digite a observação que deseja colocar no commit: ')
nav = input('Digite o nome do seu navegador: ')

a = 15
aa = 17

time.sleep(1)               
py.hotkey('ctrl', 'alt', 't')
time.sleep(5)
py.write(f'cd {pasta}')
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
if nav == 'opera' or 'Opera' or 'opera gx' or 'Opera gx' or 'Opera Gx' or \
            'Opera GX' or 'Operagx' or 'OperaGx' or 'OperaGX':
    py.write(f'start opera https://github.com/')
elif nav == 'google' or 'chrome' or 'google chrome' or 'Google' or 'Chrome' \
            or 'Google Chrome':
    py.write(f'start chrome https://github.com/')
time.sleep(0.5)
py.press('enter')
time.sleep(10)
if pasta == 'prog-301':
    for a in range(a):
        py.press('tab')
elif pasta == 'aulas-prog':
    for aa in range(aa):
        py.press('tab')
time.sleep(0.5)
py.press('enter')