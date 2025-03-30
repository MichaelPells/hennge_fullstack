"""
Time Complexity: O(N + Xt)
Space Complexity: O(N + Xt) due to input storage and recursion depth

Where:
N = Number of test cases
Xt = Total number of integers in all test cases

Note: To avoid hitting the maximum recursion limit (`sys.getrecursionlimit()`) for test cases around 1000 and above,
I devised a technique I call Recursion Breaking. Works like magic!
"""


def adder(cases: list, N: int, test: int, output: list, maxdepth: int, depth: int):
    """
    Finds the next test case, adds up the squares of the non-negative integers, and stores result in `output`.
    - `cases`: List of all test cases
    - `N`: Number of test cases
    - `test`: Index of current test case (starting at `1`)
    - `output`: List containing result from each test case
    - `maxdepth`: Maximum recursion depth allowed per recursion
    - `depth`: Recursion depth for current function call in each recursion's call stack
    """

    # Step 1 - Extract test case:
    line = (test * 2) - 1 # Actual test case (Y1, Y2, ..., Yn) is taken from every other line.
    integers = map(int, cases[line].strip().split()) # Convert test case to an iterable of integers.

    # Step 2 - Filter out negative integers (`Yn`):
    integers = filter(lambda Yn: Yn >= 0, integers)

    # Step 3 - Square all integers:
    integers = map(lambda Yn: Yn**2, integers)

    # Step 4 - Sum up all integers: `(Y1 + Y2 + ... + Yn)`:
    result = sum(integers)

    # Step 5 - Store result to `output`:
    output.append(f"{result}\n") # Append result to `output` object (as a string for `str.join()`).

    # Step 6 - Call another `adder` function on next test case if any,
    # or end recursion if none, or when maxdepth is reached.
    # This temporarily increases the recursion depth by `maxdepth - depth` more number of `adder` function calls,
    # and terminates current recursion if the set maximum recursion depth (`maxdepth`) is reached:
    if test < N and depth < maxdepth:
        adder(cases, N, test + 1, output, maxdepth, depth + 1)

def recursion_manager(cases: list, N: int, test: int, output: list, maxdepth : int):
    """
    Manages `adder`'s call stack, ensuring recursion depth slowly approaches `sys.getrecursionlimit()`.
    Breaks recursion into a series of smaller recursions in sizes of `maxdepth`,
    greatly inhibiting stack overflow and reducing a space complexity of `O(N)` to something like `O(N / maxdepth)`.
    That is, the recursion depth only actually increases by `1` `recursion_manager` function call
    for every `maxdepth` number of `adder` function calls.
    - `cases`: List of all test cases
    - `N`: Number of test cases
    - `test`: Index of last test case from last recursion.
    - `output`: List containing result from each test case
    - `maxdepth`: Maximum recursion depth allowed per recursion
    """

    # Do `test + 1` for first (or next) test case,
    # and call `adder` function with all needed args.
    # This creates a recursion of `maxdepth` number of `adder` function calls
    # that treats only the next `maxdepth` number of test cases,
    # and stores each test case result in `output`:
    adder(cases, N, test + 1, output, maxdepth, 1)

    # Start another recursion of `maxdepth` number of `adder` function calls, if there are still test cases left.
    if test + maxdepth < N:
        # Call `adder` function if number of untreated test cases no longer exceeds `maxdepth + 1`:
        if N - (test + maxdepth) <= maxdepth + 1:
            # Do `test + maxdepth` for current test case, and reset `depth`:
            adder(cases, N, test + maxdepth + 1, output, maxdepth + 1, 1)
        # Apply `recursion_manager` function if number of untreated test cases still exceeds `maxdepth + 1`:
        else:
            recursion_manager(cases, N, test + maxdepth, output, maxdepth)

def main():
    """
    Program entry point. Reads data from standard input, passes data to `adder` or `recursion_manager`,
    and prints final result to standard output.
    """

    # Step 1 - Read the standard input for test cases:
    data = open(0) # (File descriptor `0` points to standard input.)
    N = int(data.readline().strip()) # Read number of test cases `N` on first line.
    cases = data.readlines() # Read the rest of the input (test cases) as a list of lines

    # Step 2 - Call `adder` function on first test case or pass data to `recursion_manager`:
    test = 0 # Initialize number of test cases treated with `0`.
    output = [] # Create an empty list to store result of each test case.

    if N: # If there are test cases
        # To optimize space complexity, implement a recursion manager to manage `adder`'s call stack,
        # ensuring it never exceeds a set maximum recursion depth (`maxdepth`).

        # Set maximum recursion depth between 3 and 27.
        # This range of values seemed optimal, recording a 0.000MB memory usage,
        # after memory profiling during testing with 100 test cases:
        maxdepth = 10

        if N <= maxdepth + 1: # Call `adder` function directly if `N` does not exceed `maxdepth + 1`.
            adder(cases, N, test + 1, output, maxdepth + 1, 1)
        else: # Apply `recursion_manager` function if `N` exceeds `maxdepth + 1`.
            recursion_manager(cases, N, test, output, maxdepth)

        # Note 1:
        # To ensure this alogrithm's recursion depth is not unnecessarily increased
        # by 1 underlying `recursion_manager` function call, for `N <= maxdepth + 1`,
        # `adder` is rather called directly for such cases where `N <= maxdepth + 1`.
        # `maxdepth + 1`, because optimality does not actually start until `maxdepth + 2`

        # Note 2: `output` object is passed by reference for a more efficient update to `output` across recursions.

    # Step 3 - Output program result to standard output:
    open(1, "w").write("".join(output)) # Join all results in `output`. (File descriptor `1` points to standard output.)

if __name__ == "__main__":
    main()
