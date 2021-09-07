import argparse
from collections import Counter
from collections import defaultdict
from collections import namedtuple

def get_args():
    parser = argparse.ArgumentParser(description='Bottles of beer song',formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-n','--num',metavar='number',type=int,default=10,help='How many bottles')
    args = parser.parse_args()
    if args.num < 1:
        parser.error(f'--num "{args.num}" must be greater than 0')
    return args

def main():
    print('Collections')
    mylist = [1,1,1,1,1,1,1,1,1,1,3,3,3,3,3,3,4,4,4,4,9,9,1,4,3,9,2,2]
    mylist2 = ['a','a',10,9,10,1,1,2,'a']
    print(Counter(mylist))
    print(Counter(mylist2))
    print(Counter('aasbndaaklksosbb'))
    sentence = "how many times does each word show up in this sentence with a word"
    print(Counter(sentence.split()))
    letters='aaaabbbcccccccdddddddaaa'
    c=Counter(letters)
    print(c)
    print(c.most_common())
    print(c.values())
    print(c.keys())
    print(c.most_common(3))

    d= {'a':10}
    #d['hello'] #error

    d = defaultdict(lambda: 0)
    d['ok']=100
    print(d['bad'])

    mytuple = (10,20,30)
    print(mytuple[0])
    Dog = namedtuple('Dog',['age','breed','name'])
    manchitas = Dog(age=5,breed='Fox',name='Manchitas')
    print(type(manchitas))
    print(manchitas)
    print(manchitas.age)
    print(manchitas.breed)
    print(manchitas.name)
    print(manchitas[0])


    

if __name__ == '__main__':
    main()