from contextlib import contextmanager


@contextmanager
def wrapper():
    print('before')
    yield
    print('after')

with wrapper():
    print("hello")
