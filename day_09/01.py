def compute_differential_series(series):
    """
        Compute the differential series of a given series.
        The differential series is a series of series, where each element series is
        the difference between two consecutive elements of the previous series.
        Visually:
            (S_0)            0   3   6   9  12  15
            (S_1)              3   3   3   3   3
            (S_2)                0   0   0   0

        This functions stops when S_i is all 0s and returns all the S_i.
    """
    def _process(series):
        res = []
        for i in range(len(series) - 1):
            res.append(series[i + 1] - series[i])
        return res

    diff_series = [series.copy()]

    # Stop when the last computed difference is all 0s
    while any(map(lambda x: x != 0, diff_series[-1])):
        diff_series.append(_process(diff_series[-1]))

    return diff_series


def find_next_element(series):
    """
        Find the next element in the series. First compute the differential series.
        Then, find the next elements of all the differential series in reverse order,
        by adding the last element of the i-th series to the last element of the 
        (i+1)-th (bottom) series.

        Visually:

            (S_0)            0   3   6   9  12  15   A
            (S_1)              3   3   3   3   3   B
            (S_2)                0   0   0   0   0

        The algorithm first finds B = 3 + 0 (last element of S_1 + last element of S_2),
        then finds A = 15 + B (last element of S_0 + B). The algorithm returns A.
    """
    diff_series = compute_differential_series(series)

    for i in range(len(diff_series) - 2, -1, -1):
        diff_series[i].append(diff_series[i+1][-1] + diff_series[i][-1])
    return diff_series[0][-1]

with open('input.txt', 'r') as f:
    lines = [line[:-1] for line in f.readlines()]

series = [list(map(int, line.split(' '))) for line in lines]

print(sum([find_next_element(s) for s in series]))