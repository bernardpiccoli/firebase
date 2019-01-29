import datetime
from placa import Placa
import json
from clienteService import ClientService


from firebaseUtils import FireBaseUtils

firebase = FireBaseUtils()

p1 = Placa("Fill", 1001, "GM", "Prisma", "Azul", "poi0987")
p1.novaPassagem()
firebase.CREATE(p1)
firebase.UPDATE(p1)

client = ClientService(firebase)
client.ADDPASSAGEM("poi0987")