"""
Gets the first X numbers from a file and writes them to another one.
"""
import os, sys

def read_file_lines(file_name):
    with open(file_name, mode='r') as first_file:
        file_lines = first_file.readlines()

    file_lines = [line.strip() for line in file_lines]
    return file_lines

def write_iterable_to_file(file_name, iterable):
    with open(file_name, mode='w') as out_file:
        for item in iterable:
            out_file.write(item + '\n')
        out_file.truncate(out_file.tell() - len(os.linesep))  # remove last '\n'

if len(sys.argv) < 4:
    print('Usage: python {} IN_FILE_NAME OUT_FILE_NAME NUM_NUMBERS')
    sys.exit(0)

IN_FILE_NAME = sys.argv[1]
OUT_FILE_NAME = sys.argv[2]
NUM_NUMBERS = int(sys.argv[3])

file_numbers = read_file_lines(IN_FILE_NAME)
numbers_to_write = file_numbers[0:NUM_NUMBERS]
write_iterable_to_file(OUT_FILE_NAME, numbers_to_write)

print('Numbers Written: {}'.format(NUM_NUMBERS))
