import win32gui
import win32con
import win32process


def find_windows_by_pid(pid):
    result = []

    def callback(hwnd, extra):
        if win32gui.IsWindowVisible(hwnd):
            _, found_pid = win32process.GetWindowThreadProcessId(hwnd)
            if found_pid == pid:
                result.append(hwnd)

    win32gui.EnumWindows(callback, None)
    return result


def make_click_through(hwnd):
    ex_style = win32gui.GetWindowLong(hwnd, win32con.GWL_EXSTYLE)
    new_style = ex_style | 0x00080000 | 0x00000020
    win32gui.SetWindowLong(hwnd, win32con.GWL_EXSTYLE, new_style)
    win32gui.SetLayeredWindowAttributes(hwnd, 0, 255, 0x00000002)
