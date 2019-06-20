from random import randint

class Game:
    possibleMoves= []
    win = []
    blocks = []
    forks = []

    status = ''
    gameString = ''
    errMsg = ''

    def __init__(self, gameString):
        self.gameString = gameString
        self.board = list(gameString)
        self.blocks = []
        self.forks = []
        self.win = []
        self.status = 'In Play'

        try:
            if self.whosTurn() == 'o':

                if self.analyseGame() != 'LOSE':
                    self.possibleMoves = [i for i, x in enumerate(self.board) if x == " "]
                    self.gameString = self.decidePlay()

        except Exception as e:
            self.errMsg = 'ERROR!!!  ' + str(e )




    def analyseSet(self, spaces):
        
        spacesSet = [
            self.board[spaces[0]],
            self.board[spaces[1]],
            self.board[spaces[2]]
        ]

        naughts = spacesSet.count('o')
        crosses = spacesSet.count('x') 
        blanks = spacesSet.count(' ')

        if crosses == 3:
            
            self.status = "x wins"
            return 'LOSE'
        
        if naughts == 2 and crosses == 0 and self.status == "In Play":
            idx = spacesSet.index(' ')
            self.win.append(spaces[idx])
            self.status = "o wins"
            return 'WIN'

        # Find threats
        if crosses == 2 and naughts == 0:
            idx = spacesSet.index(' ')
            self.blocks.append(spaces[idx])
            return 'THREAT'
        
        # Find possible forks
        if naughts == 1 and crosses == 0:
            idx = spacesSet.index(' ')
            self.forks.append(spaces[idx])
            return 'FORK'

    def analyseGame(self):
        
        lines = [
            # rows
            [0,1,2],
            [3,4,5],
            [6,7,8],
            # columns
            [0,3,6],
            [1,4,7],
            [2,5,8],
            # diagonals
            [0,4,8],
            [2,4,6]
        ]

        for line in lines:
            self.analyseSet(line)

        pass

    def decidePlay(self):
        play = ''

        if len(self.win) > 0:
            play = self.win[0]

        elif len(self.blocks) > 0:
            # if something needs to be blocked.
            # check if there's a block that would also allow for fork creation.
            advantageBlocks = list(set(self.blocks).intersection(self.forks))
            if len(advantageBlocks) > 0:
                play = advantageBlocks[0]    
            else:
                play = self.blocks[0]

        elif len(self.forks) > 0:
            # nothing to block? any chances to fork?
            play = self.forks[0]
        else:
            # Try to lay the center, if not pick a random free square and play it.
            if 4 in self.possibleMoves:
                play = 4
            else:
                play = randint(0, len(self.possibleMoves))
        
        self.board[play] = 'o'
        
        return (''.join(self.board)).replace(' ', '+')


    def whosTurn(self):
        naughts = self.gameString.count('o')
        crosses = self.gameString.count('x')

        if naughts >= crosses:
            return 'x'
        else:
            return 'o'
