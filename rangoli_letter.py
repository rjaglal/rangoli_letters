'''

Prints the below pattern for the input size of > 1

--------e--------
------e-d-e------
----e-d-c-d-e----
--e-d-c-b-c-d-e--
e-d-c-b-a-b-c-d-e
--e-d-c-b-c-d-e--
----e-d-c-d-e----
------e-d-e------
--------e--------

'''


import string


# Single line printer
def print_line(size, last_num):
    alphabet = list(string.ascii_lowercase)
    width = (4 * (size - 1)) + 1
    line = ''

    # Creates string of right side of line --> "e-d-c-b-"
    for i in range((size - 1), last_num, -1):
        line += (str(alphabet[i]) + '-')

    # Create string for center of line --> "a"
    line += (str(alphabet[last_num]))

    # Create string for left side of line --> "b-c-d-e"
    for i in range(last_num + 1, size):
        line += "-" + str(alphabet[i])

    # Prints the whole line surrounded by a width of '-'
    print(line.center(width, '-'))


def print_rangoli(size):
    # Prints the top lines
    for last_num in range(size - 1, 0, -1):
        print_line(size, last_num)

    # Print the middle and bottom lines
    for last_num in range(0, size):
        print_line(size, last_num)


if __name__ == '__main__':
    print('Please enter an integer: ')
    n = int(input())
    print_rangoli(n)
