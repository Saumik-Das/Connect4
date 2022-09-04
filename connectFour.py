


class Connect4:
    def __init__(self):
        self.B = [
            [0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0]
        ]

        self.C = [[5,0],[5,1],[5,2],[5,3],[5,4],[5,5],[5,6]]

        self.player = 1

    def get_open_spots(self):
        for r in range(6):
            for c in range(7):
                if self.B[r][c] == 0:
                    return [r][c]

    def is_valid_move(self,r,c):
        if 0<=r<=6 and 0<=c<=7 and self.B[r][c]==0:
            return True
        return False

    def make_move(self,r,c):
        r,c = self.C[c]
        print(r,c)
        if self.is_valid_move(r,c):
            self.B[r][c] = self.player
            self.player = (self.player+2)%2 + 1
            if r != 0:
                self.C[c] = [r-1,c]
            print(self.C)

    def check_for_winner(self):

        for c in range(7):
            for r in range(3):
                if self.B[r][c]==self.B[r+1][c]==self.B[r+2][c]==self.B[r+3][c]!=0:
                    return self.B[r][c]
                    # return self.player + 1
        for r in range(6):
            for c in range(4):
                if self.B[r][c]==self.B[r][c+1]==self.B[r][c+2]==self.B[r][c+3]!=0:
                    return self.B[r][c]
                    # return self.player + 1
        for r in range(3):
            for c in range(4):
                if self.B[r][c]==self.B[r+1][c+1]==self.B[r+2][c+2]==self.B[r+3][c+3]!=0:
                    return self.B[r][c]
        for r in reversed(range(3,6)):
            for c in range(4):
                if self.B[r][c]==self.B[r-1][c+1]==self.B[r-2][c+2]==self.B[r-3][c+3]!=0:
                    return self.B[r][c]
        if self.get_open_spots()==[]:
            return 0
        return -1

game = Connect4()

def print_board():
    chars = ['-', 'X', 'O']
    for r in range(6):
        for c in range(7):
            print(chars[game.B[r][c]], end=' ')
        print()
while game.check_for_winner()==-1:
    print_board()
    r,c = eval(input('Enter spot, player ' + str(game.player) + ': '))
    game.make_move(r,c)
print_board()

winner = game.check_for_winner()

# print(winner)

if winner==0:
    print("It's a draw.")
else:
    print('Player', winner, 'wins!')