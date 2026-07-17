import subprocess
import time
import random
import math
from engine.window import find, click_through
from engine.network import NetworkBackend
from engine.progress import progress, retry
from engine.config import config
from engine import mouse

backend = NetworkBackend()
process = subprocess.Popen(
    "player/build/windows/parry-click.exe",
    stdout=None if config.allow_stdout else subprocess.DEVNULL,
    stderr=None if config.allow_stdout else subprocess.DEVNULL,
    stdin=subprocess.DEVNULL,
)
pid = process.pid


@progress(f"特效场景已启动，PID={pid}，正在初始化")
@retry(config.hwnd_max_retry)
def make_through():
    time.sleep(0.5)
    hwnds = find(pid)
    if len(hwnds) > 0:
        for hwnd in hwnds:
            click_through(hwnd)
    else:
        raise


@progress("正在连接播放器API")
@retry(5)
def ping():
    backend.send("ping")
    for message in backend.wait_message(timeout=1):
        if message == "pong":
            break


@mouse.on_click
def click_listener(x, y, btn, pressed):
    if pressed:
        backend.send(
            ",".join(  # 位置，角度，大小
                str(item)
                for item in [
                    "play",
                    x,
                    y,
                    random.random() * 2 * math.pi,
                    random.uniform(0.8, 1.2),
                ]
            )
        )


try:
    process.wait()
except KeyboardInterrupt:
    process.terminate()
