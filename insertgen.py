import fileinput
import sys
import os
from formatData import formatdata


str_pos = []
ignore_space = []

try:

    if len(sys.argv) == 2 and sys.argv[1] == '--help':
        sys.exit(
            'Execute -> python insertgen.py <input file path> <output file path> \n Ex. "python insertgen.py home/xyz/input.txt home/xyz/output.txt"')
    elif len(sys.argv) == 1:
        print('Takes arguments <input file path> , <output file path>\n')
        sys.exit(
            'Two args required, none given , type "insertgen.py --help" for help\n')
    elif len(sys.argv) == 2:
        print('Takes arguments <input file path> , <output file path> -> <output file path> missing\n')
        sys.exit(
            'Two args required , only 1 given , type "insertgen.py --help" for help\n')

    else:
        file = open(sys.argv[2], 'w')
        input_fname_split = os.path.splitext(sys.argv[1])
        if input_fname_split[-1] != '.txt':
            sys.exit(
                f'Error -> input file extension -> {input_fname_split[-1]}, input file should only be .txt extension\n')
        col = int(input("Number of columns: "))
        while True:
            num_of_str = int(input("Total number string columns: "))
            if num_of_str <= col:
                break
            else:
                print("number of string columns can't be more than total columns\n")

        for i in range(0, num_of_str):
            str_pos.append(int(input("Enter string column number: ")))

        while True:
            pos = int(
                input("Position of space to ignore (-1 for no space to ignore): "))
            if pos == -1:
                break

            ignore_space.append(pos)
        print('\n')
        print(f'Number of columns:{col}', f'Number of string values in data {num_of_str}',
              f'space position to ignore {ignore_space}')

        for line in fileinput.input():
            formatdata(line, col, num_of_str, str_pos,
                       ignore_space, file)

        print("Success")
        file.close()
        sys.exit(f'Output file at : {sys.argv[2]}')


except Exception as e:
    print(e)
