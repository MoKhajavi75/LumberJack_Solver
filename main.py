# LumberJack Solver by MohamadKh75
# 2017-04-09
# ********************

import pyautogui
import time
import keyboard


print("Press 'Esc' anytime to quit!\n")
# give you time to start game and set browser!
time.sleep(3)

# take screenshot and detect the color of determined pixel!
pixel = pyautogui.screenshot()
person_color = pixel.getpixel((958, 334))
left_color = pixel.getpixel((955, 313))
right_color = pixel.getpixel((1083, 313))

# set the needed colors!
tree_color = (161, 116, 56)
back_color = (211, 247, 255)

print("Let's Go!\n")

while True:

    # provide the needed delay! Python is absolutely faster than the game so...
    time.sleep(0.11)

    # take screenshot again!
    pixel = pyautogui.screenshot()
    person_color = pixel.getpixel((958, 334))
    left_color = pixel.getpixel((955, 313))
    right_color = pixel.getpixel((1083, 313))

    # if the person is at the LEFT side, so:
    if person_color == (51, 93, 101):
        if left_color == back_color:
            pyautogui.click(987, 606)
            pyautogui.click(987, 606)

        elif left_color == tree_color:
            pyautogui.click(1057, 606)
            pyautogui.click(1057, 606)

    # and if he's at the RIGHT side:
    else:
        if right_color == back_color:
            pyautogui.click(1057, 606)
            pyautogui.click(1057, 606)

        elif right_color == tree_color:
            pyautogui.click(987, 606)
            pyautogui.click(987, 606)

    # how to exit from the program!
    state = keyboard.is_pressed('esc')
    if state == 1:
        exit()
