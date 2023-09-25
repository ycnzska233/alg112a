# 20230920 exercise
# https://github.com/ccc112a/py2cs/blob/master/02-演算法/02-方法/02a-列舉法/03-permutation/permutation.py
# 思考：排到一半 p=[1,3] 繼續排下去
# ex: [1,3,0..], [1,3,1..], [1,3,2..], [1,3,3..] 全部試一遍

def main():

    for i in range(3):
        exercise(i+3)
        print('\n')

    return

def exercise(n:int):
    list = [1,3]
    permutations(n, list)

def permutations(lenth:int, per_list:list):
    per_len = len(per_list)
    if per_len == lenth:
        return print(per_list)
    
    for i in range(lenth):
        per_list.append(i)
        permutations(lenth, per_list)
        per_list.pop()

    return

main()
