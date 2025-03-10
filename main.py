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
    data = """2
4
3 -1 1 14
5
9 6 -53 32 16""".splitlines()

    N = int(data[0])
    test = 0
    output = []

    adder(data, N, test + 1, output)
    print("\n".join(output))


if __name__ == "__main__":
    main()
