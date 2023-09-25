#20230920 HW

from itertools import permutations

def main():

    for i in range(3):
        result = list(permutations(range(1,i+3)))
        print(f'{result}\n')

    return

main()