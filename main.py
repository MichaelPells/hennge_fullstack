def adder(cases, N, test, output):
    line = (test * 2) - 1
    integers = map(lambda i: int(i), cases[line].split())

    integers = filter(lambda Yn: Yn >= 0, integers)
    integers = map(lambda Yn: Yn**2, integers)
    result = sum(integers)

    output.append(str(result))

    if test < N:
        return adder(cases, N, test + 1, output)
    else:
        return output

def main():
    data = open(0)
    N = int(data.readline())
    cases = data.readlines()

    test = 0
    output = []

    adder(cases, N, test + 1, output)
    print("\n".join(output))


if __name__ == "__main__":
    main()
