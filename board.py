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

    def evaluate_board(self, val: str) -> bool:
        # check diagonals
        if self.check_dirc('dr', val, 0, self.size - 1):
            return True

        if self.check_dirc('dl', val, self.size -1, self.size -1):
            return True

        for i in range(self.size):
            # check up from bottom row
            if self.check_dirc('u', val, i, self.size - 1):
                return True

            # check to the left from right column
            if self.check_dirc('l', val, self.size - 1, i):
                return True

        return False

    def check_dirc(self, direc: str, val: str, col: int, row: int, count: int = 0) -> bool:
        if count == self.size:
            return True
        elif col > self.size or col < 0 or self.val[row][col] != val:
            return False

        if direc == 'u':
            return self.check_dirc(direc, val, col, row - 1, count + 1)
        elif direc == 'l':
            return self.check_dirc(direc, val, col - 1, row, count + 1)
        elif direc == 'dr':
            return self.check_dirc(direc, val, col + 1, row - 1, count + 1)
        elif direc == 'dl':
            return self.check_dirc(direc, val, col - 1, row - 1, count + 1)

            
 


    