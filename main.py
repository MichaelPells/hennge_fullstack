"""
Time Complexity: O(N + M)
Space Complexity: O(N + M) due to input storage and recursion depth

Where:
N = Number of test cases
M = Total number of integers in all test cases
"""


def adder(cases: list, N: int, test: int, output: list, depth: int, maxdepth: int):
    """
    Finds the next test case, adds up the squares of the non-negative integers, and stores result in `output`.
    - `cases`:
    - `N`:
    - `test`:
    - `output`:
    - `depth`:
    - `maxdepth`:
    """

    # Step 1: Extracts test case.
    line = (test * 2) - 1 # Test (Y1, Y2, ..., Yn) is taken from every other line
    integers = map(int, cases[line].split()) # Convert test to an iterable of integers

    # Step 2: Filters out negative integers (`Yn`).
    integers = filter(lambda Yn: Yn >= 0, integers)

    # Step 3: Squares all integers.
    integers = map(lambda Yn: Yn**2, integers)

    # Step 4: Sums up all integers `(Y1 + Y2 + ... + Yn)`.
    result = sum(integers)

    # Step 5: Stores result to `output`.
    output.append(str(result)) # Append result to `output` object (as a string for `str.join()`).

    # Step 6: Calls another `adder` function on next test case if any,
    # or end recursion if none, or when maxdepth is reached.
    # This terminates current recursion if our maximum recursion depth (maxdepth) is reached.
    if test < N and depth < maxdepth:
        adder(cases, N, test + 1, output, depth + 1, maxdepth)

def recursion_manager(cases: list, N: int, test: int, output: list, depth : int = 0, maxdepth : int = 5):
    """
    Manages `adder`'s call stack, ensuring recursion depth slowly approaches `sys.getrecursionlimit()`.
    Breaks recursion into a series of smaller recursions in sizes of `maxdepth`,
    greatly inhibiting stack overflow and reducing space complexity to `O(N / maxdepth)`.
    """

    # Do `test + 1` for first (or next) test case,
    # and call `adder` function with all needed args.
    # This creates a recursion of `maxdepth` number of function calls
    # that treats only the next `maxdepth` number of test cases,
    # and stores each test result in `output`.
    # `output` object is provided by reference for a more efficient update to `output` across recursions.
    adder(cases, N, test + 1, output, depth + 1, maxdepth)

    # Start another recursion of `maxdepth` number of function calls
    # if there are still test cases left.
    if test + maxdepth < N:
        recursion_manager(cases, N, test + maxdepth, output) # Do `test + maxdepth` for next test case

def main():
    """
    Program entry point. Reads data from standard input, passes data to `recursion_manager`,
    and prints final result to standard output.
    """

    # Step 1: Reads the standard input for test cases.
    data = open(0) # File descriptor `0` points to standard input
    N = int(data.readline().strip()) # Reads `N` test cases on first line
    cases = data.read().splitlines() # Reads the rest of the input (test cases) as a list of lines

    # Step 2: Calls `adder` function on first test case.
    test = 0 # Initialize number of test cases treated with `0`.
    output = [] # Create an empty list to store result of each test case.

    # Start a recursion of `maxdepth` number of function calls if there are test cases.
    if N: recursion_manager(cases, N, test, output)

    # Step 3: Outputs program result to standard output.
    # Join all results in `output` with `\n`.
    open(1, "w").write("\n".join(output) + "\n") # File descriptor `1` points to standard output.

if __name__ == "__main__":
    main()
