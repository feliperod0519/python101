import argparse

def get_args():
    parser = argparse.ArgumentParser(description='Bottles of beer song',formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-n','--num',metavar='number',type=int,default=10,help='How many bottles')
    args = parser.parse_args()
    if args.num < 1:
        parser.error(f'--num "{args.num}" must be greater than 0')
    return args

def ask_for_int():
    while True:
        try:
            result = int(input("Provide number:"))
        except:
            print("Not a number!")
            continue
        else:
            print("Ok")
            break
        finally:
            print("Hello")
            break
    

def main():
    print('Exception Handling')
    try:
        result = 10 + 10
        result = 10 + '10'
    except:
        print("Something went wrong")
    else:
        print("Everything went fine")
        print(result)
    try:
        f = open('somefile.txt','w') # no error
        #f = open('somefile.txt','r') # error
        f.write('Test line')
    except TypeError:
        print('TypeError')
    except OSError:
        print('OS Error')
    except:
        print("All other errors")
    finally:
        print('I always run')
    ask_for_int()

if __name__ == '__main__':
    main()

