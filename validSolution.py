def valid_solution(board):
    # Check for incomplete
    for rows in board: 
        if 0 in rows:
            return False
    
    # check rows
    for row in board:
        for x in range(1,10):
            if x not in row:
                print('rows')
                return False
    
    # check columns
    for col in [[row[i] for row in board] for i in range(len(board))]:        
        for x in range(1,10):
            if x not in col:
                print('columns')
                return False
    
    # check squares
    # for square in [     ]
    squares = [[] for _ in range(len(board))]
    for square in range(9):
        a = (square // 3) * 3 # 0,0,0 -> 3,3,3 -> 6,6,6
        b = (square % 3) * 3 #(0 -> 3 -> 6) 
        for x in range(a, a + 3):
            for y in range(b, b + 3):
                squares[square].append(board[x][y])
    print (squares)
    for row in squares:
        for x in range(1,10):
            if x not in row:
                print('squares')
                return False
    return True
        
            
solFalse = [
  [5, 3, 4, 6, 7, 8, 9, 1, 2], 
  [6, 7, 2, 1, 9, 0, 3, 4, 8],
  [1, 0, 0, 3, 4, 2, 5, 6, 0],
  [8, 5, 9, 7, 6, 1, 0, 2, 0],
  [4, 2, 6, 8, 5, 3, 7, 9, 1],
  [7, 1, 3, 9, 2, 4, 8, 5, 6],
  [9, 0, 1, 5, 3, 7, 2, 1, 4],
  [2, 8, 7, 4, 1, 9, 6, 3, 5],
  [3, 0, 0, 4, 8, 1, 1, 7, 9]
]
solTrue = [
  [5, 3, 4, 6, 7, 8, 9, 1, 2],
  [6, 7, 2, 1, 9, 5, 3, 4, 8],
  [1, 9, 8, 3, 4, 2, 5, 6, 7],
  [8, 5, 9, 7, 6, 1, 4, 2, 3],
  [4, 2, 6, 8, 5, 3, 7, 9, 1],
  [7, 1, 3, 9, 2, 4, 8, 5, 6],
  [9, 6, 1, 5, 3, 7, 2, 8, 4],
  [2, 8, 7, 4, 1, 9, 6, 3, 5],
  [3, 4, 5, 2, 8, 6, 1, 9, 7]
]
print(valid_solution(solTrue))