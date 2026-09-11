import random as r
import time as t
import pyautogui
import keyboard as kb
import textwrap

def main():

    mock = notmain(input('> '))
    print(mock)

    spacetime = 0.25
    enteringchat = '/'
    exitchat = 'enter'
    typespeed = 0.01

    pyautogui.hotkey('alt', 'tab') # uses windows keybinds to put u into ur prev tab (so u must b on windows or configure ur os correctly)
    t.sleep(1)
    kb.press_and_release(enteringchat)
    t.sleep(spacetime)
    pyautogui.typewrite((mock), interval=typespeed)
    t.sleep(spacetime)
    kb.press_and_release(exitchat)


def notmain(message):
    mock = ''
    use_upper = False

    for character in message:
        if not character.isalpha():
            mock += character
            continue

        if use_upper:
            mock += character.upper()
        else:
            mock += character.lower()

        if r.randint(1, 100) <= 90:
            use_upper = not use_upper
    return mock

if __name__ == '__main__':
    art = r"""
      __  __  ___   ____ _  _____ _   _  ____     ____ ___ ____  ____  
     |  \/  |/ _ \ / ___| |/ /_ _| \ | |/ ___|   | __ )_ _|  _ \|  _ \ 
     | |\/| | | | | |   | ' / | ||  \| | |  _    |  _ \| || |_) | | | |
     | |  | | |_| | |___| . \ | || |\  | |_| |   | |_) | ||  _ <| |_| |
     |_|  |_|\___/ \____|_|\_\___|_| \_|\____|___|____/___|_| \_\____/ 
                                            |_____|                    
    """
    print(textwrap.dedent(art))
    while True:
        main()