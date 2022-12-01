

# getCountOfVertex - Получить количество вертексов в графе

# getCountOfEdges - Получить количество граней в графе

# GetEdgeByVertex - Получить грань по вертексам

# isConnected - проверить статус грани в графе

# GetWeight - получить весс грани

# Show - отобразить таблицу графа

# SaveGraph - сохранить граф в файл

# DeleteByVertex - удалить грань по вертексам

# AddEdgeFromVertex - добавить грань по вертексам

# CreateGraphFromFile - загрузить граф из файла



class Edge:
    
    def __init__(self,startVertex,endVertex,weight=1) -> None:
        self.startVertex = startVertex
        self.endVertex = endVertex
        self.weight = weight
    
    def toString(self):
        return(self.startVertex.toString(),self.endVertex.toString(),self.weight)
    

class Vertex:
    
    isChecked = False
    Edges = []
    
    
    def __init__(self,x,y,number=0) -> None:
        self.x = int(x)
        self.y = int(y)
        # self.number = number
        
    def __eq__(self, other):
        """Equals by x,y fields"""
        if isinstance(other, Vertex):
            return self.x == other.x and self.y == other.y
        return NotImplemented
    
    def toString(self):
        return f'{self.x},{self.y}'
        
class Graph:
    
    
    def __init__(self) -> None:
        self.Edges = []
        self.Vertices = []
    
    
    def addVertices(self,vertices):
        for i in vertices:
            if i not in self.Vertices:
                self.Vertices.append(i)
    
    def getEdgeByVertices(self,f,s):
        for i in self.Edges:
            if i.startVertex == f and i.endVertex == s:
                return i
            if i.endVertex == f and i.startVertex == s:
                return i
        return False
    
    def isConnected(self,f,s):
        if self.getEdgeByVertices(f,s):
            return True
        return False
    
    def addEdge(self,f,s,weight):
        if not self.isConnected(f,s) and f in self.Vertices and s in self.Vertices:
            self.Edges.append(Edge(f,s,weight))
    
       
    def showVertices(self):
        for i in self.Vertices:
            print(i.toString())
    
    def showEdges(self):
        for i in self.Edges:
            print(i.startVertex.toString(),i.endVertex.toString(),i.weight)
            
    def deleteEdge(self,f,s):
        if self.getEdgeByVertices(f,s):
            self.Edges.remove(self.getEdgeByVertices(f,s))
    
    
    def getAllConnectedEdges(self,v):
        arr = []
        if v in self.Vertices:
            for i in self.Edges:
                if (i.startVertex == v or i.endVertex == v) :
                    # print(i.toString())
                    arr.append(i)
                    
        return arr
                    
                   
    def deleteVertex(self,v):
        target = self.getAllConnectedEdges(v)
        self.Edges = [i for i in self.Edges if i not in target ]
        
        if v in self.Vertices:
            self.Vertices.remove(v)
                
                    
        
            
    def getAllVertices(self):
        return self.Vertices
                
    def getCountOfEdges(self):
        return len(self.Edges)
    
    def getCountOfVertex(self):
        return len(self.Vertices)
    
        
    def SaveGraph(self,path):
        # s = 'start  |stop   |weight\n'
        s = ''
        for x in range(len(self.Edges)):
            i = self.Edges[x]
            tmp =f'{i.startVertex.toString()}|{i.endVertex.toString()}'+' |'+str(i.weight)+'\n'
            s +=tmp
        
        s+='\n\n##\n'
        for x in self.Vertices:
            s+= f'{x.toString()}\n'
            
        with open(path,'w') as f:
            f.writelines(s)
            
        print(f'Saved as {path}')
    

def CreateGraphFromFile(path):
    g = Graph()
    Edges = []
    Vertices = []
        
    with open(path,'r') as f:
        arr = f.read().split('##')
    
    
    vert = arr[1].split('\n')
    vert =list(filter(None, vert))
    for i in vert:
        tmp = i.split(',')
         
        fst = tmp[0]
        sec = tmp[1]
        
        v =Vertex(int(fst),int(sec))
        Vertices.append(v)
        # print(v.toString())
    
    g.addVertices(Vertices)
    
    
    edg = arr[0].split('\n')
    edg =list(filter(None, edg))
    
    
    for i in edg:
        tmp =i.split('|')
        
        fst =tmp[0].split(' ')[0]
        fst = fst.split(',')
         
        sec =tmp[1].split(' ')[0]
        sec = sec.split(',')
          
        weight =tmp[2]
        
        v1 = Vertex(int(fst[0]),int(fst[1]))
        v2 = Vertex(int(sec[0]),int(sec[1]))
        
        
        g.addEdge(v1,v2,weight)
    
    return g


    
g = Graph()
g.addVertices([Vertex(1,1),Vertex(1,2)])
g.addVertices([Vertex(1,1)])
g.showVertices()

        
        
