import argparse

def get_args():
    parser = argparse.ArgumentParser(description='Bottles of beer song',formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-n','--num',metavar='number',type=int,default=10,help='How many bottles')
    args = parser.parse_args()
    if args.num < 1:
        parser.error(f'--num "{args.num}" must be greater than 0')
    return args

#def hello():
#    return 'Hello'

def hello(name='Felipe'):
    print("hello")

    def greet():
        return '\t greet in hello'
    
    def welcome():
        return '\t welcome in hello'

    print('Return a function')
    if name == 'Felipe':
        return greet
    else:
        return welcome

def cool():
    def super_cool():
        return 'Very cool!'
    return super_cool

def hello2():
    return 'Hello Felipe'

def other(some_func):
    print('Other code runs here')
    print(some_func())

def new_decorator(original_function):
    def wrap_function():
        print('Some extra code BEFORE the injection')
        original_function()
        print('Some extra code AFTER the injection')
    return wrap_function

@new_decorator
def a_function_that_needs_decorator():
    print('I need to be decorated')


def main():
    print('Decorator')
    my_new_func = hello('Felipe')
    print(my_new_func)
    print(my_new_func())

    f = cool()
    print(f())

    other(hello2)

    a_function_that_needs_decorator()
    
    #decorated_func = new_decorator(a_function_that_needs_decorator)
    #decorated_func()

    a_function_that_needs_decorator()


    '''
    print(hello())
    greet = hello
    print(greet())
    try:
        del hello
    except:
        pass
    else:
        greet()
    '''

if __name__ == '__main__':
    main()