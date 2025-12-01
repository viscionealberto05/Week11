import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def handleAnalizzaOggetti(self, e):
        self._model.buildGrafo() #grafo costruito nel model
        self._view.txt_result.controls.clear()
        self._view.txt_result.controls.append(ft.Text(f"{self._model._grafo}"))
        self._view.update_page()

    def handleCompConnessa(self,e):
        text_id = self._view._txtIdOggetto.value
        try:
            id = int(text_id)
            print(f"{id}")
            #se sono qui osso usare id per le operazioni seguenti
            numNodi = self._model.calcolaConnessa(id)
            self._view.txt_result.controls.clear()
            if isinstance(numNodi,str):
                self._view.txt_result.controls.append(ft.Text(f"{numNodi}"))
            else:
                self._view.txt_result.controls.append(ft.Text(f"Dim. componente connessa: {numNodi}"))
            self._view.update_page()

            #RICORDARSI DI PULIRE IL GRAFO OGNI VOLTA CHE VIENE SCHISCIATO IL BOTTONE

        except ValueError:
            self._view.txt_result.controls.clear()
            self._view.txt_result.controls.append(ft.Text("Inserisci un valore valido!"))
            self._view.update_page()

