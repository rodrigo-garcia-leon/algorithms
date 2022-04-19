import math


def countTriplets(arr, r):
    t = 0
    n = len(arr)
    a = None

    for i in range(n-2):
        if a is None:
            a = arr[i]

        ri = int(math.log(arr[i] / a, r)) if r > 1 else a

        for j in range(i+1, n-1):
            rj = int(math.log(arr[j] / a, r)) if r > 1 else a+1

            if rj != ri + 1:
                continue

            for k in range(j+1, n):
                rk = int(math.log(arr[k] / a, r)) if r > 1 else a+2

                if rk != rj + 1:
                    continue

                t += 1

    return t


with open('input.txt', 'r') as f:
    [n, r] = list(map(int, f.readline().strip().split(' ')))
    arr = list(map(int, f.readline().strip().split(' ')))
    t = countTriplets(arr, r)
    print(t)
