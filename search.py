from maze import Maze

class Search:
  def search(self, g: Maze, src: int, dst: int) -> tuple:
    expanded = [] # list of expanded vertices in the traversal order
    path = [] # path from src to dst
    return expanded, path