import pyautogui as py
import time, os


time.sleep(1)
py.hotkey('ctrl', 'alt', 't')
time.sleep(5)
py.write('cd prog-301')
time.sleep(0.5)
py.press('enter')
time.sleep(0.5)
py.write('git add *')
time.sleep(0.5)
py.press('enter')
time.sleep(1)
py.write(f'git commit -m {time.strftime(""" "Teste (%d/%m/%Y %H:%M:%S)" """, time.localtime())}')
time.sleep(0.5)
py.press('enter')
time.sleep(5)
py.write('git push')
time.sleep(0.5)
py.press('enter')
