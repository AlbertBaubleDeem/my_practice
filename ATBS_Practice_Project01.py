grid = [['\xa0', '\xa0', '\xa0', '\xa0', '\xa0', '\xa0'],
        ['\xa0', 'O', 'O', '\xa0', '\xa0', '\xa0'],
        ['O', 'O', 'O', 'O', '\xa0', '\xa0'],
        ['O', 'O', 'O', 'O', 'O', '\xa0'],
        ['\xa0', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '\xa0'],
        ['O', 'O', 'O', 'O', '\xa0', '\xa0'],
        ['\xa0', 'O', 'O', '\xa0', '\xa0', '\xa0'],
        ['\xa0', '\xa0', '\xa0', '\xa0', '\xa0', '\xa0']]

# for j in range(len(grid[0])):
#     for i in range(len(grid)):
#         line = grid[i][j]
#         for k in range(len(line)):
#             print(line[k], sep='', end='')
#     print()

for symbol in range(len(grid[0])):
    for line in range(len(grid)):
            print(grid[line][symbol], sep='', end='')
    print()

# for j in range(len(grid[0])):
#     for i in range(len(grid)):    
#         for k in range(len(grid[i][j])):
#             print(grid[i][j][k], sep='', end='')
#     print()
