import yaml

FILE = "database.yaml"

storage = {}

def create(sid, name, value):
  global storage
  print("[DATABASE] Creating SID %s - name %s" % (sid, name))
  if sid not in storage:
    storage[sid] = {}
  if name in storage[sid]:
    print("[DATABASE] Error - %s already exits in SID %s" % (name, sid))
    return False
  storage[sid][name] = value
  print("[DATABASE] Created - SID %s - name %s" % (sid, name))
  return True

def query(sid):
  global storage
  print("[DATABASE] Query %s" % sid)
  if sid not in storage:
    return []
  return storage[sid]

def reset(sid):
  global storage
  print("[DATABASE] Reset %s" % sid)
  storage.pop(sid, None)

def delete(sid, name):
  global storage
  print("[DATABASE] Deleting SID %s - name %s" % (sid, name))
  if sid not in storage:
    print("[DATABASE] Error - SID %s does not exist" % sid)
    return False
  if name not in storage[sid]:
    print("[DATABASE] Error - %s does not exist in SID %s" % (name, sid))
    return False
  storage[sid].pop(name, None)
  print("[DATABASE] Deleted - SID %s - name %s" % (sid, name))
  return True

def persist():
  global storage
  f = open(FILE, "w")
  f.write(yaml.safe_dump(storage))
  print("[DATABASE] Persist data to %s" % FILE)
  f.close()

def load():
  global storage
  f = open(FILE, "r")
  storage = yaml.safe_load(f.read())
  print("[DATABASE] Load data from %s" % FILE)
  f.close()
