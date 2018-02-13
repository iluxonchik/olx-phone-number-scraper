"""
Removes numbers that are contained in the second file from the first file.
"""
import sys, os

if len(sys.argv) < 4:
    print('Usage: python {} FIRST_FILE SECOND_FILE OUT_FILE')
    print('\tRemoves all numbers from the FIRST_FILE that are contained in the'
    ' SECOND_FILE. Writes the result to the OUT_FILE.')
    sys.exit(0)

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


FIRST_FILE = sys.argv[1]
SECOND_FILE = sys.argv[2]
OUT_FILE = sys.argv[3]

first_file_lines = read_file_lines(FIRST_FILE)
second_file_lines = read_file_lines(SECOND_FILE)

ORIGINAL_FIRST_FILE_LEN = len(first_file_lines)
ORIGINAL_SECOND_FILE_LEN = len(second_file_lines)

first_file_lines = set(first_file_lines)
second_file_lines = set(second_file_lines)
out_file_lines = first_file_lines - second_file_lines

write_iterable_to_file(OUT_FILE, out_file_lines)

SET_FIRST_FILE_LEN = len(first_file_lines)
SET_SECOND_FILE_LEN = len(second_file_lines)

OUT_FILE_LEN = len(out_file_lines)
NUMBERS_REMOVED = SET_FIRST_FILE_LEN - OUT_FILE_LEN

if ORIGINAL_FIRST_FILE_LEN != SET_FIRST_FILE_LEN:
    print('[WARN!] FIRST_FILE was not preprocessed correctly. Duplicates found!')

if ORIGINAL_SECOND_FILE_LEN != SET_SECOND_FILE_LEN:
    print('[WARN!] SECOND_FILE was not preprocessed correctly. Duplicates found!')

print('Numbers Written: {}'.format(OUT_FILE_LEN))
print('Numbers Removed: {}'.format(NUMBERS_REMOVED))
