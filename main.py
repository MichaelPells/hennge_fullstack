import sys

def main():
    integers = [2, -2, 5, -1]

    integers = filter(lambda Yn: Yn >= 0, integers)
    integers = map(lambda Yn: Yn**2, integers)
    result = sum(integers)

    print(result)


if __name__ == "__main__":
    main()
