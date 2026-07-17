import subprocess
import time
from engine.window import find, click_through
from engine.network import NetworkBackend
from engine.progress import progress, retry
from engine.config import config

backend = NetworkBackend()
process = subprocess.Popen(
    "player/build/windows/parry-click.exe",
    stdout=None if config.allow_stdout else subprocess.DEVNULL,
    stderr=None if config.allow_stdout else subprocess.DEVNULL,
)
pid = process.pid


@progress(f"特效场景正在启动，PID={pid}，正在获取窗口句柄")
@retry(config.hwnd_max_retry)
def make_through():
    time.sleep(0.5)
    hwnds = find(pid)
    if len(hwnds) > 0:
        for hwnd in hwnds:
            click_through(hwnd)
    else:
        raise


@progress("正在连接场景API")
@retry(5)
def ping():
    backend.send("ping")
    for message in backend.wait_message(timeout=1):
        print("message")
        if message == "pong":
            break


try:
    process.wait()
except KeyboardInterrupt:
    process.terminate()
