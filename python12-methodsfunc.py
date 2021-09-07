import argparse

def get_args():
    parser = argparse.ArgumentParser(description='Bottles of beer song',formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-n','--num',metavar='number',type=int,default=10,help='How many bottles')
    args = parser.parse_args()
    if args.num < 1:
        parser.error(f'--num "{args.num}" must be greater than 0')
    return args

def main():
    print('Methods Functions Documentation')
    mylist = [1,2,3]
    
    #help(mylist)

    '''
    hello - multiline comments
    '''
    say_hello()
    say_hello('felipe')
    print(add_num(1,2))
    print(even_check(3))
    print(check_even_list([1,9,9,55,3,1,89]))

#def say_hello():
#    print("hello")

def say_hello(name='default name'):
    print(f"hello {name}")

def add_num(n1,n2):
    return n1+n2

def even_check(n):
    return (n%2==0)

def check_even_list(num_list):
    for n in num_list:
        if n%2 == 0:
            return True
        else:
            pass
    return False
    

if __name__ == '__main__':
    main()