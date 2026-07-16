import subprocess
import time

from engine.window import find_windows_by_pid, make_click_through

EXE_PATH = "player/build/windows/parry-click.exe"


def main():
    proc = subprocess.Popen(EXE_PATH)
    pid = proc.pid
    print(f"PID: {pid}")
    for _ in range(30):
        time.sleep(0.2)
        hwnds = find_windows_by_pid(pid)
        if hwnds:
            for hwnd in hwnds:
                make_click_through(hwnd)
            break
    else:
        print("窗口启动失败")
    try:
        proc.wait()
    except KeyboardInterrupt:
        proc.terminate()


if __name__ == "__main__":
    main()
