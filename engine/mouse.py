from pynput import mouse
from collections.abc import Callable


def on_click(func: Callable):
    listener = mouse.Listener(on_click=func)
    listener.start()
    return listener
