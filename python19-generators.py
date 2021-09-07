import argparse

def get_args():
    parser = argparse.ArgumentParser(description='Bottles of beer song',formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-n','--num',metavar='number',type=int,default=10,help='How many bottles')
    args = parser.parse_args()
    if args.num < 1:
        parser.error(f'--num "{args.num}" must be greater than 0')
    return args

def fibonacci1(n):
    a=1
    b=1
    output = list([0])
    for i in range(n):
        output.append(a)
        a,b = b,a+b
    return output

def simple_gen():
    for x in range(3):
        #print(x)
        yield x

def create_cubes(n):
    for x in range(n):
        yield x**3


def main():
    print('Decorator')
    print(fibonacci1(10))
    for i in simple_gen():
        print(i)
    g = simple_gen()
    print(g)
    print(next(g))
    print(next(g))
    print(next(g))
    try:
       print(next(g)) #Error
    except:
       pass

    s= 'hello'
    s_iter = iter(s)
    print(next(s_iter))
    print(next(s_iter))


    for i in create_cubes(10):
        print(i)

if __name__ == '__main__':
    main()