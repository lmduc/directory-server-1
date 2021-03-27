import database

class QueryController:
  def __init__(self, data):
    self.data = data
    payload = data["payload"]
    self.sid = payload["sid"]

  def call(self):
    return {
      "success": "true",
      "data": database.query(self.sid)
    }
