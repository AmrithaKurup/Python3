def new_decorator(original_func):

    def wrap_func():
        print('before the function')
        original_func()
        print('after the function')

    return wrap_func


@new_decorator
def func_needs_decorator():
    print('I want to be decorated!')


func_needs_decorator()
