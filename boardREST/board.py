import os
import sys
import bisect
import time
#import CellMove 
from checkers.boardREST.Moves import Moves

#exec(open("./board.py").read())

cell_v = ('b','B','w','W')
#cacheRes = []
Bcounter = 0
m_side = Moves(8,4)
m_nside = Moves.makeOposite(m_side)
#compBoard = None


class Board:
    position=[]
    moves=[]
    nextboards=[]
    tree = []
    m = None
    positionAsString = ''
    cacheRes = []
    compBoard = None


    def __init__(self, s, cacheList = None, compObj = None):     
      self.position = [i for i in s] # string to a list
      self.positionAsString = s
      self.m =None
      self.moves=[]
      self.nextboards=[]
      self.tree = []       
      self.cacheRes = cacheList
      self.compBoard = compObj
      global Bcounter
      Bcounter =Bcounter + 1
      
    def __del__(self):
      global Bcounter
      Bcounter= Bcounter - 1
    
    @classmethod
    def fromList(cls, b, cacheList = None, compBoardObj = None ):
      bret = cls('', cacheList, compBoardObj)
      bret.position = b
      bret.positionAsString = ''.join(b)
      return bret

    def compJumps(self, side, n_side):
      
      def makeBoard(curBoard,v):
        
        def doJumpDir (v, jump, jumpOver):
          retval=False
          for jmp in range(len(jump)):
            if (curBoard[ jump[jmp] ] ==' ') and ( str.lower(curBoard[jumpOver[jmp] ] )==n_side ):           
              self.moves.append(v)
              newBoard = []
              newBoard = curBoard.copy()
              newBoard[ jump[jmp] ] = str.upper(newBoard[v]) if self.m.cells[ jump[jmp] ].lastLine else newBoard[v]  
              newBoard[ v ] = ' '
              newBoard[ jumpOver[jmp] ] = ' '        
              
              if not makeBoard(newBoard, jump[jmp] ): #compJumps(curBoard, side, n_side):                
                self.nextboards.append([newBoard, self.moves.copy()])
                self.nextboards[-1][1].append(jump[jmp])
              self.moves.pop()
              retval= True
          return retval
              
        doJmpRetB = False
        doJmpRetF = False
        if pc == str.upper(side):
          doJmpRetB = doJumpDir(v, self.m.cells[v].jumpBk, self.m.cells[v].jumpBkOver)
        doJmpRetF = doJumpDir(v, self.m.cells[v].jumpFw, self.m.cells[v].jumpFwOver)  
        return (doJmpRetF or doJmpRetB)

      # for ever piece try to make new board and moves
      for v, pc in enumerate(self.position, start=0):
        if str.lower(pc)==side:          
          makeBoard(self.position, v)

      return len(self.nextboards) >0



    def compSteps(self,  side, n_side):
      
      def doStepDir (v, step): 
        for stp in range(len(step)):
          if self.position[ step[stp] ] == ' ':
            newBoard = []
            newBoard = self.position.copy()
            newBoard[step[stp]] = str.upper(newBoard[v]) if self.m.cells[ step[stp] ].lastLine else newBoard[v]   #
            newBoard[v] =' '
            self.nextboards.append([newBoard, [v, step[stp] ]])

      for v, pc in enumerate(self.position, start=0):
        if str.lower(pc)==side:          
          doStepDir(v, self.m.cells[v].stepFw)
          if pc==str.upper(side):
            doStepDir(v, self.m.cells[v].stepBk)
        
    #def __cmp__(self,other):
     # return 0 #cmp(0,0)

    def __lt__(self,other):
      return self.positionAsString < other.positionAsString
    
    def __eq__(self,other):
      return self.positionAsString == other.positionAsString
  

    def computeMoves(self, side, n_side, mysideDirection, depth=0):
      cacheRes = self.cacheRes
      compBoard = self.compBoard
      self.m =mysideDirection
      if not self.compJumps( side, n_side): # {self.position,[] },
        self.compSteps( side, n_side)
      #if cacheRes == []:
       # cacheRes = [ [] for i in range( depth+1 )]
      
      if len(cacheRes)<=depth:
        for i in range(len(cacheRes), depth+1 ):
          cacheRes.append([]) 


      cr = cacheRes[depth]
      bisect.insort(cr, self) # (''.join(self.position), self ))
    
      def index(a, x):
          #'Locate the leftmost value exactly equal to x'
          i = bisect.bisect_left(a, x)
          if i != len(a) and a[i] == x:
              return i
          raise ValueError

      if depth>0:
        #self.pointValue = -132 if mysideDirection == mysideDirection.myOrg else 132
        cr = cacheRes[depth-1]
        for b in self.nextboards:          
          mustCompute =  False           
          try:
            compBoard.positionAsString = ''.join(b[0])
            #idx = bisect.bisect(cr, compBoard) #  (''.join(b[0]),)) #cr.index(b[0])            
            idx=index(cr, compBoard)
            self.tree.append( cr[idx])           
          except ValueError: 
            mustCompute = True

          if mustCompute == True:    
            self.tree.append(self.fromList(b[0], self.cacheRes, self.compBoard))            		
            self.tree[-1].computeMoves(n_side, side, mysideDirection.myOposite, depth-1)
            

    def __str__(self):
      s='   '
      for l in range(m_side.length):
        for w in range(m_side.width):
          s= s+'['+ self.position[ w + (l* m_side.width)]+ ']   '
        s = s +'\n' 
        if (l % 2)==1:
          s = s +'   '   
      return s

    @classmethod
    def getBoardCount(cls):
      global Bcounter
      ret = Bcounter
      Bcounter = 0
      return ret

#compBoard = Board('') #
#b = Board('bbbbbbbbbbbb        wwwwwwwwwwww')

#tstart = time.time()
#b.computeMoves('b','w', m_side, 6)
#print(time.time() - tstart )
#print(Bcounter)



#print(b.nextboards[0][0])
#print(b.nextboards[1][0])
