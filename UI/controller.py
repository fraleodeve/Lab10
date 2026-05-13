import flet as ft

class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def handleCalcola(self, e):
        anno = self._view._txtAnno.value

        if anno == "":
            self._view.txt_result.controls.clear()
            self._view.txt_result.controls.append(
                ft.Text("Attenzione! Inserire un anno.", color="red"))
            self._view.update_page()
            return

        try:  # verifico che l'utente inserisca un valore numerico
            annoInt = int(anno)
        except ValueError:
            self._view.txt_result.controls.clear()
            self._view.txt_result.controls.append(
                ft.Text("Attenzione! Inserire un valore numerico.", color="red"))
            self._view.update_page()
            return

        if annoInt < 1816 or annoInt > 2016:
            self._view.txt_result.controls.clear()
            self._view.txt_result.controls.append(
                ft.Text("Attenzione! Inserire un valore compreso tra 1816 e 2016.", color="red"))
            self._view.update_page()
            return

        self._model.buildGraph(annoInt)
        vicini = self._model.getVicini()

        self._view.txt_result.controls.clear()
        self._view.txt_result.controls.append(ft.Text(f"Grafo correttamente creato!"))
        self._view.txt_result.controls.append(ft.Text(f"Il grafo ha {self._model.getConnesse()} componenti connesse!"))
        self._view.txt_result.controls.append(ft.Text(f"Di seguito il dettaglio sui nodi: "))
        for el in vicini:
            self._view.txt_result.controls.append(ft.Text(f"{el[0]} -- {el[1]} vicini."))

        self._view._DDStati.value = None
        self._view._DDStati.options = []

        self._view._DDStati.disabled = False
        self._view._btnTrova.disabled = False

        nodi = self._model.getNodi()
        for el in nodi:
            self._view._DDStati.options.append(ft.dropdown.Option(text = el.StateNme,
                                                                  key = el))
        self._view.update_page()

    def handleTrova(self, e):
        stato = self._view._DDStati.value
        if stato is None:
            self._view.txt_result.controls.clear()
            self._view.txt_result.controls.append(
                ft.Text("Attenzione! Selezionare un stato", color="red"))
            self._view.update_page()
            return

        lista = self._model.statiRaggiungibili(stato)
        print(f"Gli stati raggiungibili da {stato} sono: {len(lista)}")

        self._view.txt_result.controls.clear()
        if len(lista) == 1:
            self._view.txt_result.controls.append(ft.Text(f"Non posso raggiungere nessun altro stato"))
        else:
            self._view.txt_result.controls.append(ft.Text(f"Gli stati raggiungibili da {stato} sono:"))
            # lista.remove(lista[0]) # se non si vuole considerare il nodo di partenza
            for el in lista:
                self._view.txt_result.controls.append(ft.Text(f"- {el}"))
        self._view.update_page()

