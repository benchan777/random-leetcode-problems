grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]

def numIslands(grid):
  counter = 0

  for i in range(len(grid)):
    for j in range(len(grid[0])):
      if grid[i][j] == '1':
        counter += 1
        dfs_iterative(grid, i, j)
  print(counter)
  return counter

def dfs_iterative(grid, row, column):
  length = len(grid)
  width = len(grid[0])
  stack = []
  visited = []

  stack.append((row, column))

  while stack:
    coordinates = stack.pop(0)
    row = coordinates[0]
    column = coordinates[1]
  
    grid[coordinates[0]][coordinates[1]] = '0'
    visited.append(coordinates)

    if column + 1 < width: # check right hand bounds
      tuple = (row, column + 1)
      if tuple not in visited and grid[tuple[0]][tuple[1]] == '1':
        stack.insert(0, tuple)
    if column - 1 >= 0: # check left hand bounds
      tuple = (row, column - 1)
      if tuple not in visited and grid[tuple[0]][tuple[1]] == '1':
        stack.insert(0, tuple)
    if row - 1 >= 0: # check upper bounds
      tuple = (row - 1, column)
      if tuple not in visited and grid[tuple[0]][tuple[1]] == '1':
        stack.insert(0, tuple)
    if row + 1 < length: # check lower bounds
      tuple = (row + 1, column)
      if tuple not in visited and grid[tuple[0]][tuple[1]] == '1':
        stack.insert(0, tuple)

numIslands(grid)