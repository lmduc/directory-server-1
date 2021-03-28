import database

class ResetController:
  def __init__(self, data):
    self.data = data
    payload = data["payload"]
    self.sid = payload["sid"]

  def call(self):
    database.reset(self.sid)
    return { "success": "true" }
