import database

class UnregisterController:
  def __init__(self, data):
    self.data = data
    payload = data["payload"]
    self.sid = payload["sid"]
    self.name = payload["name"]

  def call(self):
    if database.delete(self.sid, self.name):
      return { "success": "true" }
    else:
      return { "success": "false" }
