import subprocess
import time
from engine.window import find_windows_by_pid, make_click_through

process = subprocess.Popen("player/build/windows/parry-click.exe")
pid = process.pid

print(f"特效场景正在启动，PID={pid}。")
print("正在获取窗口句柄...")
for _ in range(30):
    time.sleep(0.5)
    hwnds = find_windows_by_pid(pid)
    if hwnds:
        for hwnd in hwnds:
            make_click_through(hwnd)
        break
else:
    print("窗口启动失败。")
    process.wait()
print("场景启动成功。")

try:
    process.wait()
except KeyboardInterrupt:
    process.terminate()
