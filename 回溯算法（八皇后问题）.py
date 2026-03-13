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



'''------优化版本-------'''
from typing import List, Generator

class EightQueens:
    def __init__(self, n: int = 8):
        self.n = n
        self.solutions = []

    def solve(self) -> List[List[int]]:
        """主入口：使用位运算递归求解"""
        self.solutions = []
        # 参数含义：行号, 列限制, 左对角线限制, 右对角线限制, 当前已放位置
        self._backtrack_bits(0, 0, 0, 0, [])
        return self.solutions

    def _backtrack_bits(self, row: int, col_mask: int, ld_mask: int, rd_mask: int, current_board: List[int]):
        """位运算核心逻辑"""
        if row == self.n:
            self.solutions.append(current_board)
            return

        # 1. 计算当前行哪些位置是安全的（1表示可以放置）
        # (col_mask | ld_mask | rd_mask) 得到被攻击的位置，取反并限制在 n 位内
        safe_bits = (~(col_mask | ld_mask | rd_mask)) & ((1 << self.n) - 1)

        while safe_bits:
            # 2. 提取最右边的 1（即选择一个安全位）
            p = safe_bits & -safe_bits
            
            # 3. 计算这个 1 对应的是第几列
            col = (p).bit_length() - 1
            
            # 4. 递归到下一行
            # ld_mask | p 后左移一位代表左对角线攻击范围向下延伸
            # rd_mask | p 后右移一位代表右对角线攻击范围向下延伸
            self._backtrack_bits(
                row + 1,
                col_mask | p,
                (ld_mask | p) << 1,
                (rd_mask | p) >> 1,
                current_board + [col]
            )
            
            # 5. 将该位置零（回溯），尝试下一个 safe_bit
            safe_bits &= safe_bits - 1

    def print_solution(self, solution: List[int]):
        """美化打印：渲染棋盘图形"""
        print(f"\n" + " ✨ " * self.n)
        for r in range(self.n):
            line = []
            for c in range(self.n):
                if solution[r] == c:
                    line.append("👑")  # 皇后
                else:
                    # 棋盘格交替颜色
                    line.append("⬜" if (r + c) % 2 == 0 else "⬛")
            print(" ".join(line))
        print(" ✨ " * self.n)

# 测试运行
if __name__ == "__main__":
    n = 8
    game = EightQueens(n)
    all_solutions = game.solve()

    print(f"✅ 计算完成！{n} 皇后问题共有 {len(all_solutions)} 个解。")
    
    # 打印前 2 个解作为示例
    for i in range(min(2, len(all_solutions))):
        print(f"\n📍 解法 {i + 1}:")
        game.print_solution(all_solutions[i])