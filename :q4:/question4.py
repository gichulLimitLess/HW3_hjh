def factorial(n):
    if n == 0:
        return 1
    elif n == 1:
        return n
    else:
        return n*factorial(n-1)

def main():
    for i in range (0, 15, 2):
        print("factorial {0:d}: {1:d}".format(i, factorial(i)))

if __name__ == '__main__':
    main()
        

    
