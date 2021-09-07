import argparse
from typing import List

def get_args():
    parser = argparse.ArgumentParser(description='Bottles of beer song',formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-n','--num',metavar='number',type=int,default=10,help='How many bottles')
    args = parser.parse_args()
    if args.num < 1:
        parser.error(f'--num "{args.num}" must be greater than 0')
    return args

def main():
    my_list = [1,2,3]
    my_list = ['hello',1,2]
    print(len(my_list))
    print(my_list[0])
    print(my_list[1:])
    anotherlist= [5,6]
    print(my_list + anotherlist)

    new_list = my_list + anotherlist
    new_list[0] = 'Someting Else'.upper()
    print(new_list)
    new_list.append(9)
    print(new_list)
    x = new_list.pop()
    print(x)
    print(new_list)
    x = new_list.pop(0)
    print(x)

    new_list = ['a','e','x','b','c']
    num_list = [4,3,1,8,3]
    new_list.sort() #['a', 'b', 'c', 'e', 'x']
    num_list.sort() #[1, 3, 3, 4, 8]
    print(new_list)
    print(num_list)

    sortedList = new_list.sort()
    print(type(sortedList)) #none

    num_list.reverse()
    print(num_list)

    new_list = []
    new_list.append(2)
    new_list.append(3)
    new_list.append(4)
    del new_list[1:]
    print(new_list)
    new_list.clear()
    print(new_list)

    my_list2 = list()
    my_list2.append(3)
    print(my_list2)


if __name__ == '__main__':
    main()