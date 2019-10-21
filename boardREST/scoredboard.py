from checkers.boardREST.board import * #Board 

class ScoredBoard(Board):
    """
    extends board class with calculation of position value so we can have a score for each move.
    pawn is 1, king is 2 (negative for the oposition)
    """
    pointValue = 0


    def computeMoves(self, side, n_side, mysideDirection, depth=0):
      """
      each board in the tree will have a score. that scores from posible moves are propagated up in the tree.
      it is always progapated best score for the side that has a turn.
      If it is the enemy's turn the value is minimum of the score - which represtent the best move for the oposition
      if our move we take the maximum score to propagate up.
      """

      def getSide():
        if mysideDirection == mysideDirection.myOrg:
          return side 
        else: 
          return n_side

      if any(str.upper(n_side) == str.upper(p) for p in self.position) and any(str.upper(side) == str.upper(p) for p in self.position) :  # [side,  ] in self.position: 
        super().computeMoves( side, n_side, mysideDirection, depth)
      else:        
        self.pointValue =  self.getPoints(self.position, getSide() ) * 2
        #print('oops', self.position, self.pointValue )
       # self.pointValue = side if mysideDirection == mysideDirection.myOrg else n_side
        return

      if self.nextboards==[]: #no move posible for the oponent        
        self.pointValue = self.getPoints(self.position, getSide() ) * 3  
        #print('oops', self.position, self.pointValue )
      elif depth>0:
        self.pointValue = mysideDirection.acuPointsFun(br.pointValue for br in self.tree)            
      else:
        pts = [self.getPoints(Aposition[0], getSide()) for Aposition in self.nextboards ]
        self.pointValue = mysideDirection.acuPointsFun(pts)
        

    def getPoints(self, Aposition, a_side):
      ret = 0
      for p in Aposition:
        if p >' ':          
          if str.isupper(p):
            dif = 2
          else:
            dif = 1
          if p.lower() == a_side:
            ret = ret + dif
          else:
            ret = ret - dif
      return ret      
