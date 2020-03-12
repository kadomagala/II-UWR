

def opt_dist(xs, D):
    """
    Idea is to generate all possible sequences of '1' with length D and XOR them with original list xs then number of
    '1' in this output by the definition of XOR gives us number of needed changes, then we just take minimum.
    """
    min_swaps = len(xs)
    sequence_of_ones = ['1' if i < D else '0' for i in range(0, len(xs))]

    if D == 0:
        return num_of_ones(xor_ls_of_chr(xs, sequence_of_ones))

    while sequence_of_ones[len(sequence_of_ones) - 1] != '1':
        candidate_min = num_of_ones(xor_ls_of_chr(xs, sequence_of_ones))
        min_swaps = min(min_swaps, candidate_min)
        sequence_of_ones.pop()
        sequence_of_ones.insert(0, '0')

    candidate_min = num_of_ones(xor_ls_of_chr(xs, sequence_of_ones))
    min_swaps = min(min_swaps, candidate_min)

    return min_swaps


def xor_ls_of_chr(x1, x2):
    """
    XOR on two lists of chars {'0', '1'}
    """
    assert (len(x1) == len(x2))
    return ['1' if x1[i] != x2[i] else '0' for i in range(0, len(x1))]


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
    with open('zad4_input.txt', 'r') as r:
        with open('zad4_output.txt', 'w') as w:
            for line in r:
                s = line.split()
                w.write(str(opt_dist(list(s[0]), int(s[1]))))
                w.write('\n')
