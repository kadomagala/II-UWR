import random
from random import randrange
import queue
import numpy as np

DEBUG = False


def print_nonogram(nonogram):
    for x in nonogram:
        for y in x:
            print('#' if y == '1' else '.')
        print()

global dist_rows
global dist_cols

def solve(rows, cols):
    nonogram = shuffle_nonogram(len(rows), len(cols))

    MAX_NUM_OF_CHANGES = len(rows) * len(cols) * 25
    num_of_changes = 0
    small_probability = 0.15
    global dist_rows
    global dist_cols

    dist_rows = calc_dists(rows)
    dist_cols = calc_dists(cols)
    while True:
        if num_of_changes >= MAX_NUM_OF_CHANGES:  # lets try again
            nonogram = shuffle_nonogram(len(rows), len(cols))
            num_of_changes = 0
        num_of_changes += 1

        rows_to_fix = get_unsolved_rows_idxs(rows, nonogram)

        cols_to_fix = get_unsolved_cols_idxs(cols, nonogram)

        if len(rows_to_fix) == 0 and len(cols_to_fix) == 0:
            return nonogram

        axis = np.random.choice([True, False])

        non_optimal_strategy = np.random.random(1)[0] <= small_probability

        if axis:  # work on row
            i = 0
            if non_optimal_strategy:
                i = np.random.randint(len(rows))
            else:
                if len(rows_to_fix) > 0:
                    i = np.random.choice(rows_to_fix)
            if len(rows_to_fix) == 0 and not non_optimal_strategy:
                continue

            j_candidates = [0]  # canidates for column, might be more than one so lets pick random
            max_sum_level = len(rows) * len(cols)
            for j in range(len(cols)):
                # suppose we want to fix j column
                j_sum = sum_level(i, j, rows, cols, nonogram)

                if j_sum < max_sum_level:
                    max_sum_level = j_sum
                    j_candidates = [j]
                elif j_sum == max_sum_level:
                    j_candidates.append(j)

            j_candidates = np.random.choice(j_candidates)
            nonogram[i][j_candidates] = '0' if nonogram[i][j_candidates] == '1' else '1'
        else:  # work on column
            j = 0
            if non_optimal_strategy:
                j = np.random.randint(len(cols))
            else:
                if len(cols_to_fix) > 0:
                    j = np.random.choice(cols_to_fix)
            if len(cols_to_fix) == 0 and not non_optimal_strategy:
                continue

            i_candidates = [0]
            max_sum_level = len(rows) * len(cols)

            for i in range(len(rows)):  # suppose we want to fix i row
                i_sum = sum_level(i, j, rows, cols, nonogram)

                if i_sum < max_sum_level:
                    max_sum_level = i_sum
                    i_candidates = [i]
                elif i_sum == max_sum_level:
                    i_candidates.append(i)

            i_candidates = np.random.choice(i_candidates)
            nonogram[i_candidates][j] = '0' if nonogram[i_candidates][j] == '1' else '1'


def sum_level(row, col, rows, cols, nonogram):
    """
    Counts how good is it to swap nonogram[i][j] compared to not swaping at all
    """
    current_row_dist = opt_dist(nonogram[row, :], rows[row], dist_rows[row])
    current_col_dist = opt_dist(nonogram[:, col], cols[col], dist_cols[col])
    current_sum = current_row_dist + current_col_dist

    nonogram[row][col] = '1' if nonogram[row][col] == '0' else '0'

    changed_row_dist = opt_dist(nonogram[row, :], rows[row], dist_rows[row])
    changed_col_dist = opt_dist(nonogram[:, col], cols[col], dist_cols[col])
    changed_sum = changed_row_dist + changed_col_dist

    nonogram[row][col] = '1' if nonogram[row][col] == '0' else '0'
    return changed_sum - current_sum


def get_unsolved_rows_idxs(rows, nonogram):
    """
        Returns indexes of rows which are not correct
    """
    to_pick = []
    for i in range(len(rows)):
        if opt_dist(nonogram[i, :], rows[i], dist_rows[i]) > 0:
            to_pick.append(i)
    return to_pick


def get_unsolved_cols_idxs(cols, nonogram):
    """
        Returns indexes of columns which are not correct
    """
    to_pick = []
    for i in range(len(cols)):
        if opt_dist(nonogram[:, i], cols[i], dist_cols[i]) > 0:
            to_pick.append(i)
    return to_pick



def shuffle_nonogram(row_size, col_size):
    return np.random.choice(['0', '1'], size=(row_size, col_size))


def opt_dist(xs, D, mem):
    """
    Idea is to generate all possible len(D) sequences of '1' with length D[x] and XOR them with original list xs then number of
    '1' in this output by the definition of XOR gives us number of needed changes, then we just take minimum.
    """
    if len(D) == 1:

        min_swaps = len(xs)
        sequence_of_ones = ['1' if i < D[0] else '0' for i in range(0, len(xs))]

        if D[0] == 0:
            return num_of_ones(xor_ls_of_chr(xs, sequence_of_ones))

        while sequence_of_ones[len(sequence_of_ones) - 1] != '1':
            candidate_min = num_of_ones(xor_ls_of_chr(xs, sequence_of_ones))
            min_swaps = min(min_swaps, candidate_min)
            sequence_of_ones.pop()
            sequence_of_ones.insert(0, '0')

        candidate_min = num_of_ones(xor_ls_of_chr(xs, sequence_of_ones))
        min_swaps = min(min_swaps, candidate_min)
    else:
        min_swaps = len(xs)
        for sequence in mem:
            if len(xs) != len(sequence):
                for i in sequence:
                    candidate_min = num_of_ones(xor_ls_of_chr(xs, i))
                    min_swaps = min(min_swaps, candidate_min)
            else:
                candidate_min = num_of_ones(xor_ls_of_chr(xs, sequence))
                min_swaps = min(min_swaps, candidate_min)
            if min_swaps == 0:
                return min_swaps
    return min_swaps


def calc_dists(desc):
    result = [[] for i in range(len(desc))]
    for i in range(len(desc)):
        result[i].append(possible_sequences(desc[i], len(desc)))
    return result


def possible_sequences(desc, max_len):
    return possible_sequences_rec(desc, [], max_len)


def possible_sequences_rec(desc, already_set, max_len):
    result = [x for x in possible_seq(already_set.copy(), desc[0], desc[1:], max_len)]
    if not desc[1:]:
        return result
    else:
        new_res = []
        for s in result:
            for x in possible_sequences_rec(desc[1:], s.copy(), max_len):
                new_res.append(x)
        return new_res


def possible_seq(already_setted, current, remaining, max_len):
    if already_setted:
        if already_setted[len(already_setted)-1] == '1':
            already_setted.append('0')
    left_bound = len(already_setted)
    right_bound = max_len
    for x in remaining:
        right_bound -= x
        right_bound -= 1
    while left_bound + current <= right_bound:
        new = already_setted.copy()
        for i in range(current):
            new.append('1')
        if not remaining:
            left = left_bound + current
            while left < right_bound:
                new.append('0')
                left += 1
        yield new
        already_setted.append('0')
        left_bound += 1


def xor_ls_of_chr(x1, x2):
    """
    XOR on two lists of chars {'0', '1'}
    """
    assert (len(x1) == len(x2))
    return ['1' if x1[i] != x2[i] else '0' for i in range(len(x1))]


def num_of_ones(xs):
    """
    Count number of '1' in list xs
    """
    n = 0
    for x in xs:
        if x == '1':
            n += 1
    return n


if __name__ == '__main__':
    if DEBUG:
        # .##.##.....####
        pass
    else:
        with open('zad_input.txt', 'r') as r:
            with open('zad_output.txt', 'w') as w:
                while True:
                    line = r.readline()
                    if not line:
                        break
                    rows_num = int(line.split()[0])
                    cols_num = int(line.split()[1])
                    rows_ls = []
                    cols_ls = []
                    for x in range(rows_num):
                        c = r.readline()
                        c = c.split()
                        ints_list = [int(i) for i in c]
                        rows_ls.append(ints_list)
                    for y in range(cols_num):
                        c = r.readline()
                        c = c.split()
                        ints_list = [int(i) for i in c]
                        cols_ls.append(ints_list)
                    print("Solving ...")
                    result = solve(rows_ls, cols_ls)

                    for x in range(rows_num):
                        for y in range(cols_num):
                            w.write('#' if result[x][y] == '1' else '.')
                        w.write('\n')