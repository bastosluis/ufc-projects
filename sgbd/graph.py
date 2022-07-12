import constants
#from sgbd.constants import VERTEX_CURRENT      
from typing import List

class Vertex():
    def __init__(self,label):
        self.label = label
        self.state = constants.VERTEX_NOT_SEEN
        self.neighbours = []


        
class Graph():
    def __init__(self):
        self.__vertexVec: List[Vertex] = []
        self.last_added = None
    def getVertex(self,index : int):
        return self.__vertexVec[index]
    def addNeigh(self,transaction_id1 : int,transaction_id2 : int):
        v1 = self.__vertexVec[transaction_id1-1]
        v2 = self.__vertexVec[transaction_id2-1]
        v1.neighbours.append(v2)
        self.last_added = (v1,v2)
    def removeNeigh(self):
        for index in range(len(self.last_added[0].neighbours)):
            if self.last_added[0].neighbours[index] == self.last_added[1]:
                self.last_added[0].neighbours.pop(index)
    def addVertex(self,label):
        v = Vertex(label)
        self.__vertexVec.append(v)
    def vecVertexSize(self):
        return len(self.__vertexVec)
    def clearVertex(self):
        for v in self.__vertexVec:
            v.state = constants.VERTEX_NOT_SEEN
    
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
    for index in range(g.vecVertexSize()):
        v = g.getVertex(index)
        if v.state == constants.VERTEX_NOT_SEEN:
            if DFS(g,v):
                g.clearVertex()
                return True
    g.clearVertex()
    return False
