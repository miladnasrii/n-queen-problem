def is_safe(board, row, col):
    for i in range(col):
        if board[i] == row or board[i] - i == row - col or board[i] + i == row + col:
            return False
    return True

def solution(n, col, board, results):
    if col == n:
        results.append(board[:])  
        return
    for row in range(n):
        if is_safe(board, row, col): 
            board[col] = row  
            solution(n, col + 1, board, results)  

def solution_n_queens(n):
    results = []
    solution(n, 0, [-1] * n, results)  
    if results == []:
        print("There is no solution!")
    return results

N = int(input("Enter the number of queens : "))
solutions = solution_n_queens(N)  
for solution in solutions:  
    for row in solution:  
        line = ["0"] * N 
        line[row] = "1"  
        print(" ".join(line)) 
    print()