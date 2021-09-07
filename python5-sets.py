import argparse

def get_args():
    parser = argparse.ArgumentParser(description='Bottles of beer song',formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-n','--num',metavar='number',type=int,default=10,help='How many bottles')
    args = parser.parse_args()
    if args.num < 1:
        parser.error(f'--num "{args.num}" must be greater than 0')
    return args

def main():
    print('Sets')
    myset = set()
    myset.add(1)
    myset.add(2)
    print(myset)

    mylist = [1,1,1,1,1,2,2,2,2,2,3,3,3,3,3,4]
    myset = set(mylist)
    print(myset) #{1, 2, 3, 4}
    print(myset.pop())
    print(myset)

    b= None

if __name__ == '__main__':
    main()