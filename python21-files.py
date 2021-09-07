import argparse
import os
import shutil
import send2trash

def get_args():
    parser = argparse.ArgumentParser(description='Bottles of beer song',formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-n','--num',metavar='number',type=int,default=10,help='How many bottles')
    args = parser.parse_args()
    if args.num < 1:
        parser.error(f'--num "{args.num}" must be greater than 0')
    return args

def main():
    print('Files')
    
    '''
    f = open('file-practice2.txt','w+')
    f.write('Some test string --> 1')
    f.close()

    send2trash.send2trash('file-practice2.txt')

    f = open('file-practice2.txt','w+')
    f.write('Some test string --> 1')
    f.close()

    print(os.getcwd())
    print(os.listdir())
    print(os.listdir('C:\\Personal'))
    shutil.move('file-practice2.txt','C:\\Personal')
    '''

    for folder, sub_folders,files in os.walk("C:\\Personal\\Phyton-101\\MyMainPackage"):
        print(f"Currently lookin at {folder}")
        print('\n')
        print("Subfolders:")
        for sub_fold in sub_folders:
            print(f"Subfolder {sub_fold}")
        print('\n')
        print("The files are:")
        for f in files:
            print(f"\tFile {f}")
        print('\n')



if __name__ == '__main__':
    main()