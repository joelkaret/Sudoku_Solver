import copy
import time



class Main:
    def __init__(self, board) -> None:
        self.board = board
        self.current = copy.deepcopy(board)
        self.column = 0
        self.row = 0
        self.solutions = 1
        self.stop = True #Set to false if you do not want it pause after 10 solutions.
        self.start = time.time()
        self.since_last = time.time()
        self.average = []

    def check(self):
        normal = self.current
        transposed = self.transpose_board()
        three_by_three = self.three_by_three()
        if self.mini_check(normal) and self.mini_check(transposed) and self.mini_check(three_by_three):
            if self.check_original() and self.current[self.row][self.column] != 0:
                return True
        return False
    
    def mini_check(self, array):
        for i in array:
            for j in range(len(i)):
                for k in range(j+1,9):
                    if i[j] == i[k] and i[j] != 0:
                        return False
        return True

    def check_original(self):
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                if self.board[i][j] != self.current[i][j] and self.board[i][j] != 0:
                    return False
        return True

    def no_zeros(self):
        for i in range(len(self.current)-1,-1,-1):
            for j in range(len(self.current[i])-1,-1,-1):
                if self.current[i][j] == 0:
                    return False
        return True

    def display_board(self, board):
        counter = 0
        for i in board:
            if counter % 3 == 0 and counter != 0:
                print('-'*21)
            counter2 = -2
            for j in i[:-1]:
                print(j, end='|')
                if counter2 % 3 == 0:
                    print(' |', end = '')
                counter2 += 1
            print(i[-1])
            counter += 1
    
    def transpose_board(self):
        transposed = []
        for i in range(len(self.current)):
            temp_transposed_row = []
            for j in range(len(self.board[i])):
                temp_transposed_row.append(self.current[j][i])
            transposed.append(temp_transposed_row)
        return transposed

    def three_by_three(self):
        transposed = []
        for i in range(0,9,3):
            for j in range(0,9,3):
                temp_transposed_box = []
                for k in range(0,3):
                    for l in range(0,3):
                        temp_transposed_box.append(self.current[k+i][l+j])
                transposed.append(temp_transposed_box)
        return transposed
    
    def solve(self):
        if self.check():
            if self.no_zeros():
                self.complete()
            else:
                self.next_cage()
        elif self.board[self.row][self.column] != 0:
            self.next_cage()
        else:
            self.next_number()

    def next_cage(self):
        if self.column == 8:
            self.column = 0
            if self.row == 8:
                self.previous_cage()
            else:
                self.row += 1
        else:
            self.column += 1
    
    def next_number(self):
        if self.current[self.row][self.column] == 9:
            self.previous_number()
        else:
            self.current[self.row][self.column] += 1

    def previous_cage(self):
        if self.column == 0:
            self.column = 8
            if self.row == 0:
                self.failed()
            else:
                self.row -= 1
        else:
            self.column -= 1
        if self.board[self.row][self.column] != 0:
            self.previous_cage()

    def previous_number(self):
        self.current[self.row][self.column] = 0
        self.previous_cage()
        self.next_number()

    def complete(self):
        if self.solutions == 1:
            print('\nOriginal board: \n')
            self.display_board(self.board)
            print('\n','-'*50, sep = '')
            print('\nCompleted Solution 1')
            print(f'Found In: {time.time() - self.start} seconds\n')
            self.average.append(time.time()-self.start)
            self.since_last = time.time()
            self.display_board(self.current)
            self.solutions += 1
            self.next_number()
        elif self.solutions < 11:
            print('\n','-'*50, sep = '')
            print(f'\nCompleted Solution {self.solutions}')
            print(f'Found In: {time.time() - self.start} seconds')
            print(f'Since last solution: {time.time() - self.since_last} seconds')
            self.average.append(time.time()-self.since_last)
            print(f'Average time per solution = {sum(self.average)/len(self.average)} seconds\n')
            self.since_last = time.time()
            self.display_board(self.current)
            self.solutions += 1
            self.next_number()
        elif self.stop:
            print('\n','-'*50, sep = '')
            print("\nThere are more than 10 solutions.")
            a = 'ok'
            start = time.time()
            while a != 'y' and a != 'n':
                a = input("Would you like to stop outputing?(Y/N):\n").lower()
            if a == 'y':
                exit()
            else:
                end = time.time()
                user_wasted = end - start
                print(f'User Paused for {user_wasted} seconds')
                self.start += user_wasted
                self.since_last += user_wasted
                self.stop = False
        else:
            print('\n','-'*50, sep = '')
            print(f"\nCompleted Solution {self.solutions}")
            print(f'Found In: {time.time() - self.start} seconds')
            print(f'Since last solution: {time.time() - self.since_last} seconds')
            self.average.append(time.time()-self.since_last)
            print(f'Average time per solution = {sum(self.average)/len(self.average)} seconds\n')
            self.since_last = time.time()
            self.display_board(self.current)
            self.solutions += 1
            self.next_number()

    def failed(self):
        if self.solutions == 1:
            print("Original board: ")
            self.display_board(self.board)
            print("There are no solutions to this sudoku.\n")
            exit()
        print("No more solutions.")
        print(f'Total Time Elapsed: {time.time() - self.start} seconds')
        print(f'Since last solution: {time.time() - self.since_last} seconds\n')
        exit()

    def run(self):
        while True:
            self.solve()


    
    # def testing1234(self):
    #     print(self.board[0][0]) #prints 0
    #     self.current[0][0] = 5
    #     print(self.board[0][0]) #prints 5

### 1-9, completed
# board = [   [1,2,3,4,5,6,7,8,9],
#             [4,5,6,7,8,9,1,2,3],
#             [7,8,9,1,2,3,4,5,6],
#             [2,3,4,5,6,7,8,9,1],
#             [5,6,7,8,9,1,2,3,4],
#             [8,9,1,2,3,4,5,6,7],
#             [3,4,5,6,7,8,9,1,2],
#             [6,7,8,9,1,2,3,4,5],
#             [9,1,2,3,4,5,6,7,8]]

### Empty
board = [   [0,0,0,0,0,0,0,0,0]    ,
            [0,0,0,0,0,0,0,0,0]    ,
            [0,0,0,0,0,0,0,0,0]    ,
            [0,0,0,0,0,0,0,0,0]    ,
            [0,0,0,0,0,0,0,0,0]    ,
            [0,0,0,0,0,0,0,0,0]    ,
            [0,0,0,0,0,0,0,0,0]    ,
            [0,0,0,0,0,0,0,0,0]    ,
            [0,0,0,0,0,0,0,0,0]    ]

###Random The Times
# board = [   [0,0,0,0,0,0,0,0,1]    ,
#             [0,0,6,5,0,2,8,0,0]    ,
#             [0,1,0,8,4,0,7,0,0]    ,
#             [0,3,1,0,0,0,5,8,0]    ,
#             [0,0,7,0,0,0,0,0,2]    ,
#             [0,5,0,0,0,0,4,9,0]    ,
#             [0,2,3,1,0,5,0,0,0]    ,
#             [0,0,0,7,0,9,0,0,0]    ,
#             [1,0,0,0,6,0,0,0,3]    ]

### Extra Hard 1 Solution
# board = [   [0,2,0,0,0,0,0,0,0]    ,
#             [0,0,0,6,0,0,0,0,3]    ,
#             [0,7,4,0,8,0,0,0,0]    ,
#             [0,0,0,0,0,3,0,0,2]    ,
#             [0,8,0,0,4,0,0,9,0]    ,
#             [6,0,0,5,0,0,0,0,0]    ,
#             [0,0,0,0,9,0,7,8,0]    ,
#             [5,0,0,0,0,1,0,0,0]    ,
#             [0,0,0,0,0,0,0,4,0]    ]

### 17 Clues
# board = [   [0,0,0,0,5,0,3,0,6]    ,
#             [1,0,0,6,0,0,0,0,0]    ,
#             [0,0,0,0,0,0,7,0,0]    ,
#             [2,0,0,0,0,0,5,4,0]    ,
#             [0,0,0,0,0,3,0,0,0]    ,
#             [0,0,0,0,0,6,0,0,0]    ,
#             [0,0,0,2,4,0,0,1,0]    ,
#             [0,3,0,0,0,0,0,8,0]    ,
#             [0,0,7,0,0,0,0,0,0]    ]


ok = Main(board)
#print(ok.check())
# ok.testing1234()
ok.run()
# #ok.three_by_three()
# #ok.transpose_board()
# #ok.display_board(board)



