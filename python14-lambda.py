import argparse
name = 'Global String'
x= 50

def get_args():
    parser = argparse.ArgumentParser(description='Bottles of beer song',formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-n','--num',metavar='number',type=int,default=10,help='How many bottles')
    args = parser.parse_args()
    if args.num < 1:
        parser.error(f'--num "{args.num}" must be greater than 0')
    return args

def square(num):
    return num**2

def greet():
    name = 'FelipeRod'
    global x 
    print(f'X is {x}')
    def hello():
        print(f"Hello {name}")
    hello()
    x= 'new value'
    print(f'Now X is {x}')

def splicer(mystring):
    if len(mystring)%2 == 0:
        return 'EVEN'
    else:
        return mystring[0]

def check_even(n):
    return n%2 == 0

def printer():
    x=50
    return x

def main():
    print('Lambda, Filter')
    my_nums = [1,2,3,4,5,6]
    for i in map(square,my_nums):
        print(i)
    l = list(map(square,my_nums))
    print(l)
    names = ['Felipe','Carolina','Manchitas']
    print(list(map(splicer,names)))

    print(list(filter(check_even,my_nums)))
    print(list(map(lambda n: n**2,my_nums)))
    print(list(filter(lambda i: i%2 == 0,my_nums)))
    print(list(map(lambda x:x[0],names)))
    print(list(map(lambda x:x[::-1],names)))

    
    print(25)
    print(printer())

    print(name)
    greet()
    print(name)

    print(x)


if __name__ == '__main__':
    main()