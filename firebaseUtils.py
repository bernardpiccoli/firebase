import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

class FireBaseUtils:
    
    def __init__(self):
        self.ref = self.connect()

    def connect(self):
        cred = credentials.Certificate("serviceAccountKey.json")

        firebase_admin.initialize_app(cred, {
            'databaseURL': 'https://autopark-alpr.firebaseio.com/'
        })

        ref = db.reference("placas")
        return ref

    def CREATE(self, obj):
        obj_ref = self.ref.child(obj.placa.upper())
        obj_ref.set({
            'proprietario': obj.proprietario,  
            'apartamento': obj.apartamento,  
            'marca': obj.marca,
            'modelo': obj.modelo,
            'cor': obj.cor
        })
    
    def UPDATE(self, obj):
        obj_ref  = self.ref.child(obj.placa.upper())
        obj_ref.update({
            'proprietario': obj.proprietario,  
            'apartamento': obj.apartamento,  
            'marca': obj.marca,
            'modelo': obj.modelo,
            'cor': obj.cor,
            'passagens': obj.passagens
        })

    def READ(self, placa = None):
        if(placa != None):
            obj_ref  = self.ref.child(placa.upper())
            return obj_ref.get()
        else:
            print(self.ref.get())

    def DELETE(self, obj):
        obj_ref  = self.ref.child(obj.placa)
        obj_ref.delete()