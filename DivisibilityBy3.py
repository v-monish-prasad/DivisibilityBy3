def isDivisibileBy3(array):
    sum = 0

    for i in array:
        sum += i % 3

    if sum % 3 == 0:
        return 1
    else:
        return 0


if __name__ == "__main__":
    A = list(map(int, input().strip('[').strip(']').split(',')))

    print(isDivisibileBy3(A))
