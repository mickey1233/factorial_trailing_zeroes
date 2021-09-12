import math


def trailingzeroes(n):
    zeros = 0
    x = n
    while(n > 0):
        n //= 5
        zeros += n

    print(x, '! =', ' ', math.factorial(x), sep='')
    print('number of trailing zeroes = ', zeros)


def main():
    trailingzeroes(3)
    trailingzeroes(5)
    trailingzeroes(0)
    trailingzeroes(30)
    trailingzeroes(50)


if __name__ == "__main__":
    main()
