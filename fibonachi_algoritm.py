def recur_fibo(n):
    if n <= 1:
        return n
    else:
        return(recur_fibo(n-1) + recur_fibo(n-2))


def main():
    nterms = 10

    n1, n2 = 0, 1
    count = 0

    print("Fibonacci sequence (recursion):")
    for i in range(nterms):
        print(recur_fibo(i))

    print("Fibonacci sequence (while):")
    while count < nterms:
        print(n1)
        nth = n1 + n2
        # update values
        n1 = n2
        n2 = nth
        count += 1


if __name__ == "__main__":
    main()
