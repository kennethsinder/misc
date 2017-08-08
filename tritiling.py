def tile(x):
    A = [0] * (x + 1)
    B = [0] * (x + 1)
    B[2] = B[0] = 1
    A[2] = A[0] = 1
    for i in range(2, x):
        B[i] = B[i - 2] + 2 * A[i - 1]
    return B[x]


if __name__ == '__main__':
    x = 0
    outputs = []
    while x != -1:
        x = int(input())
        if x != -1:
            outputs.append(tile(x))
    for output in outputs:
        print(output)