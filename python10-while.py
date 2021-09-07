import argparse
from random import shuffle
from random import randint

def get_args():
    parser = argparse.ArgumentParser(description='Bottles of beer song',formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-n','--num',metavar='number',type=int,default=10,help='How many bottles')
    args = parser.parse_args()
    if args.num < 1:
        parser.error(f'--num "{args.num}" must be greater than 0')
    return args

def main():
    print('While')
    x=0
    while x<5:
        print(f'{x}')
        x+=1
    x=0
    while x<5:
        print(f'{x}')
        x+=1
    else:
        print(f'no less than {x}')
    
    x = [1,2,3]
    for i in x:
        pass

    mystring = 'FelipeRod'
    for l in mystring:
        if l == 'e':
            continue
        print(l)
    
    mystring = 'FelipeRod'
    for l in mystring:
        if l == 'e':
            break
        print(l)
    
    for n in range(11):
        print(n)
    for n in range(3,11):
        print(n)
    for n in range(0,11,2):
        print(n)

    print(list(range(0,11,2)))

    word = 'abcde'
    for item in enumerate(word):
        print(item)

    for indx,letter in enumerate(word):
        print(indx)
        print(letter)
    
    mylist1 = [1,2,3]
    mylist2 = ['a','b','c']
    mylist3 = [100,200,300]
    for item in zip(mylist1,mylist2):
        print(item)

    for item in zip(mylist1,mylist2,mylist3):
        print(item)
    
    print('x' in ['x',2,3])
    print('x' in [1,2,3])
    print('a' in 'a world')

    print('k1' in {'k2':2, 'k1':3})
    d= {'k1':345}
    print(345 in d.values())

    mylist = [10,20,30,1,40,100,101]
    print(min(mylist))
    print(max(mylist))
    shuffle(mylist)
    print(mylist)
    print(randint(0,100))

    result = input('Enter a number here:')
    print(result)
    print(int(result))

if __name__ == '__main__':
    main()