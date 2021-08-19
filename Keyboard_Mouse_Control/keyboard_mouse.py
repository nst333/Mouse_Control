import pyautogui
import keyboard
import time

PosX, PosY = pyautogui.position()
key = 1

while True:
    PosX, PosY = pyautogui.position()
    if keyboard.is_pressed('w'): #up
        pyautogui.moveTo(PosX, PosY+-50, 0.1)
    if keyboard.is_pressed('s'): #down
        pyautogui.moveTo(PosX, PosY+50, 0.1)
    if keyboard.is_pressed('a'): #left
        pyautogui.moveTo(PosX+-50, PosY, 0.1)
    if keyboard.is_pressed('d'): #right
        pyautogui.moveTo(PosX+50, PosY, 0.1)

    if keyboard.is_pressed('control'):
        if keyboard.is_pressed('w'): #up
            pyautogui.moveTo(PosX, PosY+-10, 0.1)
        if keyboard.is_pressed('s'): #down
            pyautogui.moveTo(PosX, PosY+10, 0.1)
        if keyboard.is_pressed('a'): #left
            pyautogui.moveTo(PosX+-10, PosY, 0.1)
        if keyboard.is_pressed('d'): #right
            pyautogui.moveTo(PosX+10, PosY, 0.1)
                
    if keyboard.is_pressed('shift'):
        if keyboard.is_pressed('w'): #up
            pyautogui.moveTo(PosX, PosY+-5, 0.1)
        if keyboard.is_pressed('s'): #down
            pyautogui.moveTo(PosX, PosY+5, 0.1)
        if keyboard.is_pressed('a'): #left
            pyautogui.moveTo(PosX+-5, PosY, 0.1)
        if keyboard.is_pressed('d'): #right
            pyautogui.moveTo(PosX+5, PosY, 0.1)
        
    if keyboard.is_pressed('c'):
        pyautogui.click()
    if keyboard.is_pressed('r'):
        pyautogui.rightClick()
    if keyboard.is_pressed('u'):
        pyautogui.scroll(50)
    if keyboard.is_pressed('f'):
        pyautogui.scroll(-50)
            
