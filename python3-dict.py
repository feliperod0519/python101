import argparse

def get_args():
    parser = argparse.ArgumentParser(description='Bottles of beer song',formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-n','--num',metavar='number',type=int,default=10,help='How many bottles')
    args = parser.parse_args()
    if args.num < 1:
        parser.error(f'--num "{args.num}" must be greater than 0')
    return args

def main():
    print('Dictionaries')
    my_dict = {'k1':'v1','k2':'v2'}
    print(my_dict)
    print(my_dict['k1'])

    d = {'k1':123, 'k2':[0,1,2,3], 'k3':{'innerKey':100}}
    print(d)
    print(d['k2'][2])
    print(d['k3']['innerKey'])

    newd = {'k1':100, 'k2':200}
    newd['k3'] = 300
    print(newd)
    newd['k1']= 'something else'
    print(newd)

    print(d.keys()) # dict_keys(['k1', 'k2', 'k3'])
    print(d.values()) # dict_values([123, [0, 1, 2, 3], {'innerKey': 100}])
    print(d.items()) # dict_items([('k1', 123), ('k2', [0, 1, 2, 3]), ('k3', {'innerKey': 100})])

    mydict = dict()


if __name__ == '__main__':
    main()