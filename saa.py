#/*---------------------------------------------------------------------
#|
#|  Lab 3:  Simulated Annealing in N-Queens			
#|  Christianah Adigun
#|
#|  Purpose:  To solve the N-queens problem using simulated annealing.
#|
#*-------------------------------------------------------------------*/

import time
import random, math

class Board(object):
    """An N-queens solution attempt."""

    def __init__(self, queens):
        """Instances differ by their queen placements."""
        self.queens = queens.copy()  # No aliasing!

    def display(self):
        """Print the board."""
        for r in range(len(self.queens)):
            for c in range(len(self.queens)):
                if self.queens[c] == r:
                    print 'Q',
                else:
                    print '-',
            print
        print

    def moves(self):
        """Return a list of possible moves given the current placements."""
        # YOU FILL THIS IN
        global temp, cNew, cOld, origQueen
        initial = list()
        origQueen = self.queens.copy()
        # Get the positions of the current queens
        for r in range(len(self.queens)):
            for c in range(len(self.queens)):
                if self.queens[c] == r:
                    k = (c, r)
                    initial.append(k)        
        initial = sorted(initial, key=lambda x: x[0])

        # Get possible moves
        possibleMoves = list()
        for i in range(len(initial)):
            pair = initial[i]
            val = pair[1]
            for j in range(len(initial)):
                if (j != val):
                    k = (i,j)
                    possibleMoves.append(k)

        # Get cost
        cOld = self.cost()

        rand = random.randint(1, len(possibleMoves) - 1)
        nxtMove = possibleMoves[rand]
        dupQueen = self.queens
        for r in range(len(dupQueen)):
            for c in range(len(dupQueen)):
                if dupQueen[c] == r and c == nxtMove[0]:
                    dupQueen[c] = nxtMove[1]
                else:
                    pass

        self.queens = dupQueen 
        cNew = self.cost()

        if(temp > threshold):
            if(cOld > 0):
                if(cNew <= cOld):
                    # if the cost of neighbor is less than the cost of solution
                    cOld = cNew
                    self.queens = dupQueen
                    #Add move to list
                    position.append(nxtMove)
                else:
                    # Compute cost increase, c and probability, p
                    c = cNew - cOld
                    p = math.exp(-c/temp)
                    if (p > 1):
                        self.queens = dupQueen
                        position.append(nxtMove)
                    else:
                        self.queens = origQueen
                        
                temp = temp * decayRate
                self.moves()

        


    def neighbor(self, move):
        """Return a Board instance like this one but with one move made."""
        # YOU FILL THIS IN
        global globalQueen
        for r in range(len(globalQueen)):
            for c in range(len(globalQueen)):
                if globalQueen[c] == r and c == move[0]:
                    globalQueen[c] = move[1]
                else:
                    pass
        return Board(globalQueen)


    def cost(self):
        """Compute the cost of this solution."""
        # YOU FILL THIS IN
        copy = []
        initial = []
        cost = 0
        
        # Get cost by rows
        for r in range(len(self.queens)):
            for c in range(len(self.queens)):
                if self.queens[c] == r:
                    k = (c, r)
                    copy.append(r)
                    initial.append(k)
        initial = sorted(initial, key=lambda x: x[0])

        # Gets adjacent diagonal values to current position of queen
        def diags(move):
            arr = []
            r = move[0]
            c = move[1]
            for i in range(8):
                for j in range(8):
                    r -= 1
                    c += 1
                    k = (r, c)
                    if (r < 0) or (c > 7):
                        pass
                    else:
                        arr.append(k)
            r = move[0]
            c = move[1]
            for i in range(8):
                for j in range(8):
                    r += 1
                    c -= 1
                    k = (r, c)
                    if (c < 0) or (r > 7):
                        pass
                    else:
                        arr.append(k)
            r = move[0]
            c = move[1]
            for i in range(8):
                for j in range(8):
                    r += 1
                    c += 1
                    k = (r, c)
                    if (c < 0) or (r > 7) or (r < 0) or (c > 7):
                        pass
                    else:
                        arr.append(k)
            r = move[0]
            c = move[1]
            for i in range(8):
                for j in range(8):
                    r -= 1
                    c -= 1
                    k = (r, c)
                    if (c < 0) or (r > 7) or (r < 0) or (c > 7):
                        pass
                    else:
                        arr.append(k)
            return arr
        
        # Add to cost of rows
        cost += len(copy) - len(set(copy))
        
        # Get cost by diagonal for i in range(len(initial)):
        for i in range(len(initial)):
            thisDiagCost = len(set(initial) - ( set(initial) - set(diags(initial[i]))))
            cost += thisDiagCost

        # Return cost value
        return cost

class Agent(object):
    """Knows how to solve an n-queens problem with simulated annealing."""
    def anneal(self, board):
        """Return a list of moves to adjust queen placements."""
        # YOU FILL THIS IN
        # Return list of moves in position Array
        print "Steps: ", len(position)
        print "List of Moves: ", position
        print "\n\n\n"
        return position
        

def main():
    """Create a problem, solve it with simulated anealing, and console-animate."""
    
    # Set Global Variables
    global temp, position, cOld, cNew, origQueen, threshold, decayRate, globalQueen
    temp = random.randint(10, 15)
    threshold = 0.1 / temp
    decayRate = 1 - threshold
    position = list()
    
    
    queens = dict()
    for col in range(8):
        row = random.choice(range(8))
        queens[col] = row

    board = Board(queens)
    globalQueen = queens.copy()
    board.display()
    board.moves()

    agent = Agent()
    path = agent.anneal(board)

    while path:
        move = path.pop(0)
        board = board.neighbor(move)
        time.sleep(0.5)
        board.display()


if __name__ == '__main__':
    main()
