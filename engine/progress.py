def progress(title: str):
    def decorator(func):
        print(f"{title}...", end="", flush=True)
        func()
        print("成功。")

    return decorator
