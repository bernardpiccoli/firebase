import json
import datetime

class Placa:

  def __init__(self, proprietario, apartamento, marca, modelo, cor, placa, listaPassagens=None):
    self.proprietario = proprietario
    self.apartamento = apartamento
    self.marca = marca
    self.modelo = modelo
    self.cor = cor
    self.placa = placa

    if(  listaPassagens is not None ):
      self.passagens = listaPassagens
    else:
      self.passagens = list()
  
  def PASSAR(self):
    self.passagens.append({
      'data': datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    })