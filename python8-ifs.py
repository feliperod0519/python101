import argparse

def get_args():
    parser = argparse.ArgumentParser(description='Bottles of beer song',formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-n','--num',metavar='number',type=int,default=10,help='How many bottles')
    args = parser.parse_args()
    if args.num < 1:
        parser.error(f'--num "{args.num}" must be greater than 0')
    return args

def main():
    print('If')
    hungry = False
    if hungry:
        print("feed me!")
    else:
        print("No I'm good")
    loc= 'Bank'
    if loc == 'Auto Shop':
        print('Cars')
    elif loc == 'Bank':
        print('$$$!')
    else:
        print("I don't know much")   
        

if __name__ == '__main__':
    main()