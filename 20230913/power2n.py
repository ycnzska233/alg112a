# 20230913 HW
# https://github.com/ccc112a/py2cs/blob/master/02-演算法/02-方法/01-查表法/power2n/power2n.py

from datetime import datetime

_power2n = [None]*100
_power2n[0] = 1

def main():
    n = int(input('power2n, n='))
    if n < 0:
        return print('Enter n >= 0')

    print('----- ----- ----- -----')
    print('Method 1: 2**n')
    start_time = datetime.now()
    print(f'power2,{n} = {power2n1(n)}')
    end_time = datetime.now()
    use_time = end_time - start_time
    print(f'used time: {use_time}\n -----')

    print('Method 2: power2n(n-1)+power2n(n-1)')
    start_time = datetime.now()
    print(f'power2,{n} = {power2n2(n)}')
    end_time = datetime.now()
    use_time = end_time - start_time
    print(f'used time: {use_time}\n -----')

    print('Method 3: 2*power2n(n-1)')
    start_time = datetime.now()
    print(f'power2,{n} = {power2n3(n)}')
    end_time = datetime.now()
    use_time = end_time - start_time
    print(f'used time: {use_time}\n -----')

    print('Method 4: recursion + table')
    start_time = datetime.now()
    print(f'power2,{n} = {power2n4(n)}')
    end_time = datetime.now()
    use_time = end_time - start_time
    print(f'used time: {use_time}\n')

# power
def power2n1(n):
    return 2**n

# recursion1
# power2n(n-1)+power2n(n-1)
def power2n2(n):
    if n == 0:
        return 1
    return power2n2(n-1)+ power2n2(n-1)

# recursion2
# 2*power2n(n-1)
def power2n3(n):
    if n == 0:
        return 1
    return 2 * power2n3(n-1)

# recursion + table
# if
# power2n(n-1)+power2n(n-1) 
def power2n4(n):
    if _power2n[n] is None:
        return 2 * power2n4(n-1)
    return _power2n[n]

main()