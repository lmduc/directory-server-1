import database
import sys

class ExitController:
  def __init__(self, data):
    self.data = data

  def call(self):
    database.persist()
    sys.exit()
