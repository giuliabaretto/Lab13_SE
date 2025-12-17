import flet as ft
from UI.view import View
from model.model import Model

class Controller:
    def __init__(self, view: View, model: Model):
        self._view = view
        self._model = model

    def handle_graph(self, e):
        """ Handler per gestire creazione del grafo """""
        self._model.creo_grafo()
        self._view.lista_visualizzazione_1.controls.clear()
        self._view.lista_visualizzazione_1.controls.append(ft.Text(f"Numero di vertici: {self._model.num_nodi()} Numero di archi: {self._model.num_archi()}"))
        min_p, max_p = self._model.peso_min_e_max()
        self._view.lista_visualizzazione_1.controls.append(ft.Text(f"Informazioni sui pesi degli archi - valore minimo: {min_p} e valore massimo: {max_p}"))
        self._view.update()

    def handle_conta_edges(self, e):
        """ Handler per gestire il conteggio degli archi """""
        self._view.lista_visualizzazione_2.controls.clear()
        try:
            soglia = float(self._view.txt_name.value)
        except:
            self._view.show_alert("Inserisci un numero valido per la soglia")
            return
        archi_minori, archi_maggiori = self._model.conta_archi_soglia(soglia)
        if not 3 <= soglia <= 7:
            self._view.show_alert("Soglia fuori range. Inserisci un numero compreso nell'intervallo [3,7]")
        self._view.lista_visualizzazione_2.controls.append(ft.Text(f"Numero archi con peso maggiore della soglia: {archi_maggiori}"))
        self._view.lista_visualizzazione_2.controls.append(ft.Text(f"Numero archi con peso minore della soglia: {archi_minori}"))
        self._view.update()

    def handle_ricerca(self, e):
        """ Handler per gestire il problema ricorsivo di ricerca del cammino """""
        # TODO