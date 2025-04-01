from search import Search
import heapq
from maze import Maze

class AStar(Search):
    """
    def search(self, g: Maze, src: tuple, dst: tuple) -> tuple:
        expanded = []  
        path = {}  
        pq = []  
        heapq.heappush(pq, (0, src, 0))  

        g_cost = {src: 0}  
        came_from = {src: None}  
        power_mode = {src: 0}

        while pq:
            _, current, steps_left = heapq.heappop(pq)

            if current in expanded:
                continue

            expanded.append(current)

            if current == dst:
                path = []
                while current is not None:
                    path.append(current)
                    current = came_from[current]
                path.reverse()
                return expanded, path

            if g.is_bonus(current):
                steps_left = 5  

            for neighbor in g.get_neighbors(current):
                new_g = g_cost[current] + g.get_cost(current, neighbor)

                if neighbor not in g_cost or new_g < g_cost[neighbor]:
                    g_cost[neighbor] = new_g
                    f = new_g + self.heuristic(neighbor, dst)
                    heapq.heappush(pq, (f, neighbor, max(steps_left - 1, 0)))  # Giảm số bước xuyên tường
                    came_from[neighbor] = current  

        return expanded, []  
    """
    # def search(self, g: Maze, src: tuple, dst: tuple) -> tuple:
    #     expanded = []  # list of expanded vertices in the traversal order
    #     path = []  # path from src to dst
        
    #     # Open list (priority queue)
    #     open_list = []
    #     heapq.heappush(open_list, (0 + self.heuristic(src, dst), 0, src, []))  # (f, g, node, path)

    #     # Closed set to avoid revisiting nodes
    #     closed = set()

    #     while open_list:
    #         # Get node with the lowest f value (f = g + h)
    #         f, g, current_node, current_path = heapq.heappop(open_list)

    #         # Ensure current_node is a tuple (r, c)
    #         if not isinstance(current_node, tuple) or len(current_node) != 2:
    #             continue  # Skip if current_node is not a valid tuple (r, c)

    #         # Check if we reached the goal
    #         if current_node == dst:
    #             return current_path, g  # Return path and cost

    #         # Skip if node has been expanded
    #         if current_node in closed:
    #             continue
    #         closed.add(current_node)

    #         # Expand node by checking its neighbors
    #         for neighbor in g.get_neighbors(current_node):  # Ensure current_node is a tuple (r, c)
    #             # Apply teleport logic when reaching a corner
    #             new_neighbor = g.teleport(current_node, neighbor)

    #             # Calculate cost for neighbor
    #             new_g = g + 1  # Assuming each step has cost 1
    #             h = self.heuristic(new_neighbor, dst)
    #             new_f = new_g + h
                
    #             # Add to open list
    #             heapq.heappush(open_list, (new_f, new_g, new_neighbor, current_path + [new_neighbor]))

    #         expanded.append(current_node)

    #     return None, None  # Return None if no path found


# def search(self, g: Maze, src: tuple, dst: tuple) -> tuple:
#     expanded = []
#     path = []
#     open_list = []

#     # Push (f, cost, node, path) instead of (f, g, node, path)
#     heapq.heappush(open_list, (self.heuristic(src, dst), 0, src, []))

#     closed = set()

#     while open_list:
#         f, cost, current_node, current_path = heapq.heappop(open_list)

#         if not isinstance(current_node, tuple) or len(current_node) != 2:
#             continue

#         if current_node == dst:
#             return current_path, cost

#         if current_node in closed:
#             continue
#         closed.add(current_node)

#         for neighbor in g.get_neighbors(current_node):
#             new_neighbor = g.teleport(current_node, neighbor)
#             new_cost = cost + 1
#             h = self.heuristic(new_neighbor, dst)
#             new_f = new_cost + h

#             heapq.heappush(
#                 open_list,
#                 (new_f, new_cost, new_neighbor, current_path + [new_neighbor])
#             )

#         expanded.append(current_node)

#     return None, None

    def search(self, g: Maze, src: tuple, dst: tuple) -> tuple:
        expanded = []
        path = {}
        pq = []
        heapq.heappush(pq, (0, src, 0))

        g_cost = {src: 0}
        came_from = {src: None}

        while pq:
            _, current, steps_left = heapq.heappop(pq)

            # Sync steps_left with Maze's power mode
            g.power_mode_steps = steps_left

            if current in expanded:
                continue
            expanded.append(current)

            if current == dst:
                path = []
                while current is not None:
                    path.append(current)
                    current = came_from[current]
                path.reverse()
                return expanded, path

            # If bonus pie is found, reset to 5 steps
            if g.is_bonus(current):
                g.power_mode_steps = 5
                

            for neighbor in g.get_neighbors(current):
                new_cost = g_cost[current] + g.get_cost(current, neighbor)
                if neighbor not in g_cost or new_cost < g_cost[neighbor]:
                    g_cost[neighbor] = new_cost
                    f = new_cost + self.heuristic(neighbor, dst)
                    heapq.heappush(pq, (f, neighbor, max(steps_left - 1, 0)))
                    came_from[neighbor] = current

        return expanded, []


    def heuristic(self, node, goal):
        """Sử dụng khoảng cách Manhattan làm heuristic"""
        return abs(node[0] - goal[0]) + abs(node[1] - goal[1])
