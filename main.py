"""
Time Complexity: O(N + Xt)
Space Complexity: O(N + Xt) due to input storage and recursion depth

Where:
N = Number of test cases
Xt = Total number of integers in all test cases

Note: To avoid hitting the maximum recursion limit (`sys.getrecursionlimit()`) for test cases around 1000 and above,
I devised a technique I call Recursion Breaking. Works like magic!
"""


def adder(cases: list, N: int, test: int, output: list, maxframes: int, frames: int):
    """
    Finds the next test case, adds up the squares of the non-negative integers, and stores result in `output`.
    - `cases`: List of all test cases
    - `N`: Number of test cases
    - `test`: Index of current test case (starting at `1`)
    - `output`: List containing result from each test case
    - `maxframes`: Maximum number of stack frames allowed per recursion
    - `frames`: Current number of stack frames in current recursion
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
    # or end recursion if none, or when maxframes is reached.
    # This temporarily increases the recursion depth by `maxframes - frame` more number of `adder` function calls,
    # and terminates current recursion if the set maximum number of stack frames (`maxframes`) is reached:
    if test < N and frames < maxframes:
        adder(cases, N, test + 1, output, maxframes, frames + 1)

def recursion_manager(cases: list, N: int, test: int, output: list, maxframes : int):
    """
    Manages `adder`'s call stack, ensuring recursion depth slowly approaches `sys.getrecursionlimit()`.
    Breaks recursion into a series of smaller recursions in sizes of `maxframes`,
    greatly inhibiting stack overflow and empirically reducing a space complexity of `O(N)`
    to something like `O(N / maxframes)`.
    That is, the recursion depth only actually increases by `1` `recursion_manager` function call
    for every `maxframes` number of `adder` function calls.
    - `cases`: List of all test cases
    - `N`: Number of test cases
    - `test`: Index of last test case from last recursion.
    - `output`: List containing result from each test case
    - `maxframes`: Maximum number of stack frames allowed per recursion
    """

    # Do `test + 1` for first (or next) test case,
    # and call `adder` function with all needed args.
    # This creates a recursion of `maxframes` number of `adder` function calls
    # that treats only the next `maxframes` number of test cases,
    # and stores each test case result in `output`:
    adder(cases, N, test + 1, output, maxframes, 1)

    # Start another recursion of `maxframes` number of `adder` function calls, if there are still test cases left.
    if test + maxframes < N:
        # Call `adder` function if number of untreated test cases no longer exceeds `maxframes + 1`:
        if N - (test + maxframes) <= maxframes + 1:
            # Do `test + maxframes` for current test case, and reset `frames` for new call stack:
            adder(cases, N, test + maxframes + 1, output, maxframes + 1, 1)
        # Apply `recursion_manager` function if number of untreated test cases still exceeds `maxframes + 1`:
        else:
            recursion_manager(cases, N, test + maxframes, output, maxframes)

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
        # ensuring it never exceeds a set maximum number of stack frames (`maxframes`).

        # Set maximum number of stack frames between 3 and 27.
        # This range of values seemed optimal, recording a 0.000MB memory usage,
        # after memory profiling during testing with 100 test cases:
        maxframes = 10

        if N <= maxframes + 1: # Call `adder` function directly if `N` does not exceed `maxframes + 1`.
            adder(cases, N, test + 1, output, maxframes + 1, 1)
        else: # Apply `recursion_manager` function if `N` exceeds `maxframes + 1`.
            recursion_manager(cases, N, test, output, maxframes)

        # Note 1:
        # To ensure this alogrithm's recursion depth is not unnecessarily increased
        # by 1 underlying `recursion_manager` function call, for `N <= maxframes + 1`,
        # `adder` is rather called directly for such cases where `N <= maxframes + 1`.
        # `maxframes + 1`, because optimality does not actually start until `maxframes + 2`

        # Note 2: `output` object is passed by reference for a more efficient update to `output` across recursions.

    # Step 3 - Output program result to standard output:
    open(1, "w").write("".join(output)) # Join all results in `output`. (File descriptor `1` points to standard output.)

if __name__ == "__main__":
    main()
