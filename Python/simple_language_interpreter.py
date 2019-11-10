from abc import ABC, abstractmethod
from expression import *


class Program(ABC):
    def __init__(self):
        self.indent = ""

    def set_indent(self, indent):
        self.indent = indent

    @abstractmethod
    def evaluate(self, variables):
        pass

    @abstractmethod
    def __str__(self):
        pass


class Block(Program):
    def __init__(self, instructions):
        super().__init__()
        self.instructions = instructions

    def set_indent(self, indent):
        for i in self.instructions:
            i.set_indent(indent)

    def evaluate(self, variables):
        for i in self.instructions:
            i.evaluate(variables)

    def __str__(self):
        res = ""
        for i in self.instructions:
            res += str(i) + "\n"
        return res


class IfInstruction(Program):
    def __init__(self, condition, true_program, false_program):
        super().__init__()
        self.condition = condition
        self.true_program = true_program
        self.true_program.set_indent(self.indent + "   ")
        self.false_program = false_program
        self.false_program.set_indent(self.indent + "   ")

    def set_indent(self, indent):
        self.indent = indent
        self.true_program.set_indent(indent + "   ")
        self.false_program.set_indent(indent + "   ")

    def evaluate(self, variables):
        if not self.condition.count(variables) == 0:
            self.true_program.evaluate(variables)
        else:
            self.false_program.evaluate(variables)

    def __str__(self):
        return (self.indent + "if " + str(self.condition) + ":\n" + str(self.true_program)
                + "\n" + self.indent + "else\n" + str(self.false_program))


class ForInstruction(Program):
    def __init__(self, start, end_condition, iterator, body_program):
        super().__init__()
        self.start = start
        self.end_condition = end_condition
        self.iterator = iterator
        self.body_program = body_program
        self.body_program.set_indent(self.indent + "   ")

    def evaluate(self, variables):
        self.start.evaluate(variables)
        while self.end_condition.count(variables) != 0:
            self.body_program.evaluate(variables)
            self.iterator.evaluate(variables)

    def __str__(self):
        return (self.indent + "for " + str(self.start)) + "; " + str(self.end_condition) + "; " + str(self.iterator) \
            + ": \n" + str(self.body_program)


class Assign(Program):
    def __init__(self, var, value):
        super().__init__()
        self.var = var
        self.value = value

    def evaluate(self, variables):
        variables.update({str(self.var): self.value.count(variables)})

    def __str__(self):
        return self.indent + str(self.var) + " := " + str(self.value)


test = ForInstruction(Assign(Variable("i"), Const(0)), LesserThan(Variable("i"), Const(10)), Assign(Variable("i"), Add(Variable("i"), Const(1))), Assign(Variable("sum"), Multiply(Const(2), Variable("i"))))

fib_env = {}
n = 10

fibonacci = Block([
    Assign(Variable("n"), Const(n)),
    Assign(Variable("prev"), Const(0)),
    Assign(Variable("current"), Const(1)),
    ForInstruction(Assign(Variable("i"), Const(1)),
                   LesserThan(Variable("i"), Variable("n")),
                   Assign(Variable("i"), Add(Variable("i"), Const(1))),
                   Block([
                       Assign(Variable("temp"), Variable("current")),
                       Assign(Variable("current"), Add(Variable("prev"), Variable("current"))),
                       Assign(Variable("prev"), Variable("temp"))
                   ])
                   )
])

# fibonacci.evaluate(fib_env)
# print(str(fibonacci))
# print(fib_env)

prime_candidate = 376

prime_checker = Block([
    Assign(Variable("n"), Const(prime_candidate)),
    Assign(Variable("result"), Const(1)),
    ForInstruction(Assign(Variable("i"), Const(2)),
                   LesserThan(Multiply(Variable("i"), Variable("i")), Variable("n")),
                   Assign(Variable("i"), Add(Variable("i"), Const(1))),
                   IfInstruction(Equal(Modulo(Variable("n"), Variable("i")), Const(0)),
                                 Assign(Variable("result"), Const(0)),
                                 Block([])))
])

print(str(prime_checker))

prime_env = {}
prime_checker.evaluate(prime_env)

print(prime_env)