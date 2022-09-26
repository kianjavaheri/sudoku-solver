class Solution:
    def solveSudoku(self, board: list[list[str]]) -> None:
        self.solve(board)

    def solve(self, board):
        find = self.find_empty(board)
        if not find:
            return True
        row, col = find

        for i in range(1, 10):
            if self.valid(board, i, find):
                board[row][col] = i

                if self.solveSudoku(board):
                    return True

                board[row][col] = 0
        return False

    def find_empty(self, board):
        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == 0:
                    return (row, col)

        return None

    def valid(self, board, num, pos):
        row, col = pos # unpack tuple

        # checks horizontally
        for i in range(len(board[0])):
            if board[row][i] == num and not i == col:
                return False

        # checks vertically
        for i in range(len(board)):
            if board[i][col] == num and not i == row:
                return False

        # checks box
        box_row = col // 3
        box_col = row // 3
        for i in range(box_col * 3, box_col + 3):
            for j in range(box_row * 3, box_row + 3):
                if board[i][j] == num and not (i, j) == pos:
                    return False

        return True

def print_board(bo):
    for i in range(len(bo)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - ")

        for j in range(len(bo[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(bo[i][j])
            else:
                print(str(bo[i][j]) + " ", end="")

def main():
    board = [
        [7,8,0,4,0,0,1,2,0],
        [6,0,0,0,7,5,0,0,9],
        [0,0,0,6,0,1,0,7,8],
        [0,0,7,0,4,0,2,6,0],
        [0,0,1,0,5,0,9,3,0],
        [9,0,4,0,6,0,0,0,5],
        [0,7,0,3,0,0,0,1,2],
        [1,2,0,0,0,7,4,0,0],
        [0,4,9,2,0,6,0,0,7]
    ]

    sol = Solution()
    sol.solveSudoku(board)

    print_board(board)


if __name__ == "__main__":
    main()