import argparse

def get_args():
    parser = argparse.ArgumentParser(description='Bottles of beer song',formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-n','--num',metavar='number',type=int,default=10,help='How many bottles')
    args = parser.parse_args()
    if args.num < 1:
        parser.error(f'--num "{args.num}" must be greater than 0')
    return args

def employee_check(work_hours):
    current_max = 0
    employee_of_month = ''
    for emp,hrs in work_hours:
        if hrs > current_max:
            current_max = hrs
            employee_of_month = emp
        else:
            pass
    return (employee_of_month,current_max)


def main():
    print('Tuple unpacking')

    stock_prices = [('APPL',200),('GOOG',400),('MSFT',100)]
    for i in stock_prices:
        print(i)
    for t,p in stock_prices:
        print(p + (0.1*p))

    work_hours = [('FelipeRod',40),('Carolina',60),('Manchitas',1)]
    t = employee_check(work_hours)
    n,h = employee_check(work_hours)
    print(t)
    print("{}:{}".format(n,h))

if __name__ == '__main__':
    main()