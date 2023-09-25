#20230920 HW

def main():
    for i in range(3):
        permutations(i+2)
        print('\n')
    return

def permutations(n:int):
    permutationList = []
    return value(n, permutationList)

def value(lenth:int, list:list):
    per_len = len(list)

    if per_len == lenth:
        return print(list)
    
    for i in range(lenth):
        list.append(i)
        value(lenth, list)
        list.pop()

    return

main()