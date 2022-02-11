# amain file
from platform import architecture
from os_info import *


def draw_screen():
    _os_ = os_info()
    name = _os_.distro()
    architecture = _os_.architecture()
    clock = _os_.sys_time(0, 1)
    column = [
        ['os name', name],
        ['architecture', architecture],
        ['time', clock]
    ]
    _ascii_ = _os_.ascii_logo()
    for i in range(0, len(_ascii_)):
        print(''.join(_ascii_[i]), end='')
        if i < len(column):
            print('\t\t\t' + ' : '.join(column[i]))
        else:
            print()




def main():
    draw_screen()



if __name__ == "__main__":
    main()
