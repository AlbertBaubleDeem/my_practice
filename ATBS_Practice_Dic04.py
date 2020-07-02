#! /usr/bin/python3

def printBoard(board_dic):
    print(board_dic['top-L'] + '|' + board_dic['top-M'] + '|' + board_dic['top-R'])
    print('-+-+-')
    print(board_dic['mid-L'] + '|' + board_dic['mid-M'] + '|' + board_dic['mid-R'])
    print('-+-+-')
    print(board_dic['low-L'] + '|' + board_dic['low-M'] + '|' + board_dic['low-R'])

board_dic = {
'top-L': ' ','top-M': ' ','top-R': ' ',
'mid-L': ' ','mid-M': ' ','mid-R': ' ',
'low-L': ' ','low-M': ' ','low-R': ' ',
}

turn = 'X'
for i in range(9):
    printBoard(board_dic)
    print('Turn for ' + turn + '.  Move on which space?')
    move = input()
    board_dic[move] = turn
    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'

printBoard(board_dic)