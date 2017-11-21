def test(func):
    def new_func(*args, **kwargs):
        print('start')
        func(*args, **kwargs)
        print('end')

    return new_func


@test
def spam():
    print('Eggs!!!')

spam()
