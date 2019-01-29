from firebaseUtils import FireBaseUtils
from json import JSONDecoder
import json
from collections import namedtuple
from Placa import Placa


class ClientService:

    def __init__(_self, firebase):
        _self.firebase = firebase

    def ADDPASSAGEM(self, placaReferencia):
        obj = self.firebase.READ(placaReferencia)
        if 'passagens' in obj:
            p1 = Placa(obj['proprietario'],  obj['apartamento'], obj['marca'], obj['modelo'],  obj['cor'], placaReferencia, obj['passagens'])
        else:
            p1 = Placa(obj['proprietario'],  obj['apartamento'], obj['marca'], obj['modelo'],  obj['cor'], placaReferencia, [])
        p1.PASSAR()
        print("Passou")
        self.firebase.UPDATE(p1)

    def LERPASSAGENS(self, placaReferencia):
            obj = self.firebase.READ(placaReferencia)
            return obj