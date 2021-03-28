import database
import os

class ExitController:
  def __init__(self, data):
    self.data = data

  def call(self):
    database.persist()
    os._exit(1)
