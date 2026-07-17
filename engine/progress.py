from collections.abc import Callable


def progress(title: str):
    def decorator(func):
        print(f"{title}...", end="", flush=True)
        func()
        print("成功。")

    return decorator


def retry(maxTimes: int):
    def decorator(func: Callable):
        def wrapper():
            triedTimes = 0
            while triedTimes < maxTimes:
                triedTimes += 1
                try:
                    return func()
                except Exception:
                    continue
            raise ValueError(
                f'"{func.__name__}" retry failed.',
            )

        return wrapper

    return decorator
