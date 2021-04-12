import board
import random

class TestWin():
    def __init__(self, size):
        self.size = size

    def testCase(self, values, max_moves):
        my_board = board.Board(self.size)
        for i in range(0, max_moves*2, 2):
            my_board.add_list(values[i], values[i + 1], 'x')

        my_board.print_board()
        if my_board.evaluate_board('x') == True:
            print('you win')
        else:
            print('you lose')
        
def test3():
    test = TestWin(3)

    # (1) diagonal right to left
    test1 = [0, 2, 1, 1, 2, 0]
    test.testCase(test1, 3)

    # (2) diagonal left to right
    test2 = [0, 0, 1, 1, 2, 2]
    test.testCase(test2, 3)

    #(3) left 0
    test3 = [0, 2, 0, 1, 0, 0]
    test.testCase(test3, 3)

    #(4) left 1
    test4 = [1, 2, 1, 1, 1, 0]
    test.testCase(test4, 3)

    #(5) left 2
    test5 = [2, 2, 2, 1, 2, 0]
    test.testCase(test5, 3)

    #(6) up 0
    test6 = [0, 0, 1, 0, 2, 0]
    test.testCase(test6, 3)

    #(7) up 1
    test7 = [0, 1, 1, 1, 2, 1]
    test.testCase(test7, 3)

    #(8) up 2
    test8 = [0, 2, 1, 2, 2, 2]
    test.testCase(test8, 3)

def test3Rand():
    position = []
    for i in range(10):
        position.append(random.randint(0, 2))

    test = TestWin(3)
    test.testCase(position, 5)

def test4Rand():
    position = []
    for i in range(18):
        position.append(random.randint(0, 3))

    test = TestWin(4)
    test.testCase(position, 9)

test3()
test3Rand()
test4Rand()