from win32api import GetKeyState, mouse_event
from time import sleep

PLUS = 15
MINUS = -15
CODE = 0x58

def SLEEP(timing=0.001):
    sleep(timing)

def MSEVENT(plusPXL, minusPXL):
    mouse_event(0x01, plusPXL, minusPXL)
    
def SQUARE():
    while True:
        if GetKeyState(CODE) < 0:
            MSEVENT(PLUS, 0)
            MSEVENT(PLUS, 0)
            SLEEP()
            
            MSEVENT(0, MINUS)
            MSEVENT(0, MINUS)
            SLEEP()
            
            MSEVENT(MINUS, 0)
            MSEVENT(MINUS, 0)
            SLEEP()
            
            MSEVENT(0, PLUS)
            MSEVENT(0, PLUS)
        else:
            continue

if __name__ == "__main__":
    print("Для выхода нажми CTRL + C\nИли просто закрой это окно =)")
    SQUARE()
