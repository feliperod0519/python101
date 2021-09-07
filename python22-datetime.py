import argparse
from datetime import datetime
from datetime import date

def get_args():
    parser = argparse.ArgumentParser(description='Bottles of beer song',formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-n','--num',metavar='number',type=int,default=10,help='How many bottles')
    args = parser.parse_args()
    if args.num < 1:
        parser.error(f'--num "{args.num}" must be greater than 0')
    return args

def main():
    print('Files')
   
    '''
    mytime = datetime.time(2,20)
    print(mytime)
    mytime = datetime.time(13,20,1,20)
    print(mytime)
    today = datetime.date.today()
    print(today)
    print(today.ctime())
    mydt = datetime(2021,10,3,14,20,1)
    mydt.replace(year=2020)
    print(mydt)
    '''

    d1 = date(2021,11,3)
    d2 = date(2020,5,21)
    d = d1 - d2
    print(d)

if __name__ == '__main__':
    main()