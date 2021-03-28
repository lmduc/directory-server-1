import json
from registercontroller import RegisterController
from querycontroller import QueryController
from resetcontroller import ResetController
from unregistercontroller import UnregisterController
from exitcontroller import ExitController

class OperationController:
  def __init__(self, data):
    self.data = json.loads(data)

  def call(self):
    if self.data["operation"] == "register":
      return RegisterController(self.data).call()
    elif self.data["operation"] == "unregister":
      return UnregisterController(self.data).call()
    elif self.data["operation"] == "query":
      return QueryController(self.data).call()
    elif self.data["operation"] == "reset":
      return ResetController(self.data).call()
    elif self.data["operation"] == "exit":
      return ExitController(self.data).call()
