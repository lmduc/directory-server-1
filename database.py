storage = {}

def create(sid, name, value):
  if sid not in storage:
    storage[sid] = {}
  if name in storage[sid]:
    return False
  storage[sid][name] = value
  return True

def query(sid):
  if sid not in storage:
    return []
  return storage[sid]

def reset(sid):
  storage.pop(sid, None)
