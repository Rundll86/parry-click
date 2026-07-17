import subprocess
import time
from engine.window import find_windows_by_pid, make_click_through
from engine.network import NetworkBackend
from engine.progress import progress
from engine.config import config

backend = NetworkBackend()
process = subprocess.Popen(
    "player/build/windows/parry-click.exe",
    stdout=None if config.allow_stdout else subprocess.DEVNULL,
    stderr=None if config.allow_stdout else subprocess.DEVNULL,
)
pid = process.pid


@progress(f"特效场景正在启动，PID={pid}，正在获取窗口句柄")
def make_through():
    for _ in range(config.hwnd_max_retry):
        time.sleep(0.5)
        hwnds = find_windows_by_pid(pid)
        if hwnds:
            for hwnd in hwnds:
                make_click_through(hwnd)
            break
    else:
        print("窗口启动失败。")
        process.wait()


@progress("正在连接场景API")
def ping():
    backend.send("ping")
    for message in backend.wait_message():
        if message == "pong":
            break


try:
    process.wait()
except KeyboardInterrupt:
    process.terminate()
