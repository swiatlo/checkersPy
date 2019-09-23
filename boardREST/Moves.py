

class CellMove():
  stepFw =[]
  stepBk =[]
  jumpFw =[]
  jumpFwOver=[]
  jumpBk =[]
  jumpBkOver=[]
  mycell =-1

  def __init__ (self, cell):
    self.mycell = cell
    self.stepFw = []
    self.stepBk =[]
    self.jumpFw =[]
    self.jumpFwOver=[]
    self.jumpBk =[]
    self.jumpBkOver=[]
    self.lastLine=True
  
  def __str__(self):
    return (str(self.mycell) +
      '\nstep Fw ' +  ' '.join(str(x) for x in  self.stepFw) +  
      '\nstep Bk ' +  ' '.join(str(x) for x in  self.stepBk) + 
      '\njump Fw ' +  ' '.join(str(x) for x in  self.jumpFw) +
      '\nover Fw ' +  ' '.join(str(x) for x in  self.jumpFwOver)+
      '\njump Bk ' +  ' '.join(str(x) for x in  self.jumpBk) +
      '\nover Bk ' +  ' '.join(str(x) for x in  self.jumpBkOver)        
        )



class Moves():

  cells=[]
  length=0
  width=0
  myOposite = None
  myOrg = None
  acuPointsFun = None

  @classmethod
  def makeOposite(cls, m):
    ret = Moves(0,0)
    ret.length = m.length
    ret.width = m.width
    ret.cells = [ CellMove(i) for i in range( len(m.cells)) ]
    ret.myOposite = m 
    m.myOposite = ret
    ret.myOrg = m 
    m.myOrg = m
    ret.acuPointsFun = min
    m.acuPointsFun = max
    for i, cm in enumerate(ret.cells, start=0):
      cm.mycell = m.cells[i].mycell 
      cm.stepFw = m.cells[i].stepBk
      cm.stepBk = m.cells[i].stepFw
      cm.jumpFw = m.cells[i].jumpBk
      cm.jumpFwOver= m.cells[i].jumpBkOver
      cm.jumpBk = m.cells[i].jumpFw
      cm.jumpBkOver = m.cells[i].jumpFwOver
      cm.lastLine = (cm.stepFw == [] )
    return ret


  def __init__(self, length, width):
    if length == 0:
      return    
    last_cellnum = width*length 
    self.length=length
    self.width=width

    self.cells = [ CellMove(i) for i in range( last_cellnum ) ]
    cellnums = [[i, int((i / width)+1 ) % 2] for i in range( last_cellnum ) ] #kkk in  range( length * width)
      
    def nextcell(curcell,delt):
      if curcell == None:
        return
      retval = curcell+(width-1)+delt + cellnums[curcell][1]
      if ((retval<last_cellnum) and (cellnums[curcell][1] != cellnums[retval][1] )):  
        return retval
      else:
        return 

    def fixcell(i,delt):
      nc = nextcell(i,delt)
      if nc != None:  
        self.cells[i].lastLine = False       
        self.cells[i].stepFw.append(nc)
        self.cells[nc].stepBk.append(i)
        jc = nextcell(nc,delt)
        if jc != None:
          self.cells[i].jumpFw.append(jc)
          self.cells[i].jumpFwOver.append(nc)
          self.cells[jc].jumpBk.append(i)
          self.cells[jc].jumpBkOver.append(nc)    

    for i in range( last_cellnum ):
      fixcell(i,0)
      fixcell(i,1)


  def printfew(self):
    print(self.cells[0])
    print(self.cells[1])
    print(self.cells[10])
    print(self.cells[26])

  