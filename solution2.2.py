import sys
import math

def answer(src, dest):
    """Graph + Dijkstra"""
    graph = init_graph()
    moves = get_shortest_path_or_none(graph, src, dest)
    if moves == None:
      return None
    else:
      return len(moves)

def init_graph():
    # Node: int
    # Edge: int
    # edges_of_node: int -> set(int)
    edges_of_node = {}
    for i in range(64):
      moves = get_possible_displacements(i)
      neighbours = map(lambda x: i + x, moves)
      edges_of_node[i] = set(neighbours)
    
    return edges_of_node

def get_possible_displacements(i):
    # Relative moves:
    #  #h#a#       
    #  g###b     
    #  ##X##       
    #  f###c     
    #  #e#d#     
    #
    # Relative displacements:
    a = -15
    b = -6
    c = 10
    d = 17
    e = 15
    f = 6
    g = -10
    h = -17

    # Where can i move to?
    moves = []
    column = i % 8
    row = math.floor(i / 8)
    if (row >= 2) & (column <= 6): moves.append(a)

    if (row >= 1) & (column <= 5): moves.append(b)

    if (row <= 6) & (column <= 5): moves.append(c)

    if (row <= 5) & (column <= 6): moves.append(d)

    if (row <= 5) & (column >= 1): moves.append(e)

    if (row <= 6) & (column >= 2): moves.append(f)
    
    if (row >= 1) & (column >= 2): moves.append(g)

    if (row >= 2) & (column >= 1): moves.append(h)
    
    return moves

def get_shortest_path_or_none(graph, src, dest):
    distance = dict([(x, 0) if x == src else (x, sys.maxsize) for x in graph.keys()])
    unvisited = set(graph.keys())
    previous = {}

    while (len(unvisited) != 0):
      current = min(unvisited, key=distance.get)
      unvisited.remove(current)
      
      if current == dest:
        break
      
      for neighbour in graph[current]:
        new_dist = distance[current] + 1
        if new_dist < distance[neighbour]:
          distance[neighbour] = new_dist
          previous[neighbour] = current
    
    if previous.has_key(dest):
      next = dest
      result = []
      while previous.has_key(next):
        result.insert(0, next)
        next = previous[next]

      return result

    else:
      return None

print(answer(0, 0))