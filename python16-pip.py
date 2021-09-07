import argparse

#>pip install requests
#>pip install colorama

from colorama import Fore

def get_args():
    parser = argparse.ArgumentParser(description='Bottles of beer song',formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-n','--num',metavar='number',type=int,default=10,help='How many bottles')
    args = parser.parse_args()
    if args.num < 1:
        parser.error(f'--num "{args.num}" must be greater than 0')
    return args

def main():
    print('pip')
    print(Fore.RED + "some RED text")
    print(Fore.GREEN + "some RED text")

if __name__ == '__main__':
    main()