import database

class RegisterController:
  def __init__(self, data):
    self.data = data
    payload = data["payload"]
    self.sid = payload["sid"]
    self.name = payload["name"]
    self.value = payload["value"]

  def call(self):
    if database.create(self.sid, self.name, self.value):
      return { "success": "true" }
    else:
      return { "success": "false" }
