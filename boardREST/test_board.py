import unittest
from board import *
from scoredboard import *
# from scoredboard import *

class TestBoardMoves(unittest.TestCase):
    def test_boardjumps(self):
        b = Board('bbbbbbbb            wwwwwwwwwwww',[],Board(''))
        #print(b.position)
        b.position[23]=' '
        b.position[9]='w'
        b.position[18]='w'
        b.position[21]='B'
        b.position[17]='W'
        b.position[19]='b'
        b.position[15]='W'
        b.position[20]='b'
        b.position[29]=' '
        
        
        bn1 = b.position.copy()
        bn2 = b.position.copy()
        Bn3 = b.position.copy()
        Bn4 = b.position.copy()

        print(b)
        #b.position[17]='w'
        b.computeMoves('b','w',m_side)
        bn1[5] = ' ' 
        bn1[9] = ' '
        bn1[18] = ' '
        bn1[23] = 'b'

        bn2[6] = ' '
        bn2[9] = ' ' 
        bn2[13] = 'b'

        Bn3[20] = ' '
        Bn3[24] = ' '
        Bn3[29] = 'B'

        Bn4[21] = ' '
        Bn4[17] = ' ' 
        Bn4[18] = ' '
        Bn4[23] = 'B' 

         
#        print(b.position)
        #print(Board.fromList(b.nextboards[0][0]))
        #print(Board.fromList(b.nextboards[1][0]))
        print(b.nextboards[0][1])  
        print(b.nextboards[1][1])              
        print(b.nextboards[2][1])              
        print(b.nextboards[3][1])      
        self.assertEqual(b.nextboards[0][0],bn1)        
        self.assertEqual(b.nextboards[1][0],bn2)        
        self.assertEqual(b.nextboards[2][0],Bn3)        
        self.assertEqual(b.nextboards[3][0],Bn4)        
        self.assertEqual(b.nextboards[0][1],[5, 14, 23])  
        self.assertEqual(b.nextboards[1][1],[6, 13])   
        self.assertEqual(b.nextboards[2][1],[20, 29])              
        self.assertEqual(b.nextboards[3][1],[21, 14, 23])
        self.assertEqual(len(b.nextboards), 4)

    def test_boardstep(self):
        b = Board('bb  bb         b  Bbww wwwbwww w',[], Board('') )
        print('\n kkkk\n')
        print(b)
        b.computeMoves('b','w', m_side)
        #for nb in b.nextboards:
         #   print(Board.fromList(nb[0]))

        bn1 = b.position.copy()
        bn2 = b.position.copy()
        bn3 = b.position.copy()
        bn4 = b.position.copy()
        bn5 = b.position.copy()
        bn6 = b.position.copy()
        bn7 = b.position.copy()
        bn8 = Board('bbb wwwwwwwwwwww                ',[], Board('') )
        bn8.computeMoves('b','w', m_side)

        bn1[1] = ' '
        bn1[6] = 'b'
        bn2[4] = ' '
        bn2[8] = 'b'
        bn3[5] = ' '
        bn3[8] = 'b'
        bn4[5] = ' '
        bn4[9] = 'b'
        bn5[18] = ' '
        bn5[22] = 'B'
        bn6[18] = ' '
        bn6[14] = 'B'
        bn7[26] = ' '
        bn7[30] = 'B'


        self.assertEqual(b.nextboards[0][0], bn1)
        self.assertEqual(b.nextboards[1][0], bn2)
        self.assertEqual(b.nextboards[2][0], bn3)
        self.assertEqual(b.nextboards[3][0], bn4)
        self.assertEqual(b.nextboards[4][0], bn5)
        self.assertEqual(b.nextboards[5][0], bn6)
        self.assertEqual(b.nextboards[6][0], bn7)
        self.assertEqual(bn8.nextboards, [])

        self.assertEqual(b.nextboards[1][1], [4,8])
        self.assertEqual(b.nextboards[4][1], [18,22])
        self.assertEqual(b.nextboards[5][1], [18,14])
        self.assertEqual(len(b.nextboards), 7)

    def test_boardPoints(self):
        b = ScoredBoard('bb  bb         b  Bbww wwwbww  w', [], Board('') )
        self.assertEqual(b.getPoints(b.position, 'b'),9-8)        
        self.assertEqual(b.getPoints(b.position, 'w'),8-9)

    def test_nextMoveErr(self):
        b = ScoredBoard(' b b b bbbbb     w Bw    w      ',[], Board(''))
        print(b)
        b.computeMoves('b','w',m_side,6)
        self.assertEqual(b.getPoints(b.position, 'b'), 7)  #was 5

        b = ScoredBoard(' b    b bbbbbb w wwww www b     ',[], Board('') )
        #print(b)
        b.computeMoves('b','w',m_side,6)
        self.assertEqual(b.getPoints(b.position, 'b'), 1)

        b = ScoredBoard('   b   b bbb      ww b w  B w   ',[], Board(''))
        #print(b)
        b.computeMoves('b','w',m_side,6)
        self.assertEqual(b.getPoints(b.position, 'b'), 4)

        b = ScoredBoard('   b   b bbb      ww b w  B     ',[], Board(''))
        print(b)
        b.computeMoves('b','w',m_side,8)
        self.assertEqual(b.getPoints(b.position, 'b'), 5) 

