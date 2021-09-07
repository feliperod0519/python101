import argparse

def get_args():
    parser = argparse.ArgumentParser(description='Bottles of beer song',formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-n','--num',metavar='number',type=int,default=10,help='How many bottles')
    args = parser.parse_args()
    if args.num < 1:
        parser.error(f'--num "{args.num}" must be greater than 0')
    return args

def main():
    print('List Comprehension')
    mystring = 'HelloWorld'
    mylist = [l for l in mystring]
    print(mylist)

    mylist = [x for x in range(0,11)]
    print(mylist)

    mylist = [x**2 for x in range(0,11)]
    print(mylist)

    mylist = [x for x in range(0,11) if x%2 == 0]
    print(mylist)

    celcius = [0,10,20,34.5]
    fahrenheit = [((9/5)*temp+32)for temp in celcius]
    print(fahrenheit)

    results = [x if x%2 == 0 else 'odd' for x in range(0,11)]
    print(results)

    results = [x if x%2 == 0 else 0 for x in range(0,11)]
    print(results)

    mylist = []
    for x in [2,4,6]:
        for y in [100,200,300]:
            mylist.append(x*y)
    print(mylist)

    mylist = [x*y for x in [2,4,6] for y in [1,10,100]]
    print(mylist)

if __name__ == '__main__':
    main()