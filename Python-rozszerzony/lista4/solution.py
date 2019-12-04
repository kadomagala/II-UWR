import itertools
import timeit
from prettytable import PrettyTable


# zadanie 1
def is_prime(num):
    i = 2
    if num <= 2:
        return False
    while i * i <= num:
        if num % i == 0:
            return False
        i += 1
    return True


def primes_iterative(n):
    result = []
    for i in range(1, n):
        if is_prime(i):
            result.append(i)
    return result


def primes_comprehension(n):
    return [x for x in range(1, n) if is_prime(x)]


def primes_functional(n):
    # result = [x for x in range(1, n)]
    result = filter(is_prime, range(1, n))
    return list(result)


def primes_iter():
    cur = 3
    yield 2
    while True:
        if is_prime(cur):
            yield cur
        cur += 2


def primes_iterator(n):
    return list(itertools.takewhile(lambda x: x < n, primes_iter()))


def zad1_test():
    tab = PrettyTable()
    tab.field_names = ["", "imperative", "functional", "comprehension", "iterator"]
    args = [10, 100, 1000]
    for arg in args:
        setup = "arg = " + str(arg) + ""
        tab.add_row(
            [str(arg), timeit.timeit('res = primes_iterative(arg)', setup=setup, number=1000, globals=globals()),
             timeit.timeit('res = primes_functional(arg)', setup=setup, number=1000, globals=globals()),
             timeit.timeit('res = primes_comprehension(arg)', setup=setup, number=1000, globals=globals()),
             timeit.timeit('res = primes_iterator(arg)', setup=setup, number=1000, globals=globals())])
    print(tab)


def is_perfect_number(num):
    divisors = []
    for i in range(1, num):
        if num % i == 0:
            divisors.append(i)
    return sum(divisors) == num


def perfects_iterative(n):
    result = []
    for i in range(1, n):
        if is_perfect_number(i):
            result.append(i)
    return result


def perfects_compose(n):
    return [x for x in range(1, n) if is_perfect_number(x)]


def perfects_functional(n):
    return list(filter(is_perfect_number, range(1, n)))


def test_zad2():
    tab = PrettyTable()
    tab.field_names = ["", "imperative", "functional", "compose"]
    args = [10, 100, 1000]
    for arg in args:
        setup = "arg = " + str(arg) + ""
        tab.add_row(
            [str(arg), timeit.timeit('res = perfects_iterative(arg)', setup=setup, number=10, globals=globals()),
             timeit.timeit('res = perfects_functional(arg)', setup=setup, number=10, globals=globals()),
             timeit.timeit('res = perfects_compose(arg)', setup=setup, number=10, globals=globals())])
    print(tab)


if __name__ == "__main__":
    #zad1_test()
    test_zad2()