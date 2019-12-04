from itertools import permutations


class Cryptarithm():
    def __init__(self, first_arg, sec_arg, res):
        self.first_arg = first_arg
        self.sec_arg = sec_arg
        self.res = res
        self.first_sol = ""
        self.sec_sol = ""
        self.res_sol = ""

    def __str__(self):
        form = "{:>1} {:>" + str(len(self.res)) + "}"
        res = form.format("", self.first_arg) + "\n" + form.format("+", self.sec_arg) \
              + "\n" + form.format("", self.res)
        return res

    def get_solution(self):
        form = "{:>1} {:>" + str(len(self.res)) + "}"
        return form.format("", self.first_sol) + "\n" + form.format("+", self.sec_sol) + "\n" \
              + form.format("", self.res_sol)

    def solve(self):
        letters = set(self.first_arg) | set(self.sec_arg) | set(self.res)

        letters = list(letters)

        perms = permutations([x for x in range(0, 10)], len(letters))
        for p in perms:
            if self.is_solution(p, letters):
                break

    def is_solution(self, permutation, letters):
        dic = dict()
        for i in range(0, len(permutation)):
            dic[letters[i]] = permutation[i]

        self.first_sol = ""
        self.sec_sol = ""
        self.res_sol = ""

        if dic[self.first_arg[0]] == 0 or dic[self.sec_arg[0]] == 0 or dic[self.res[0]] == 0:
            return False

        self.first_sol = "".join([str(dic[ch]) for ch in self.first_arg])
        for ch in self.sec_arg:
            self.sec_sol += str(dic[ch])
        for ch in self.res:
            self.res_sol += str(dic[ch])

        return int(self.first_sol) + int(self.sec_sol) == int(self.res_sol)


if __name__ == "__main__":
    cr = Cryptarithm("KIOTO", "OSAKA", "TOKIO")
    print(cr)
    print("")
    cr.solve()
    print(cr.get_solution())
