class Board():
    
    def __init__(self, size: int) -> None:
        self.size = size
        self.val = [[' ' for j in range(self.size)] for i in range(self.size)]

    def add_list(self, row: int, col: int, val: str) -> None:
        if self.val[row][col] == ' ':
            self.val[row][col] = val

    def get_column_label(self) -> str:
        result = '    '
        for col in range(self.size):
            result = result  + str(col) + '   '
        return result

    def print_board(self) -> None:
        print(self.get_column_label())

        for row in range(self.size):
            row_str = str(row) + ' | '
            separator ='  '

            for col in range(self.size):
                row_str = row_str + str(self.val[row][col]) + ' | '
                separator = separator + ' ---'

            print(separator)
            print(row_str)

        print()

    def evaluate_board(self, val):
        result = self.check_dirc('r', val, 0, self.size - 1)

        #TODO: check from other positions (bottom row, further right col)
        #TODO: check diagonal
        return result

    def check_dirc(self, direc: str, val: str, col: int, row: int, count: int = 0) -> bool:
        if count == self.size:
            return True
        elif col > self.size or col < 0 or self.val[row][col] != val:
            return False

        if direc == 'u':
            return self.check_dirc(direc, val, col, row - 1, count + 1)
        elif direc == 'r':
            return self.check_dirc(direc, val, col + 1, row, count + 1)
        elif direc == 'l':
            return self.check_dirc(direc, val, col - 1, row, count + 1)

            
 
myboard = Board(4)
myboard.add_list(3, 0, 'x')
myboard.add_list(3, 1, 'x')
myboard.add_list(3, 2, 'o')
myboard.add_list(3, 3, 'x')
myboard.print_board()

if myboard.evaluate_board('x') == True:
    print('you win')
else:
    print('you lose')