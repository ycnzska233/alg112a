#20230920 HW

def main():
    n = int(input())
    
    return

def truthTable(n:int):
    truthtable = []
    return value(n, truthtable)

def value(n:int, table:list):

    lenth = len(table)

    if lenth == n:
        print(table)
        return
    
    for i in [0,1]:
        table.append(i)
        value(n, table)
        table.pop()
    
    return

main()