import argparse

def get_args():
    parser = argparse.ArgumentParser(description='Bottles of beer song',formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-n','--num',metavar='number',type=int,default=10,help='How many bottles')
    args = parser.parse_args()
    if args.num < 1:
        parser.error(f'--num "{args.num}" must be greater than 0')
    return args

def main():
    print('For')
    mylist = [1,2,3,4,5,6,7,8,9,10]
    for i in mylist:
        print(i)
    for i in mylist:
        if i%2 == 0:
            print(i)
        else:
            print(f'-->{i}')
    x = 0
    for i in mylist:
        x += i
    print(x)

    mystring = 'Hello World'
    for letter in mystring:
        print(letter)

    for _ in 'FelipeRod':
        print(_)

    t = tuple([1,2,3,4])
    for item in t:
        print(item)

    mylist = [(1,2),(2,3),(4,5),(6,7)]
    for item in mylist:
        print(item)

    for (a,b) in mylist:
        print(f"({a},{b})")

    mylist = [(1,2,3),(2,3,4),(4,5,6),(6,7,8)]  #,(5,5)] Error
    for a,b,c in mylist:
        print(f'{a}/{b}/{c}')

    d = {'k1':1,'k2':2,'k3':3}
    for item in d:
        print(item)

    for item in d.items():
        print(item)

    for k,v in d.items():
        print(f"{k}:{v}")

    for v in d.values():
        print(v)

    for k in d.keys():
        print(k) 
    


if __name__ == '__main__':
    main()