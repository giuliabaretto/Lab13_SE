import networkx as nx
from flet.core import row

from database.dao import DAO

class Model:
    def __init__(self):
        self.G = nx.DiGraph()

    def creo_grafo(self):
        self.G.clear()
        # nodi -> cromosomi
        nodi = DAO.get_cromosomi()
        self.G.add_nodes_from(nodi)
        # controllo i collegamenti tra geni, gli edges sono gli archi tra cromosomi
        interazioni = DAO.get_interazioni()


        for interazione in interazioni:
            # prendo dati dal dizionario interazione
            a = interazione["c1"]
            b = interazione["c2"]
            correlazione = interazione["correlazione"]
            # archi tra a e b
            # sono nel grafo? -> se si aggiungo la correlazione (sarà il peso del grafo)
            if self.G.has_edge(a, b):
                self.G[a][b]["weight"] += correlazione
            else:
                self.G.add_edge(a, b, weight=correlazione)

    def num_nodi(self):
        return len(self.G.nodes)

    def num_archi(self):
        return len(self.G.edges)

    def peso_min_e_max(self):
        # se non ho arco non ho peso min e max
        if len(self.G.edges) == 0:
            return 0, 0
        else:
            # devo spacchettare
            pesi = [dizionario["weight"] for a, b, dizionario in self.G.edges(data=True)]
        if not pesi:
            return 0, 0
        return min(pesi), max(pesi)

    def conta_archi_soglia(self, S):
        # nel controller verifico che il valore sia compreso tra 3 e 7
        archi_minori = 0
        archi_maggiori = 0
        # spacchetto come prima ma controllo la soglia
        for a, b, dizionario in self.G.edges(data=True):
            if dizionario["weight"] < S:
                archi_minori += 1
            elif dizionario["weight"] > S:
                archi_maggiori += 1
        return archi_minori, archi_maggiori














