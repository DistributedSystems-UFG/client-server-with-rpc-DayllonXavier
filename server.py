import rpyc
from constRPYC import * #-
from rpyc.utils.server import ThreadedServer

class DBList(rpyc.Service):
  value = []

  def exposed_append(self, data):
    self.value = self.value + [data]

  def exposed_value(self):
    return self.value

  def exposed_insert(self, pos, value):
    self.value = self.value[:pos] + [value] + self.value[pos:]
  
  def exposed_get(self, idx):
    return self.value[idx]
  
  def exposed_search(self, value):
    pos = -1
    for i in range(0, len(self.value)):
      if (self.value[i] == value):
        pos = i
        break
    return pos

  def exposed_remove_idx(self, pos):
    if (pos == 0):
      self.value = self.value[1:]
    elif (pos == len(self.value)-1):
      self.value = self.value[:-1]
    else:
      self.value = self.value[:pos] + self.value[pos+1:]
      
  def exposed_remove_value(self, value):
    self.exposed_remove_idx(self.exposed_search(value))

  def exposed_sort(self):
    self.value.sort()
  
  def exposed_reverse(self):
    self.value = self.value[::-1]
  
  def exposed_length(self):
    return len(self.value)

if __name__ == "__main__":
  server = ThreadedServer(DBList(), port = PORT)
  server.start()

