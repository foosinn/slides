from functools import wraps

runners = []

def my_decorator(f):
    print(f'wrapping {f.__name__}')

    @wraps(f)
    def wrapper(*args, **kwargs):
        return f(*args, **kwargs)
    return wrapper

def run_always(f):
    runners.append(f)
    return f

@my_decorator
def tester():
    print('doing something')

@run_always
def call_on_run():
    print('hello')

def main():
    for f in runners:
        f()

if __name__ == "__main__":
    main()
