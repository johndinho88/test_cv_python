import pyautogui

import time

pyautogui.PAUSE = 0.5 

pyautogui.press ("win")
pyautogui.write("chrome")
pyautogui.press("enter")

link = "https://circuitodavisao.com/auth/login"
pyautogui.write(link)
pyautogui.press("enter")

time.sleep(3)

#pyautogui.click(x=803, y=506)
#pyautogui.write("johnanderson88@outlook.com.br")

#pyautogui.press("tab")
#pyautogui.write("john2405")                            
pyautogui.click(x=945, y=719)       
time.sleep(10)
#selecionar heat    
pyautogui.click(x=567, y=501)
time.sleep(3)       

#clicar em lançar arregimentação
pyautogui.click(x=483, y=457)
time.sleep(5)

pyautogui.click(x=1273, y=586)
pyautogui.press("tab")
time.sleep(4)

pyautogui.click(x=1372, y=586)
pyautogui.press("tab")
time.sleep(4)   

pyautogui.click(x=1475, y=583)
pyautogui.press("tab")
pyautogui.press("tab")

pyautogui.click(x=1258, y=656)
pyautogui.press("tab")
time.sleep(4)

pyautogui.click(x=1368, y=658)
pyautogui.press("tab")
time.sleep(4)

pyautogui.click(x=1482, y=660)
pyautogui.press("tab")
time.sleep(4)   