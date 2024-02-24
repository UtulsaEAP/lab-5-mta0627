def fibonacci(n):
    #write your code here
    
    n1 = 0
    n2 = 1
    for i in range(n-1):
        n3 = n1 + n2
        n1 = n2
        n2 = n3
    if n > 0:
        return n2
    elif n == 0:
        return n1
    else:
        return -1
    


if __name__ == '__main__':
    start_num = int(input())
    print(f'fibonacci({start_num}) is {fibonacci(start_num)}')