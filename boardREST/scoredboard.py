from checkers.boardREST.board import * #Board 

class ScoredBoard(Board):
    
    pointValue = 0


    def computeMoves(self, side, n_side, mysideDirection, depth=0):

      def getSide():
        if mysideDirection == mysideDirection.myOrg:
          return side 
        else: 
          return n_side

# elem in list1  for elem in list2
      if any(str.upper(n_side) == str.upper(p) for p in self.position) and any(str.upper(side) == str.upper(p) for p in self.position) :  # [side,  ] in self.position: 
        super().computeMoves( side, n_side, mysideDirection, depth)
      else:
        #print('oops', self.position)
        self.pointValue = self.getPoints(self.position, getSide() ) *2
       # self.pointValue = side if mysideDirection == mysideDirection.myOrg else n_side
        return

      if self.nextboards==[]: #no move posible for the oponent
        self.pointValue = mysideDirection.acuPointsFun(12,-12)  # get some dynamic value?
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
