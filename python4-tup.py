import argparse

def get_args():
    parser = argparse.ArgumentParser(description='Bottles of beer song',formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-n','--num',metavar='number',type=int,default=10,help='How many bottles')
    args = parser.parse_args()
    if args.num < 1:
        parser.error(f'--num "{args.num}" must be greater than 0')
    return args

def main():
    print('Tuples')
    t = (1,2,3)
    l = [1,2,3]
    print(type(t))
    print(type(l))
    print(t[0])
    print(t[-1])

    t = (1,2,3,2)
    print(len(t)) #4
    print(t.count(2)) #2
    print(t.index(3)) #2

    t[0] = 4 #Error immutability

    tt = tuple()

if __name__ == '__main__':
    main()