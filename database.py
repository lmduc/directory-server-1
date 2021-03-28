import yaml, threading

FILE = "database.yaml"

storage = {}
mutex = threading.Lock()

def create(sid, name, value):
  global storage
  global mutex

  print("[DATABASE] Creating SID %s - name %s" % (sid, name))

  mutex.acquire()
  try:
    if sid not in storage:
      storage[sid] = {}
    if name in storage[sid]:
      print("[DATABASE] Error - %s already exits in SID %s" % (name, sid))
      return False
    storage[sid][name] = value
  finally:
    mutex.release()
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
  global mutex

  mutex.acquire()
  try:
    print("[DATABASE] Reset %s" % sid)
    storage.pop(sid, None)
  finally:
    mutex.release()

def delete(sid, name):
  global storage
  global mutex

  print("[DATABASE] Deleting SID %s - name %s" % (sid, name))

  mutex.acquire()
  try:
    if sid not in storage:
      print("[DATABASE] Error - SID %s does not exist" % sid)
      return False
    if name not in storage[sid]:
      print("[DATABASE] Error - %s does not exist in SID %s" % (name, sid))
      return False
    storage[sid].pop(name, None)
  finally:
    mutex.release()
  print("[DATABASE] Deleted - SID %s - name %s" % (sid, name))
  return True

def persist():
  global storage
  global mutex

  mutex.acquire()
  try:
    f = open(FILE, "w")
    f.write(yaml.safe_dump(storage))
  finally:
    mutex.release()
    f.close()
  print("[DATABASE] Persist data to %s" % FILE)

def load():
  global storage
  global mutex

  f = open(FILE, "r")
  mutex.acquire()
  try:
    storage = yaml.safe_load(f.read())
  finally:
    mutex.release()
    f.close()
  print("[DATABASE] Load data from %s" % FILE)
