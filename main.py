import sys

def adder(data, N, test, output):
    line = test * 2
    integers = map(lambda i: int(i), data[line].split())

    integers = filter(lambda Yn: Yn >= 0, integers)
    integers = map(lambda Yn: Yn**2, integers)
    result = sum(integers)

    output.append(str(result))

    if test < N:
        return adder(data, N, test + 1, output)
    else:
        return output

def main():
    N = int(sys.stdin.readline())
    data = sys.stdin.readlines(N * 2)

    test = 0
    output = []

    adder(data, N, test + 1, output)
    print("\n".join(output))


if __name__ == "__main__":
    main()
