import constants
from sgbd.constants import VERTEX_CURRENT      


class Vertex():
    def __init__(self,label):
        self.label = label
        self.state = constants.VERTEX_NOT_SEEN
        self.neighbours = []


        
class Graph():
    def __init__(self):
        self.__vertexVec = []
        self.last_added = None
    def getVertex(self,index):
        return self.__vertexVec[index]
    def addNeigh(self,v1,v2):
        v1.neighbours.append(v2)
        self.last_added = (v1,v2)
    def addVertex(self,label):
        v = Vertex(label)
        self.__vertexVec.append(v)
    def vecVertexSize(self):
        return len(self.__vertexVec)
    
def DFS(g: Graph,v:Vertex) -> bool:
    v.state = constants.VERTEX_CURRENT
    for n in v.neighbours:
        if n.state == constants.VERTEX_NOT_SEEN:
            if DFS(g,n):
                return True
        elif n.state == constants.VERTEX_CURRENT:
            return True
    v.state = constants.VERTEX_DONE
    return False
        

def detect_cycle(g : Graph) -> bool:
    for index in range(g.vecVertexSize):
        v = g.getVertex(index)
        if v.state == constants.VERTEX_NOT_SEEN:
            if DFS(g,v):
                return True
    return False
