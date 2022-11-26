

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
    
    
    

class Vertex:
    
    isChecked = False
    Edges = []
    
    def __init__(self,x,y,number=0) -> None:
        self.x = x
        self.y = y
        self.number = number
        
class Graph:
    
    
    def __init__(self,Edges) -> None:
        self.Edges = Edges
    
    def getCountOfEdges(self):
        return len(self.Edges)
    
    def getCountOfVertex(self):
        arr = []
        for i in self.Edges:
            if i.startVertex not in arr:
                arr.append(i.startVertex)
            if i.endVertex not in arr:
                arr.append(i.endVertex)
        return arr
    
    def GetEdgeByVertex(self,fst,sec):
        for i in self.Edges:
            if [int(i.startVertex.x),int(i.startVertex.y)] == [fst.x,fst.y] and [int(i.endVertex.x),int(i.endVertex.y)] == [sec.x,sec.y]:
                return i
            if [int(i.startVertex.x),int(i.startVertex.y)] == [sec.x,sec.y] and [int(i.endVertex.x),int(i.endVertex.y)] == [fst.x,fst.y]:
                return i
        return False
    
    def isConnected(self,fst,sec):
        if self.GetEdgeByVertex(fst,sec):
            return True
        return False
    
    def GetWeight(self,fst,sec):
        r = self.GetEdgeByVertex(fst,sec)
        return r.weight

    def Show(self):
        print('start    stop  weight')
        for x in range(len(self.Edges)):
            i = self.Edges[x]
            print(f'{i.startVertex.x},{i.startVertex.y} {i.startVertex.number} |{i.endVertex.x},{i.endVertex.y} {i.endVertex.number}',i.weight)
        
    def SaveGraph(self,path):
        # s = 'start  |stop   |weight\n'
        s = ''
        for x in range(len(self.Edges)):
            i = self.Edges[x]
            tmp =f'{i.startVertex.x},{i.startVertex.y} {i.startVertex.number} |{i.endVertex.x},{i.endVertex.y} {i.endVertex.number}'+' |'+str(i.weight)+'\n'
            s +=tmp
        
        with open(path,'w') as f:
            f.writelines(s)
            
        print(f'Saved as {path}')
    
    def DeleteByVertex(self,fst,sec):
        if  self.isConnected(fst,sec):
            self.Edges.remove(self.GetEdgeByVertex(fst,sec))
            print('successfully deleted')
        else:
            print('Edge not founded')
            
    def AddEdgeFromVertex(self,fst,sec):
        # print(self.isConnected(fst,sec))
        if not self.isConnected(fst,sec):
            self.Edges.append(Edge(fst,sec))
            print('Appended')
        else:
            print('Edge already excist')
        
    
def CreateGraphFromFile(path):
    Edges = []
        
    with open(path,'r') as f:
        arr = f.read().split('\n')
    
    arr =list(filter(None, arr))
    for i in arr:
        tmp =i.split('|')
        fst =tmp[0].split(' ')[0]
        fst = fst.split(',')
        fst_num = tmp[0].split(' ')[1]
            
        sec =tmp[1].split(' ')[0]
        sec = sec.split(',')
        sec_num = tmp[1].split(' ')[1]
            
        weight =tmp[2]
        # print(fst,sec)
            
        Edges.append(Edge(Vertex(fst[0],fst[1],fst_num),Vertex(sec[0],sec[1],sec_num),weight))
        # print(f'f:{fst} s:{sec} w{weight}')
    return Graph(Edges)






   