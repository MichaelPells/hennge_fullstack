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
    """
    `main` function:
    - Step 1: Reads the standard input for test cases.
    - Step 2: Calls `adder` function on first test case.
    - Step 3: Outputs program result to standard output.
    """

    # Step 1: Reads the standard input for test cases.
    data = open(0) # File descriptor `0` points to standard input
    N = int(data.readline()) # Reads `N` test cases on first line
    cases = data.readlines() # Reads the rest of the input (test cases) as a list of lines

    # Step 2: Calls `adder` function on first test case.
    test = 0 # Initialize number of test cases treated with `0`.
    output = [] # Create an empty list to store result of each test case.

    # Do `test + 1` for first test case,
    # and call `adder` function with all needed args.
    # This creates a recursion that treats all test cases
    # and stores all test results in `output`.
    adder(cases, N, test + 1, output)

    # Step 3: Outputs program result to standard output.
    # Join all results in `output` with `\n`
    open(1, "w").write("\n".join(output)) # File descriptor `1` points to standard output


if __name__ == "__main__":
    main()
