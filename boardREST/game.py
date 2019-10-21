from board import * #Board 
from scoredboard import * #Board 
from random import *
from sys import *

#sb = ScoredBoard('bbbbbbbbb bb  b   w ww wwwwwwwww', [], Board(''))
#sb = ScoredBoard(' W b bwWb w          wBB        ', [], Board(''))
#sb = ScoredBoard('  bb   b  bb b      www     ww w', [], Board(''))
sb = ScoredBoard('b       b    bb b   w w ww bw  w', [], Board(''))
print(sb)


if len(sys.argv) >1:
    while True:        
        sb.computeMoves('b','w', m_side, int(sys.argv[1]))
        # for idx, brd in enumerate(sb.tree, start=0):
        #     if brd.pointValue == sb.pointValue:
        #         sb = ScoredBoard.fromList( sb.nextboards[idx][0] )
        #         print('comp move ', idx)
        #         break
        sb = choice( [brd for brd in sb.tree if brd.pointValue == sb.pointValue] )
        sb = ScoredBoard.fromList( sb.position, sb.cacheRes, sb.compBoard )
        print('comp move ')
        print(sb)           
        sb.computeMoves('w','b', m_side.myOposite, 1)
        if len(sb.nextboards) ==0:
            print('game over')
            exit()
        idx = randrange(0,len(sb.nextboards))
        # if len(sb.tree) >0: 
        #   for idx, brd in enumerate(sb.tree, start=0):
        #     if brd.pointValue == sb.pointValue:
        #       break
        # else:
        #   idx = randrange(0,len(sb.nextboards))
        
        sb = ScoredBoard.fromList(sb.nextboards[idx][0], sb.cacheRes, sb.compBoard )
        print('after my move')
        print(sb)
    exit()


while True:
  tstart = time.time()
  sb.computeMoves('b','w', m_side, 6)
  print(time.time() - tstart)
  print(ScoredBoard.getBoardCount())
  for idx, brd in enumerate(sb.tree, start=0):
    print(idx, brd.pointValue)
  # for idx, brd in enumerate(sb.tree, start=0):
  #   if brd.pointValue == sb.pointValue:
  #     sb = ScoredBoard.fromList( sb.nextboards[idx][0] )
  #     print('comp move ', idx)
  #     break
  xb = choice( [brd for brd in sb.tree if brd.pointValue == sb.pointValue] )
  print('comp move ', sb.tree.index(xb))

  sb = ScoredBoard.fromList( xb.position, xb.cacheRes, xb.compBoard  )
  print(sb)
  sb.computeMoves('w','b', m_side.myOposite, 0)
  for idx, brd in enumerate(sb.nextboards, start=0):    
    print(idx, sb.nextboards[idx][1] )
  idx = int(input())
  if idx==-1 or idx >= len( sb.nextboards): 
    break
  sb = ScoredBoard.fromList( sb.nextboards[idx][0], sb.cacheRes, sb.compBoard )
  print('after my move')
  print(sb)
