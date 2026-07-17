import ctypes
import ctypes.wintypes
import time
import random

user32 = ctypes.windll.user32


def shake(duration=1000, intensity=10):
    windows = []

    def enum_callback(hwnd, extra):
        if user32.IsWindowVisible(hwnd):
            rect = ctypes.wintypes.RECT()
            user32.GetWindowRect(hwnd, ctypes.byref(rect))
            windows.append(
                (
                    hwnd,
                    rect.left,
                    rect.top,
                    rect.right - rect.left,
                    rect.bottom - rect.top,
                )
            )
        return True

    EnumWindowsProc = ctypes.WINFUNCTYPE(ctypes.c_bool, ctypes.c_int, ctypes.c_int)
    user32.EnumWindows(EnumWindowsProc(enum_callback), 0)
    start = time.time()
    while time.time() - start < duration / 1000:
        dx = random.randint(-intensity, intensity)
        dy = random.randint(-intensity, intensity)
        for hwnd, x, y, w, h in windows:
            user32.SetWindowPos(hwnd, 0, x + dx, y + dy, 0, 0, 0x0001)
        time.sleep(0.016)
    for hwnd, x, y, w, h in windows:
        user32.SetWindowPos(hwnd, 0, x, y, 0, 0, 0x0001)
