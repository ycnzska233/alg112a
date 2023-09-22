#20230913 HW

from datetime import datetime

_fib=[None]*100
_fib[0] = 0
_fib[1] = 1


def main():
    n = int(input())

    print('fib:')
    start_time = datetime.now()
    for i in range(n+1):
        print(fib(i))
    end_time = datetime.now()
    use_time = end_time - start_time
    print(f'time of fib(): {use_time}')

    print('fib_look:')
    start_time = datetime.now()
    for i in range(n+1):
        print(fib_lookup(i))
    end_time = datetime.now()
    use_time = end_time - start_time
    print(f'time of fib_look(): {use_time}') 
    
def fib(n):
    if n>1:
        return fib(n-1)+fib(n-2)
    return n


def fib_lookup(n):
    if _fib[n] is None :
        _fib[n] = fib_lookup(n-1) + fib_lookup(n-2)
    return _fib[n]

main()
