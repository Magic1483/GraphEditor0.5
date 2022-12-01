import getch
from GE_06 import *


def createTwoVerticesByPoints(x1,y1,x2,y2):
    v1 = Vertex(int(x1),int(y1))
    v2 = Vertex(int(x2),int(y2))
    return [v1,v2]

def command():
    g = Graph()
    print('---Graph created---')
    while True:
        print('Command list:\n'+
              '1 show Vertices      5 delete Edge\n'+
              '2 show Edges         6 delete Vertex\n'+
              '3 add Vertex         7 save Grapn\n'+
              '4 add Edge           8 load Graph')
        print('-----------')
    
        cmd = getch.getch()
        
        match int(cmd):
            case 0:
                break
            case 1:
                g.showVertices()
            case 2:
                g.showEdges()
            case 3:
                var = input('write x,y vertex coordinate: ')
                var = var.split(' ')
                v = Vertex(var[0],var[1])
                g.addVertices([v])
            case 4:
                var1 = input('write x,y  coordinate first vertex: ')
                var1 = var1.split(' ')
                
                var2 = input('write x,y  coordinate second vertex: ')
                var2 = var2.split(' ')
                weight = input('write weight')
                
                v = createTwoVerticesByPoints(var1[0],var1[1],var2[0],var2[1])
                
                
                g.addEdge(v[0],v[1],weight)
            case 5:
                var1 = input('write x,y  coordinate first vertex: ')
                var1 = var1.split(' ')
                
                var2 = input('write x,y  coordinate second vertex: ')
                var2 = var2.split(' ')
                
                v = createTwoVerticesByPoints(var1[0],var1[1],var2[0],var2[1])
                g.deleteEdge(v[0],v[1])
            case 6:
                var1 = input('write x,y  coordinate  vertex: ')
                var1 = var1.split(' ')
                
                v = Vertex(int(var1[0]),int(var1[1]))
                g.deleteVertex(v)
            case 7:
                path = input('write path for save file (.txt)')
                g.SaveGraph(path)
            case 8:
                path = input('write path to saved file: ')
                g = CreateGraphFromFile(path)
                
                
                
                
                
                
                
    
        print('-----------')
    
if __name__=='__main__':
    command()