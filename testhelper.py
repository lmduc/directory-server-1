import client
import json

HOST      = '127.0.0.1'
PORT      = 11111
DATA_SIZE = 32

def cli():
  return client.Client(HOST, PORT, DATA_SIZE)

def payloadFor(index, sid):
	return {
		"name": "name-" + str(index),
		"value": "value-" + str(index),
		"sid": str(sid)
	}

def resetSid(sid):
  return json.loads(
    cli().request(
      json.dumps(
        {
          "operation": "reset",
          "payload": {
            "sid": "sid-1"
          }
        }
      )
    )
  )

def register(index, sid):
  return json.loads(
    cli().request(
      json.dumps(
        {
          "operation": "register",
          "payload": payloadFor(index, sid)
        }
      )
    )
  )

def unregister(sid, name):
  return json.loads(
    cli().request(
      json.dumps(
        {
          "operation": "unregister",
          "payload": {
            "sid": sid,
            "name": name
          }
        }
      )
    )
  )

def query(sid):
  return json.loads(
    cli().request(
      json.dumps(
        {
          "operation": "query",
          "payload": {
            "sid": sid
          }
        }
      )
    )
  )
