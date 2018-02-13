"""
olx.pt specific phone number filterer. It does the following:

1. Removes '351' from the beginning, if it exists
2. Checks if the number begins with one of the following:
    * 91
    * 92
    * 93
    * 96
3. Makes sure that the length of the number is 9
4. Appends +351 to the number
5. Removes all duplicates

NOTE: the code here is far from the best one. This has been written to
quickly address a need. Major refactoring needed in the future.
"""

import sys

# Not the most efficient way, specially if lists get too large.
# For project-specific use case it's perfectly fine and no need to
#  complicate.
phone_numbers = []


# STATS
ERR_CARRIER = 0
ERR_CARRIER_LIST = []
ERR_LENGTH = 0
ERR_LENGTH_LIST = []
ERR_351 = 0
PHONE_NUMS_WRITTEN = 0
DUPLICATES = 0

def filter_351(phone_number):
    global ERR_351

    if phone_number is None:
        return None

    if phone_number.startswith('351'):
        ERR_351 += 1
        return phone_number[3:]
    else:
        return phone_number

def filter_carriers(phone_number):
    global ERR_CARRIER
    global ERR_CARRIER_LIST

    if phone_number is None:
        return None

    start_digits = phone_number[0:2]

    if start_digits in ('91', '92', '93', '96'):
        return phone_number
    else:
        ERR_CARRIER += 1
        ERR_CARRIER_LIST += [phone_number]
        return None

def filter_length(phone_number):
    global ERR_LENGTH
    global ERR_LENGTH_LIST

    if phone_number is None:
        return None

    if len(phone_number) == 9:
        return phone_number
    else:
        ERR_LENGTH += 1
        ERR_LENGTH_LIST += [phone_number]
        return None

def append_351(phone_number):
    if phone_number is None:
        return None

    return '+351{}'.format(phone_number)

def add_phone_number_if_not_None(phone_number):
    global phone_numbers
    global PHONE_NUMS_WRITTEN

    if phone_number is not None:
        phone_numbers += [phone_number]
        PHONE_NUMS_WRITTEN += 1

def remove_duplicates():
    global phone_numbers, DUPLICATES

    print('Removing duplicates...')
    len_before = len(phone_numbers)
    phone_numbers = list(set(phone_numbers))
    len_after = len(phone_numbers)

    DUPLICATES = len_before - len_after

def print_stats():
    global ERR_351, ERR_CARRIER, ERR_CARRIER_LIST, ERR_LENGTH
    global ERR_LENGTH_LIST, PHONE_NUMS_WRITTEN, DUPLICATES

    print('Total Numbers Written: {}\n---\n'.format(PHONE_NUMS_WRITTEN))
    print('351 Errors : {}'.format(ERR_351))
    print('Carrier Errors : {}'.format(ERR_CARRIER))
    print('Lenght Errors: {}'.format(ERR_LENGTH))
    print('Duplicates: {}'.format(DUPLICATES))
    print('\n----\n')
    print('Carrier Errors:')
    print(ERR_CARRIER_LIST)
    print('\nLength Errors:')
    print(ERR_LENGTH_LIST)

def run():
    global phone_numbers

    IN_FILE_NAME = None
    OUT_FILE_NAME = None

    if len(sys.argv) < 3:
        print('Usage: python {} <IN_FILE_NAME> <OUT_FILE_NAME>'.format(sys.argv[0]))
        sys.exit(0)

    IN_FILE_NAME = sys.argv[1]
    OUT_FILE_NAME = sys.argv[2]

    with open(IN_FILE_NAME, mode='r') as in_file:
        for phone_number in in_file:
            phone_number = phone_number.strip()
            phone_number = filter_351(phone_number)
            phone_number = filter_carriers(phone_number)
            phone_number = filter_length(phone_number)
            phone_number = append_351(phone_number)
            add_phone_number_if_not_None(phone_number)

    remove_duplicates()

    print('Writing output to file...')
    with open(OUT_FILE_NAME, mode='w') as out_file:
        for phone_number in phone_numbers:
            out_file.write(phone_number + '\n')

    print_stats()

if __name__ == '__main__':
    run()
