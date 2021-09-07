import argparse

def get_args():
    parser = argparse.ArgumentParser(description='Bottles of beer song',formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-n','--num',metavar='number',type=int,default=10,help='How many bottles')
    args = parser.parse_args()
    if args.num < 1:
        parser.error(f'--num "{args.num}" must be greater than 0')
    return args

def main():
    #args = get_args()
    #dynamic typing
    print('Dynamic typing')
    my_dogs =2
    my_dogs = ["Chester","Manchitas"]
    print(type(my_dogs))
    #strings
    print("I'm running here")
    print('hello \n world \t kkp')
    print(len('hello'))

    mystring = "Hello World"
    print(mystring[0])
    print(mystring[-2])

    mystring = 'abcdefghijk'
    print(mystring[2:])
    print(mystring[:3])
    print(mystring[3:6])
    print(mystring[::])
    print(mystring[::2])
    print(mystring[::-1])

    #immutability
    name = "Sam"
    #name[0] = 'P' #Error

    print(name[1:])
    print('P' + name[1:])

    x = 'Hello World'
    print(x + " it's beautiful outside")

    letter = 'z'
    letter = letter * 100
    print(letter)

    x = "Hello World"
    print(x.upper().split())
    print(x.upper().split('E'))
    print(x.upper().split('O'))

    #.format() and f-strings
    print('This is a string {}'.format('INSERTED'))
    print('The {} {} {}'.format('fox','brown','quick'))
    print('The {2} {1} {0}'.format('fox','brown','quick'))

    print('The {q} {b} {f}'.format(f='fox',b='brown',q='quick'))

    result = 100/777
    print('Result {r:1.3f}'.format(r=result))
    print('Result {r:10.3f}'.format(r=result))

    name = "Felipe"
    print(f'Hello, his name is {name}')

if __name__ == '__main__':
    main()