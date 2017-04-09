# LumberJack Solver by MohamadKh75
# 2017-04-09
# Main source by Owatch from StackOverFlow - Edited by MohamadKh75
# ********************

from ctypes import windll, Structure, c_ulong, byref


class POINT(Structure):
    _fields_ = [("x", c_ulong), ("y", c_ulong)]


def queryMousePosition():
    pt = POINT()
    windll.user32.GetCursorPos(byref(pt))
    return {"x": pt.x, "y": pt.y}


pos = queryMousePosition()

# Make it live!
while True:
    old = pos
    pos = queryMousePosition()

    if pos != old:
        print(pos)
