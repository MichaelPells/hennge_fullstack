def adder(cases, N, test, output):
    """
    `adder` function:
    - Step 1: Extracts test case.
    - Step 2: Filters out negative integers (`Yn`).
    - Step 3: Squares all integers.
    - Step 4: Sums up all integers `(Y1 + Y2 + ... + Yn)`.
    - Step 5: Stores result to `output`.
    - Step 6: Calls another `adder` function on next test case, if any, or end recursion, if none.
    """

    # Step 1: Extracts test case.
    line = (test * 2) - 1 # Test (Y1, Y2, ..., Yn) is taken from every other line
    integers = map(lambda i: int(i), cases[line].split()) # Convert test to an iterable of integers

    # Step 2: Filters out negative integers (`Yn`).
    integers = filter(lambda Yn: Yn >= 0, integers)

    # Step 3: Squares all integers.
    integers = map(lambda Yn: Yn**2, integers)

    # Step 4: Sums up all integers `(Y1 + Y2 + ... + Yn)`.
    result = sum(integers)

    # Step 5: Stores result to `output`.
    output.append(str(result)) # Append result to `output` object (as a string for `str.join()`).

    # Step 6: Calls another `adder` function on next test case, if any, or end recursion, if none.
    if test < N:
        adder(cases, N, test + 1, output)

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
    # `output` object is intentionally provided by reference, for a more efficient update to `output` across recursion.
    adder(cases, N, test + 1, output)

    # Step 3: Outputs program result to standard output.
    # Join all results in `output` with `\n`.
    open(1, "w").write("\n".join(output)) # File descriptor `1` points to standard output.


if __name__ == "__main__":
    main()
