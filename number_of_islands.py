grid = [
    ["1","1","1","0","0"],
    ["0","1","0","0","0"],
    ["0","0","0","0","0"],
    ["0","0","0","0","0"]
]

def numIslands(grid):
    islands = 0
    
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == "1":
                islands += 1
                dfs(i, j, grid)
    return islands

def dfs(i, j, grid):
    if i < 0:
        return
    if j < 0:
        return
    if i >= len(grid):
        return
    if j >= len(grid[0]):
        return
    if grid[i][j] == "0":
        return

    else:
        grid[i][j] = "0"
        dfs(i, j + 1, grid)
        dfs(i, j - 1, grid)
        dfs(i + 1, j, grid)
        dfs(i - 1, j, grid)

print(numIslands(grid))