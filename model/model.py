import networkx as nx
from database.DAO import DAO
from model.connessione import Connessione

class Model:
    def __init__(self):
        self._objects_list = []
        self.getObjects()

        #mi posso creare anche un dizionario di object
        self._objects_dict = {}
        for o in self._objects_list:
            self._objects_dict[o.object_id] = o

        #grafo semplice, non diretto ma pesato
        self._grafo = nx.Graph()


    def getObjects(self):
        self._objects_list = DAO.readObjects()

    def buildGrafo(self):
        #nodi
        self._grafo.add_nodes_from(self._objects_list)

        #archi

        #modo 1 --> più lungo in assoluto (80K x 80K query SQL, dove 80k sono i nodi)
        #NON CONVENIENTE
        """for u in self._objects_list:
            for v in self._objects_list:
                DAO.readEdges(u, v) #da scrivere
                pass"""

        #modo 2 --> usare una query sola per estrarre le connessioni
        connessioni = DAO.readConnessioni(self._objects_dict)
        for c in connessioni:
            self._grafo.add_edge(c.o1,c.o2,weight=c.peso) #peso?

    def calcolaConnessa(self, id_nodo):
        nodo_sorgente = self._objects_dict[id_nodo]
        successori = nx.dfs_successors(self._grafo, nodo_sorgente)
        #for nodo in successori:
        print(f"Successori {len(successori)}")

        predecessori = nx.dfs_predecessors(self._grafo, nodo_sorgente)
        #for nodo in predecessori:
        print(f"Predecessori {len(predecessori)}")

        #Ottengo
        albero = nx.dfs_tree(self._grafo, nodo_sorgente)
        print(f"Albero {albero}")
        return len(albero.nodes)
