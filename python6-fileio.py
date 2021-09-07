import argparse

def get_args():
    parser = argparse.ArgumentParser(description='Bottles of beer song',formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-n','--num',metavar='number',type=int,default=10,help='How many bottles')
    args = parser.parse_args()
    if args.num < 1:
        parser.error(f'--num "{args.num}" must be greater than 0')
    return args

def main():
    print('I/O')
    f = open('test.txt')
    str = f.read()
    print(str)
    str = f.read()
    print(str)
    f.seek(0)
    str = f.read()
    print(str)
    f.seek(0)
    lines = f.readlines()
    print(lines)
    f.close()
    
    with open('test.txt','r') as my_new_file:
        contents = my_new_file.readlines()
    print(contents)

    with open('test.txt',mode='a') as f:
        f.write('\nhell0 4')
    
    with open('test.txt',mode='r') as f:
        contents = f.readlines()
    print(contents)

    with open('somefile.txt',mode='w') as w:
        w.write('some new file')
    
    with open('somefile.txt',mode='r') as f:
        contents = f.read()
    print(contents)

if __name__ == '__main__':
    main()