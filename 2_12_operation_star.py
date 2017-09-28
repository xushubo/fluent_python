my_list = [[]] + [[]] + [[]]
print(my_list)
my_list[0].append(1)
my_list[1].append(1)
print(my_list)
print('-----------------')

my_list1 = [[]] * 3
print(my_list1)
my_list1[0].append(1)
my_list1[1].append(1)
print(my_list1)
print('-----------------')

board = [['_'] * 3 for i in range(3)]
print(board)
board[1][2] = 'X'
print(board)
print('-----------------')

board1 = [['_'] * 3] * 3
print(board1)
board1[1][2] = 'X'
print(board1)
print('-----------------')

row = ['_'] * 3
board2  = []
for i in range(3):
    board2.append(row)
print(board2)
board2[1][2] = 'X'
print(board2)
print('-----------------')

board3 = []
for i in range(3):
    row = ['_'] * 3
    board3.append(row)
print(board3)
board3[1][2] = 'X'
print(board3)