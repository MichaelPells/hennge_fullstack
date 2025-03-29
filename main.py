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
    integers = map(int, cases[line].strip().split()) # Convert test to an iterable of integers

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
    # This temporarily increases the recursion depth by `maxdepth - 1` more number of `adder` function calls,
    # and terminates current recursion if the set maximum recursion depth (`maxdepth`) is reached.
    if test < N and depth < maxdepth:
        adder(cases, N, test + 1, output, depth + 1, maxdepth)

def recursion_manager(cases: list, N: int, test: int, output: list, depth : int, maxdepth : int):
    """
    Manages `adder`'s call stack, ensuring recursion depth slowly approaches `sys.getrecursionlimit()`.
    Breaks recursion into a series of smaller recursions in sizes of `maxdepth`,
    greatly inhibiting stack overflow and reducing space complexity to `O(N / maxdepth)`.
    The recursion depth only increases by `1` `recursion_manager` function call
    for every `maxdepth` number of `adder` function calls.
    """

    # Do `test + 1` for first (or next) test case,
    # and call `adder` function with all needed args.
    # This creates a recursion of `maxdepth` number of `adder` function calls
    # that treats only the next `maxdepth` number of test cases,
    # and stores each test result in `output`.
    # `output` object is provided by reference for a more efficient update to `output` across recursions.
    adder(cases, N, test + 1, output, depth + 1, maxdepth)

    # Start another recursion of `maxdepth` number of `adder` function calls
    # if there are still test cases left.
    if test + maxdepth < N:
        # Do `test + maxdepth` for current test case, and reset `depth`.

        # Call `adder` function if number of untreated test cases no longer exceeds `maxdepth + 1`.
        if N - (test + maxdepth) <= maxdepth + 1:
            adder(cases, N, test + maxdepth + 1, output, 1, maxdepth + 1)
        # Apply `recursion_manager` function if number of untreated test cases still exceeds `maxdepth + 1`.
        else:
            recursion_manager(cases, N, test + maxdepth, output, 0, maxdepth)
from memory_profiler import profile
@profile(precision=4)
def main():
    """
    Program entry point. Reads data from standard input, passes data to `recursion_manager`,
    and prints final result to standard output.
    """

    # Step 1: Reads the standard input for test cases.
    data = open(0) # File descriptor `0` points to standard input
    N = int(data.readline().strip()) # Reads `N` test cases on first line
    cases = data.readlines() # Reads the rest of the input (test cases) as a list of lines

    # Step 2: Calls `adder` function on first test case.
    test = 0 # Initialize number of test cases treated with `0`.
    output = [] # Create an empty list to store result of each test case.

    if N: # If there are test cases
        # To optimize space complexity, implement a recursion manager to manage `adder`'s call stack,
        # ensuring it never exceeds a set maximum recursion depth (`maxdepth`)

        # Set maximum recursion depth between 3 and 27.
        # This range of values seemed optimal, recording a 0.000MB memory usage,
        # after memory profiling during testing with 100 test cases.
        maxdepth = 10

        if N <= maxdepth + 1: # Call `adder` function if `N` does not exceed `maxdepth + 1`.
            adder(cases, N, test + 1, output, 1, maxdepth + 1)
        else: # Apply `recursion_manager` function if `N` exceeds `maxdepth + 1`.
            recursion_manager(cases, N, test, output, 0, maxdepth)

        # Note:
        # To ensure this alogrithm's recursion depth is not unnecessarily increased by 1, for `N <= maxdepth + 1`,
        # (with an underlying `recursion_manager` function call),
        # `adder` is called directly for such cases where `N <= maxdepth + 1`.
        # `maxdepth + 1`, because optimality does not actually start until `maxdepth + 2`

        # Step 3: Outputs program result to standard output.
        # Join all results in `output` with `\n`.
        open(1, "w").write("\n".join(output) + "\n") # File descriptor `1` points to standard output.

if __name__ == "__main__":
    main()
