import argparse

def get_args():
    parser = argparse.ArgumentParser(description='Bottles of beer song',formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-n','--num',metavar='number',type=int,default=10,help='How many bottles')
    args = parser.parse_args()
    if args.num < 1:
        parser.error(f'--num "{args.num}" must be greater than 0')
    return args

def main():
    print('Op Comparison')
    print('hello'=='bye')
    print('Bye'=='bye')
    print(2.0==2)
    print(1<2<3) #T
    print(1<2>3) #F
    print(1<2 and 2<3) #T
    print(1<2 and 2>3) #F
    print(not 1==1) #F
    print(not 400 > 5000) #T


if __name__ == '__main__':
    main()