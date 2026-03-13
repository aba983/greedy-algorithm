class EightQueens:
    def __init__(self):
        self.solutions = []  # 存储所有解
        self.n = 8  # 8皇后
    
    def solve(self):
        """解决八皇后问题"""
        board = [-1] * self.n  # board[i]表示第i行的皇后在第几列
        self.backtrack(board, 0)
        return self.solutions
    
    def backtrack(self, board, row):
        """回溯法求解"""
        # 找到一个解
        if row == self.n:
            self.solutions.append(board.copy())
            return
        
        # 尝试在当前行的每一列放置皇后
        for col in range(self.n):
            if self.is_safe(board, row, col):
                board[row] = col  # 放置皇后
                self.backtrack(board, row + 1)  # 递归下一行
                board[row] = -1  # 回溯，移除皇后
    
    def is_safe(self, board, row, col):
        """检查在(row, col)位置放置皇后是否安全"""
        for prev_row in range(row):
            prev_col = board[prev_row]
            
            # 检查同一列
            if prev_col == col:
                return False
            
            # 检查对角线
            if abs(prev_row - row) == abs(prev_col - col):
                return False
        
        return True
    
    def print_solution(self, solution):
        """打印一个解"""
        print("-" * 20)
        for row in range(self.n):
            line = ""
            for col in range(self.n):
                if solution[row] == col:
                    line += "👑 "  # 皇后
                else:
                    line += "⬜ " if (row + col) % 2 == 0 else "⬛ "
            print(line)
        print("-" * 20)


# 使用示例
if __name__ == "__main__":
    queens = EightQueens()
    solutions = queens.solve()
    
    print(f"八皇后问题共有 {len(solutions)} 个解")
    print(f"前3个解示例：")
    
    for i in range(min(3, len(solutions))):
        print(f"\n解 {i + 1}:")
        queens.print_solution(solutions[i])