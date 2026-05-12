import networkx as nx
from database.DAO import DAO

class Model:
    def __init__(self):
        self._grafo = nx.Graph()

        self._idMap = {}
        for el in DAO.getAllStati():
            self._idMap[el.CCode] = el

    def buildGraph(self, anno):
        self._grafo.clear()
        self._nodiAnno(anno)
        # lista = []
        for el in DAO.getAllConfini(anno):
            nodo_partenza = self._idMap[el.state1no]
            nodo_arrivo = self._idMap[el.state2no]

            # nel caso in cui non si considerino i nodi con nessun arco
            # if nodo_partenza not in lista:
                # self._grafo.add_node(nodo_partenza)
                # lista.append(nodo_partenza)
            # if nodo_arrivo not in lista:
                # self._grafo.add_node(nodo_arrivo)
                # lista.append(nodo_arrivo)

            self._grafo.add_edge(nodo_arrivo, nodo_partenza)

    def _nodiAnno(self, anno):
        lista = []
        for el in DAO.getAllConfiniSenzaTipo(anno):
            nodo_partenza = self._idMap[el.state1no]
            nodo_arrivo = self._idMap[el.state2no]

            if nodo_partenza not in lista:
                self._grafo.add_node(nodo_partenza)
                lista.append(nodo_partenza)
            if nodo_arrivo not in lista:
                self._grafo.add_node(nodo_arrivo)
                lista.append(nodo_arrivo)

        # print(sorted(lista, key=lambda x: x.StateNme))

    def statiRaggiungibili(self, stato):
        for el in DAO.getAllStati():
            if el.StateNme == stato:
                lista = list(nx.dfs_preorder_nodes(self._grafo, el))
                # return sorted(lista, key=lambda x: x.StateNme)
                return lista

    def getNumNodes(self):
        return len(self._grafo.nodes)  # equivalente a self._nodes

    def getNodi(self):
        lista = self._grafo.nodes()
        return sorted(lista, key=lambda x: x.StateNme)

    def getNumEdges(self):
        return len(self._grafo.edges)

    def getVicini(self):
        lista = self._grafo.degree()
        return sorted(lista, key=lambda x: x[0].StateNme)

    def getConnesse(self):
        return nx.number_connected_components(self._grafo)



