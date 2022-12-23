import rpyc
from constRPYC import * #-

class Client:
  conn = rpyc.connect(SERVER, PORT)

  print (conn.root.exposed_value())

  conn.root.exposed_append(6)
  conn.root.exposed_append(4)
  conn.root.exposed_append(3)
  conn.root.exposed_append(2)
  conn.root.exposed_append(1)
  print (conn.root.exposed_value())

  conn.root.exposed_insert(2, 5)
  conn.root.exposed_insert(6, 0)
  print (conn.root.exposed_value())

  conn.root.exposed_sort()
  print (conn.root.exposed_value())

  conn.root.exposed_reverse()
  print (conn.root.exposed_value())
  
  p = conn.root.exposed_search(4)
  print(p)
  print(conn.root.exposed_get(p))

  print(conn.root.exposed_length())

  conn.root.exposed_remove_idx(p)
  print (conn.root.exposed_value())

  conn.root.exposed_remove_idx(2)
  print (conn.root.exposed_value())
  
  conn.root.exposed_remove_value(1)
  print (conn.root.exposed_value())