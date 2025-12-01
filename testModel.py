from model.model import Model

model = Model()

print(model._objects_dict[1234])

model.buildGrafo()
print(model._grafo)