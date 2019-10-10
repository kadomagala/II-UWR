from abc import ABC, abstractmethod


class Expression(ABC):
    @abstractmethod
    def count(self, variables):
        pass

    @abstractmethod
    def __str__(self):
        pass


class Const(Expression):
    def __init__(self, value):
        if not isinstance(value, int) and not isinstance(value, float):
            raise InvalidValueAssignment
        self.value = value

    def count(self, variables):
        return self.value

    def __str__(self):
        return str(self.value)


class Variable(Expression):
    def __init__(self, variable):
        self.variable = variable

    def count(self, variables):
        value_of_var = variables.get(self.variable)
        if value_of_var is None:
            raise VariableNotFoundException
        if not isinstance(value_of_var, int) and not isinstance(value_of_var, float):
            raise InvalidValueAssignment
        return value_of_var

    def __str__(self):
        return str(self.variable)


class DoubleArgExpression(Expression):
    def __init__(self, left_expr, right_expr):
        self.left_expr = left_expr
        self.right_expr = right_expr

    def count(self, variables):
        pass

    def __str__(self):
        pass


class Add(DoubleArgExpression):
    def count(self, variables):
        return self.left_expr.count(variables) + self.right_expr.count(variables)

    def __str__(self):
        return "(" + str(self.left_expr) + " + " + str(self.right_expr) + ")"


class Subtract(DoubleArgExpression):
    def count(self, variables):
        return self.left_expr.count(variables) - self.right_expr.count(variables)

    def __str__(self):
        return "(" + str(self.left_expr) + " - " + str(self.right_expr) + ")"


class Multiply(DoubleArgExpression):
    def count(self, variables):
        return self.left_expr.count(variables) * self.right_expr.count(variables)

    def __str__(self):
        return "(" + str(self.left_expr) + " * " + str(self.right_expr) + ")"


class Modulo(DoubleArgExpression):
    def count(self, variables):
        return self.left_expr.count(variables) % self.right_expr.count(variables)

    def __str__(self):
        return "(" + str(self.left_expr) + " % " + str(self.right_expr) + ")"


class Divide(DoubleArgExpression):
    def count(self, variables):
        right_value = self.right_expr.count(variables)
        if right_value == 0:
            raise DivideByZeroException
        return self.left_expr.count(variables) / right_value

    def __str__(self):
        return "(" + str(self.left_expr) + " / " + str(self.right_expr) + ")"


class GreaterThan(DoubleArgExpression):
    def count(self, variables):
        if self.left_expr.count(variables) > self.right_expr.count(variables):
            return 1
        else:
            return 0

    def __str__(self):
        return str(self.left_expr) + " > " + str(self.right_expr)


class LesserThan(DoubleArgExpression):
    def count(self, variables):
        if self.left_expr.count(variables) < self.right_expr.count(variables):
            return 1
        else:
            return 0

    def __str__(self):
        return str(self.left_expr) + " < " + str(self.right_expr)


class Equal(DoubleArgExpression):
    def count(self, variables):
        if self.left_expr.count(variables) == self.right_expr.count(variables):
            return 1
        else:
            return 0

    def __str__(self):
        return str(self.left_expr) + " == " + str(self.right_expr)


class ExpressionException(Exception):
    pass


class DivideByZeroException(ExpressionException):
    pass


class VariableNotFoundException(ExpressionException):
    pass


class InvalidValueAssignment(ExpressionException):
    pass


