from functools import wraps

def my_decorator(my_func):
    print(f'starting for {my_func.__name__}')
    @wraps(my_func)
    def wrapper(*args, **kwargs):
        kwargs['name'] = "w_" + kwargs['name']
        if not kwargs['name'].startswith('w'):
            print('not allowed')
            return 0
        result = my_func(*args, **kwargs)
        result = result + 4
        return result
    return wrapper

@my_decorator
def tester(name):
    """damit gebe ich die laenge aus"""
    return len(name)

@my_decorator
def test2(name):
    print(f'asdfs{name}')

@my_decorator
def test2(name):
    print(f'asdfs{name}')

namens_laenge = tester(name='bwu')
print(namens_laenge)

namens_laenge = tester(name='wu')
print(namens_laenge)













'asdfsadf'
"asd'fasd'f"


















