# задание 1

class Matrix:
    def __init__(self, input_data):
        self.input_data = input_data

    def __str__(self):
        return '\n'.join([' '.join(map(str, line)) for line in self.input_data])

    def __add__(self, other):
        answer = ''
        if len(self.input_data) == len(other.input_data):
            for line_1, line_2 in zip (self.input_data, other.input_data):
                if len(line_1) != len(line_2):
                    return 'wrong shape of matrix'

                summ_line = [x + y for x, y in zip(line_1, line_2)]
                answer += ' '.join(map(str, summ_line)) + '\n'
        else:
            return 'wrong shape of matrix'
        return answer


matrix_1 = Matrix([[1, 2], [3, 4], [5, 6]])
matrix_2 = Matrix([[7, 8], [9, 10], [11, 12]])
print(matrix_1 + matrix_2)


# задание 2
from abc import ABC, abstractmethod


class Clothes(ABC):
    def __init__(self, par):
        self.par = par

    @abstractmethod
    def calculate(self):
        pass


class Coat(Clothes):

    @property
    def calculate(self):
        return round(self.par / 6.5 + 0.5, 2)


class Suit(Clothes):

    @property
    def calculate(self):
        return round(2 * self.par + 0.3, 2)


coat = Coat(165)
suit = Suit(165)
print(coat.calculate)
print(suit.calculate)
print('\n')


# задание 3


class Cell:
    def __init__(self, nums):
        self.nums = nums

    def __add__(self, other):
        return Cell(self.nums + other.nums)

    def __sub__(self, other):
        return Cell(self.nums - other.nums) if self.nums - other.nums > 0 \
            else 'XXX'

    def __mul__(self, other):
        return Cell(self.nums * other.nums)

    def __truediv__(self, other):
        return Cell(self.nums / other.nums)

    def make_order(self, rows):
        return '\n'.join(['*' * rows for _ in range(self.nums // rows)]) \
                + '\n' + '*' * (self.nums % rows)

    def __str__(self):
        return str(self.nums)


cell_1 = Cell(25)
print(cell_1.make_order(10))
cell_2 = Cell(5)
print(cell_1 + cell_2)
print(cell_1 - cell_2)
print(cell_1 * cell_2)
print(cell_1 / cell_2)
