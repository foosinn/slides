
from contextlib import contextmanager

class asdf:

    def __enter__(self):
       print('before')

    def __exit__(self,type, value, traceback):
           print('after')


with asdf():
    print("hello")

