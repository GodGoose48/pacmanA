# from search import Search
# import heapq
# from maze import Maze

# class AStar(Search):
#     """
#     def search(self, g: Maze, src: tuple, dst: tuple) -> tuple:
#         expanded = []  
#         path = {}  
#         pq = []  
#         heapq.heappush(pq, (0, src, 0))  

#         g_cost = {src: 0}  
#         came_from = {src: None}  
#         power_mode = {src: 0}

#         while pq:
#             _, current, steps_left = heapq.heappop(pq)

#             if current in expanded:
#                 continue

#             expanded.append(current)

#             if current == dst:
#                 path = []
#                 while current is not None:
#                     path.append(current)
#                     current = came_from[current]
#                 path.reverse()
#                 return expanded, path

#             if g.is_bonus(current):
#                 steps_left = 5  

#             for neighbor in g.get_neighbors(current):
#                 new_g = g_cost[current] + g.get_cost(current, neighbor)

#                 if neighbor not in g_cost or new_g < g_cost[neighbor]:
#                     g_cost[neighbor] = new_g
#                     f = new_g + self.heuristic(neighbor, dst)
#                     heapq.heappush(pq, (f, neighbor, max(steps_left - 1, 0)))  # Giảm số bước xuyên tường
#                     came_from[neighbor] = current  

#         return expanded, []  
#     """
#     # def search(self, g: Maze, src: tuple, dst: tuple) -> tuple:
#     #     expanded = []  # list of expanded vertices in the traversal order
#     #     path = []  # path from src to dst
        
#     #     # Open list (priority queue)
#     #     open_list = []
#     #     heapq.heappush(open_list, (0 + self.heuristic(src, dst), 0, src, []))  # (f, g, node, path)

#     #     # Closed set to avoid revisiting nodes
#     #     closed = set()

#     #     while open_list:
#     #         # Get node with the lowest f value (f = g + h)
#     #         f, g, current_node, current_path = heapq.heappop(open_list)

#     #         # Ensure current_node is a tuple (r, c)
#     #         if not isinstance(current_node, tuple) or len(current_node) != 2:
#     #             continue  # Skip if current_node is not a valid tuple (r, c)

#     #         # Check if we reached the goal
#     #         if current_node == dst:
#     #             return current_path, g  # Return path and cost

#     #         # Skip if node has been expanded
#     #         if current_node in closed:
#     #             continue
#     #         closed.add(current_node)

#     #         # Expand node by checking its neighbors
#     #         for neighbor in g.get_neighbors(current_node):  # Ensure current_node is a tuple (r, c)
#     #             # Apply teleport logic when reaching a corner
#     #             new_neighbor = g.teleport(current_node, neighbor)

#     #             # Calculate cost for neighbor
#     #             new_g = g + 1  # Assuming each step has cost 1
#     #             h = self.heuristic(new_neighbor, dst)
#     #             new_f = new_g + h
                
#     #             # Add to open list
#     #             heapq.heappush(open_list, (new_f, new_g, new_neighbor, current_path + [new_neighbor]))

#     #         expanded.append(current_node)

#     #     return None, None  # Return None if no path found


# # def search(self, g: Maze, src: tuple, dst: tuple) -> tuple:
# #     expanded = []
# #     path = []
# #     open_list = []

# #     # Push (f, cost, node, path) instead of (f, g, node, path)
# #     heapq.heappush(open_list, (self.heuristic(src, dst), 0, src, []))

# #     closed = set()

# #     while open_list:
# #         f, cost, current_node, current_path = heapq.heappop(open_list)

# #         if not isinstance(current_node, tuple) or len(current_node) != 2:
# #             continue

# #         if current_node == dst:
# #             return current_path, cost

# #         if current_node in closed:
# #             continue
# #         closed.add(current_node)

# #         for neighbor in g.get_neighbors(current_node):
# #             new_neighbor = g.teleport(current_node, neighbor)
# #             new_cost = cost + 1
# #             h = self.heuristic(new_neighbor, dst)
# #             new_f = new_cost + h

# #             heapq.heappush(
# #                 open_list,
# #                 (new_f, new_cost, new_neighbor, current_path + [new_neighbor])
# #             )

# #         expanded.append(current_node)

# #     return None, None

#     def search(self, g: Maze, src: tuple, dst: tuple) -> tuple:
#         expanded = []
#         path = {}
#         pq = []
#         heapq.heappush(pq, (0, src, 0))

#         g_cost = {src: 0}
#         came_from = {src: None}

#         while pq:
#             _, current, steps_left = heapq.heappop(pq)

#             # Sync steps_left with Maze's power mode
#             g.power_mode_steps = steps_left

#             if current in expanded:
#                 continue
#             expanded.append(current)

#             if current == dst:
#                 path = []
#                 while current is not None:
#                     path.append(current)
#                     current = came_from[current]
#                 path.reverse()
#                 return expanded, path

#             # If bonus pie is found, reset to 5 steps
#             if g.is_bonus(current):
#                 g.power_mode_steps = 5
                

#             for neighbor in g.get_neighbors(current):
#                 new_cost = g_cost[current] + g.get_cost(current, neighbor)
#                 if neighbor not in g_cost or new_cost < g_cost[neighbor]:
#                     g_cost[neighbor] = new_cost
#                     f = new_cost + self.heuristic(neighbor, dst)
#                     heapq.heappush(pq, (f, neighbor, max(steps_left - 1, 0)))
#                     came_from[neighbor] = current

#         return expanded, []


#     def heuristic(self, node, goal):
#         """Sử dụng khoảng cách Manhattan làm heuristic"""
#         return abs(node[0] - goal[0]) + abs(node[1] - goal[1])

# from search import Search
# import heapq
# from maze import Maze

# class AStar(Search):
#     def search(self, g: Maze, src: tuple, dst: tuple) -> tuple:
#         """
#         Modified A* search to find paths to all food points with special abilities:
#         - Power mode: Can go through walls for 5 steps after eating a pie
#         - Teleportation: Can teleport at corners
        
#         Args:
#             g (Maze): The maze object
#             src (tuple): Starting position (r, c)
#             dst (tuple): Not used in this implementation as we need to visit all food points
            
#         Returns:
#             tuple: (expanded nodes, final path)
#         """
#         # Initialize variables
#         expanded = []
#         all_foods = list(g.get_all_goals())  # All food points to eat
        
#         # If no food, return empty path
#         if not all_foods:
#             return expanded, []

#         # Store the complete path from the starting position to all food points
#         final_path = []
#         current_pos = src
        
#         # Keep track of remaining food points
#         remaining_foods = set(all_foods)
        
#         # Continue until all food points are eaten
#         while remaining_foods:
#             # Find the closest food point from current position
#             closest_food, path_to_food = self.find_closest_food(g, current_pos, remaining_foods)
            
#             if not path_to_food:  # If no path found to any remaining food
#                 break
                
#             # Add the path to the final path (excluding the starting position to avoid duplicates)
#             if final_path:
#                 final_path.extend(path_to_food[1:])
#             else:
#                 final_path.extend(path_to_food)
                
#             # Update the current position and remove the eaten food
#             current_pos = closest_food
#             remaining_foods.remove(closest_food)
            
#             # Add nodes to expanded (excluding duplicates)
#             for node in path_to_food:
#                 if node not in expanded:
#                     expanded.append(node)
        
#         return expanded, final_path
    
#     def find_closest_food(self, g: Maze, start: tuple, food_points: set) -> tuple:
#         """
#         Find the closest food point and the path to it using A* search
        
#         Args:
#             g (Maze): The maze object
#             start (tuple): Starting position
#             food_points (set): Set of remaining food points
            
#         Returns:
#             tuple: (closest food position, path to that food)
#         """
#         pq = []  # Priority queue
#         g_cost = {start: 0}  # Cost from start to current node
#         came_from = {start: None}  # Parent pointers for path reconstruction
#         expanded = set()  # Set of expanded nodes
        
#         # Track power mode steps for each state
#         power_steps = {start: g.power_mode_steps}
        
#         # Push starting state to the queue: (f-value, g-value, position, power_steps)
#         heapq.heappush(pq, (0, 0, start, g.power_mode_steps))
        
#         closest_food = None
#         path_to_food = []
        
#         while pq:
#             _, cost, current, steps_left = heapq.heappop(pq)
            
#             # Skip if already expanded
#             if current in expanded:
#                 continue
                
#             expanded.add(current)
            
#             # Check if we found a food point
#             if current in food_points:
#                 closest_food = current
                
#                 # Reconstruct path
#                 path_to_food = []
#                 while current is not None:
#                     path_to_food.append(current)
#                     current = came_from[current]
#                 path_to_food.reverse()
#                 break
            
#             # Update power mode if we found a pie
#             current_power = steps_left
#             if g.is_bonus(current):
#                 current_power = 5  # Reset power mode steps
            
#             # Check neighboring positions
#             for neighbor in self.get_valid_neighbors(g, current, current_power):
#                 # Check if it's a teleport position
#                 for direction in ["UP", "DOWN", "LEFT", "RIGHT"]:
#                     teleport_result = g.teleport(current, direction)
#                     if teleport_result != current:
#                         if teleport_result not in expanded:
#                             teleport_cost = cost + 1
#                             if teleport_result not in g_cost or teleport_cost < g_cost[teleport_result]:
#                                 g_cost[teleport_result] = teleport_cost
#                                 came_from[teleport_result] = current
#                                 power_after_teleport = current_power
#                                 f_n = teleport_cost + self.heuristic(teleport_result, self.get_closest_food(teleport_result, food_points))
#                                 heapq.heappush(pq, (f_n, teleport_cost, teleport_result, power_after_teleport))

#                 # Calculate cost to neighbor
#                 new_cost = cost + g.get_cost(current, neighbor)
                
#                 # If better path found
#                 if neighbor not in g_cost or new_cost < g_cost[neighbor]:
#                     g_cost[neighbor] = new_cost
#                     came_from[neighbor] = current
                    
#                     # Decrease power steps by 1 (minimum 0)
#                     power_after_move = max(0, current_power - 1)
                    
#                     # Calculate f-value using minimum distance to any food point
#                     f_n = new_cost + self.heuristic(neighbor, self.get_closest_food(neighbor, food_points))
                    
#                     heapq.heappush(pq, (f_n, new_cost, neighbor, power_after_move))
        
#         return closest_food, path_to_food
    
#     def get_valid_neighbors(self, g: Maze, pos: tuple, power_steps: int) -> list:
#         """Get valid neighbors considering power mode"""
#         r, c = pos
#         directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Right, Down, Left, Up
#         neighbors = []
        
#         for dr, dc in directions:
#             new_r, new_c = r + dr, c + dc
            
#             # Check if position is within maze bounds
#             if 0 <= new_r < g.rows and 0 <= new_c < g.cols:
#                 # Can go through walls in power mode
#                 if power_steps > 0 or (new_r, new_c) not in g.walls:
#                     neighbors.append((new_r, new_c))
        
#         return neighbors
    
#     def get_closest_food(self, pos: tuple, food_points: set) -> tuple:
#         """Find the closest food point using Manhattan distance"""
#         if not food_points:
#             return pos  # Return current position if no food points left
            
#         closest = min(food_points, key=lambda food: self.heuristic(pos, food))
#         return closest
    
#     def heuristic(self, node: tuple, goal: tuple) -> int:
#         """Manhattan distance heuristic"""
#         return abs(node[0] - goal[0]) + abs(node[1] - goal[1])

# from search import Search
# import heapq
# from maze import Maze

# class AStar(Search):
#     def search(self, g: Maze, src: tuple, dst: tuple) -> tuple:
#         """
#         Modified A* search to find paths to all food points with special abilities:
#         - Power mode: Can go through walls for 5 steps after eating a pie
#         - Teleportation: Can teleport at corners
        
#         Args:
#             g (Maze): The maze object
#             src (tuple): Starting position (r, c)
#             dst (tuple): Not used in this implementation as we need to visit all food points
            
#         Returns:
#             tuple: (expanded nodes, final path)
#         """
#         # Initialize variables
#         expanded = []
#         all_foods = list(g.get_all_goals())  # All food points to eat
        
#         # If no food, return empty path
#         if not all_foods:
#             return expanded, []

#         # Store the complete path from the starting position to all food points
#         final_path = []
#         current_pos = src
        
#         # Keep track of remaining food points
#         remaining_foods = set(all_foods)
        
#         # Keep track of power mode steps
#         power_mode_steps = 0
        
#         # Continue until all food points are eaten
#         while remaining_foods:
#             # Find the closest food point from current position
#             closest_food, path_to_food = self.find_closest_food(g, current_pos, remaining_foods, power_mode_steps)
            
#             if not path_to_food:  # If no path found to any remaining food
#                 break
                
#             # Add the path to the final path (excluding the starting position to avoid duplicates)
#             if final_path:
#                 final_path.extend(path_to_food[1:])
#             else:
#                 final_path.extend(path_to_food)
                
#             # Update the current position and remove the eaten food
#             current_pos = closest_food
#             if closest_food in remaining_foods:
#                 remaining_foods.remove(closest_food)
            
#             # Update power mode steps - check if we've eaten a pie along the path
#             for pos in path_to_food:
#                 if g.is_bonus(pos):
#                     power_mode_steps = 5
#                     g.pies_nodes.remove(pos)  # Remove eaten pie
#                     break
            
#             # Add nodes to expanded (excluding duplicates)
#             for node in path_to_food:
#                 if node not in expanded:
#                     expanded.append(node)
            
#             # Decrease power mode steps
#             power_mode_steps = max(0, power_mode_steps - len(path_to_food))
        
#         # Convert final path to movement actions
#         actions = self.convert_path_to_actions(final_path)
        
#         return expanded, actions
    
#     def find_closest_food(self, g: Maze, start: tuple, food_points: set, initial_power_steps: int) -> tuple:
#         """
#         Find the closest food point and the path to it using A* search
        
#         Args:
#             g (Maze): The maze object
#             start (tuple): Starting position
#             food_points (set): Set of remaining food points
#             initial_power_steps (int): Initial power mode steps
            
#         Returns:
#             tuple: (closest food position, path to that food)
#         """
#         pq = []  # Priority queue
#         g_cost = {start: 0}  # Cost from start to current node
#         came_from = {start: None}  # Parent pointers for path reconstruction
#         expanded = set()  # Set of expanded nodes
        
#         # Track power mode steps for each state
#         power_steps = {start: initial_power_steps}
        
#         # Push starting state to the queue: (f-value, g-value, position, power_steps)
#         heapq.heappush(pq, (0, 0, start, initial_power_steps))
        
#         closest_food = None
#         path_to_food = []
        
#         while pq:
#             _, cost, current, steps_left = heapq.heappop(pq)
            
#             # Skip if already expanded
#             if current in expanded:
#                 continue
                
#             expanded.add(current)
            
#             # Check if we found a food point
#             if current in food_points:
#                 closest_food = current
                
#                 # Reconstruct path
#                 path_to_food = []
#                 while current is not None:
#                     path_to_food.append(current)
#                     current = came_from[current]
#                 path_to_food.reverse()
#                 break
            
#             # Update power mode if we found a pie
#             current_power = steps_left
#             if g.is_bonus(current):
#                 current_power = 5  # Reset power mode steps
            
#             # Get valid neighbors considering walls and power mode
#             neighbors = self.get_valid_neighbors(g, current, current_power)
            
#             # Process normal neighbors
#             for neighbor in neighbors:
#                 # Calculate cost to neighbor
#                 new_cost = cost + g.get_cost(current, neighbor)
                
#                 # If better path found
#                 if neighbor not in g_cost or new_cost < g_cost[neighbor]:
#                     g_cost[neighbor] = new_cost
#                     came_from[neighbor] = current
                    
#                     # Decrease power steps by 1 (minimum 0)
#                     power_after_move = max(0, current_power - 1)
                    
#                     # Calculate f-value using minimum distance to any food point
#                     f_n = new_cost + self.heuristic(neighbor, self.get_closest_food(neighbor, food_points))
                    
#                     heapq.heappush(pq, (f_n, new_cost, neighbor, power_after_move))
            
#             # Check for teleport opportunities
#             if current in g.corners:
#                 for direction in ["UP", "DOWN", "LEFT", "RIGHT"]:
#                     teleport_result = g.teleport(current, direction)
#                     if teleport_result != current:
#                         # If better path found through teleport
#                         teleport_cost = cost + 1
#                         if teleport_result not in g_cost or teleport_cost < g_cost[teleport_result]:
#                             g_cost[teleport_result] = teleport_cost
#                             came_from[teleport_result] = current
                            
#                             # Power mode is unchanged by teleportation
#                             f_n = teleport_cost + self.heuristic(teleport_result, self.get_closest_food(teleport_result, food_points))
#                             heapq.heappush(pq, (f_n, teleport_cost, teleport_result, current_power))
        
#         return closest_food, path_to_food
    
#     def get_valid_neighbors(self, g: Maze, pos: tuple, power_steps: int) -> list:
#         """Get valid neighbors considering power mode"""
#         r, c = pos
#         directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Right, Down, Left, Up
#         neighbors = []
        
#         for dr, dc in directions:
#             new_r, new_c = r + dr, c + dc
            
#             # Check if position is within maze bounds
#             if 0 <= new_r < g.rows and 0 <= new_c < g.cols:
#                 # Can go through walls in power mode
#                 if power_steps > 0 or (new_r, new_c) not in g.walls:
#                     neighbors.append((new_r, new_c))
        
#         return neighbors
    
#     def get_closest_food(self, pos: tuple, food_points: set) -> tuple:
#         """Find the closest food point using Manhattan distance"""
#         if not food_points:
#             return pos  # Return current position if no food points left
            
#         closest = min(food_points, key=lambda food: self.heuristic(pos, food))
#         return closest
    
#     def heuristic(self, node: tuple, goal: tuple) -> int:
#         """Manhattan distance heuristic"""
#         return abs(node[0] - goal[0]) + abs(node[1] - goal[1])
    
#     def convert_path_to_actions(self, path: list) -> list:
#         """
#         Convert a path of coordinates to a list of movement actions
        
#         Args:
#             path (list): List of coordinates (r, c)
            
#         Returns:
#             list: List of actions ('UP', 'DOWN', 'LEFT', 'RIGHT', 'TELEPORT')
#         """
#         if not path or len(path) < 2:
#             return []
            
#         actions = []
#         for i in range(1, len(path)):
#             prev_pos = path[i-1]
#             curr_pos = path[i]
            
#             # Check for teleportation
#             if abs(prev_pos[0] - curr_pos[0]) > 1 or abs(prev_pos[1] - curr_pos[1]) > 1:
#                 actions.append(f"TELEPORT from {prev_pos} to {curr_pos}")
#             else:
#                 # Regular movement
#                 if curr_pos[0] < prev_pos[0]:
#                     actions.append("UP")
#                 elif curr_pos[0] > prev_pos[0]:
#                     actions.append("DOWN")
#                 elif curr_pos[1] < prev_pos[1]:
#                     actions.append("LEFT")
#                 elif curr_pos[1] > prev_pos[1]:
#                     actions.append("RIGHT")
        
#         return actions


# from search import Search
# import heapq
# from maze import Maze

# class AStar(Search):
#     def search(self, g: Maze, src: tuple, dst: tuple) -> tuple:
#         expanded = []
#         all_foods = list(g.get_all_goals())  # All food points to eat
        
#         if not all_foods:
#             return expanded, []

#         # Store the complete path from the starting position to all food points
#         final_path = []
#         current_pos = src
        
#         # Keep track of remaining food points and pie locations
#         remaining_foods = set(all_foods)
#         pie_locations = set(g.pies_nodes)
        
#         # Keep track of power mode steps
#         power_mode_steps = 0
        
#         # Continue until all food points are eaten
#         while remaining_foods:
#             # Find the closest food point from current position
#             closest_food, path_to_food, new_power_steps = self.find_closest_food(
#                 g, current_pos, remaining_foods, pie_locations, power_mode_steps
#             )
            
#             if not path_to_food:  # If no path found to any remaining food
#                 break
                
#             # Add the path to the final path (excluding the starting position to avoid duplicates)
#             if final_path:
#                 final_path.extend(path_to_food[1:])
#             else:
#                 final_path.extend(path_to_food)
            
#             # Update the current position
#             current_pos = path_to_food[-1]
            
#             # Remove eaten food
#             if current_pos in remaining_foods:
#                 remaining_foods.remove(current_pos)
            
#             # Check each position in the path for pies and update power mode
#             for pos in path_to_food:
#                 if pos in pie_locations:
#                     power_mode_steps = 5  # Reset power mode steps
#                     pie_locations.remove(pos)  # Remove eaten pie
#                 else:
#                     power_mode_steps = max(0, power_mode_steps - 1)  # Decrease power mode steps
            
#             # Add nodes to expanded (excluding duplicates)
#             for node in path_to_food:
#                 if node not in expanded:
#                     expanded.append(node)
        
#         # Convert final path to movement actions
#         actions = self.convert_path_to_actions(final_path, g.walls)
#         print(f"Actions: {actions}")
        
#         return expanded, actions
    
#     def find_closest_food(self, g: Maze, start: tuple, food_points: set, pie_locations: set, initial_power_steps: int) -> tuple:
#         pq = []  # Priority queue

#         start_state = (start, initial_power_steps)
        
#         g_cost = {start_state: 0}  # Cost from start to current state
#         came_from = {start_state: None}  # Parent pointers for path reconstruction
#         expanded = set()  # Set of expanded states
        
#         # Calculate initial f value
#         f_n =  min([self.heuristic(start, food) for food in food_points]) if food_points else 0
        
#         # Push starting state to the queue: (f-value, g-value, position, power_steps)
#         heapq.heappush(pq, (f_n, 0, start, initial_power_steps))
        
#         closest_food = None
#         path_to_food = []
#         ending_power_steps = 0
        
#         while pq:
#             _, cost, current, steps_left = heapq.heappop(pq)
            
#             current_state = (current, steps_left)
            
#             # Skip if already expanded
#             if current_state in expanded:
#                 continue
                
#             expanded.add(current_state)
            
#             # Check if we found a food point
#             if current in food_points:
#                 closest_food = current
#                 ending_power_steps = steps_left
                
#                 # Reconstruct path
#                 path_to_food = []
#                 current_state = (current, steps_left)
#                 while current_state is not None:
#                     path_to_food.append(current_state[0])  # Add just the position
#                     current_state = came_from[current_state]
#                 path_to_food.reverse()
#                 break
            
#             # Update power mode if we found a pie
#             current_power = steps_left
#             if current in pie_locations:
#                 current_power = 5  # Reset power mode steps
            
#             # Get valid neighbors considering walls and power mode
#             neighbors = self.get_valid_neighbors(g, current, current_power)
            
#             # Process normal neighbors
#             for neighbor in neighbors:
#                 # Calculate new power steps - decreases by 1 for each move
#                 new_power = current_power
#                 if neighbor in pie_locations:
#                     new_power = 5 
#                 else:
#                     new_power = max(0, new_power - 1)  # Decrease power steps
                
#                 neighbor_state = (neighbor, new_power)
                
#                 # Calculate cost to neighbor
#                 new_cost = cost + g.get_cost(current, neighbor)
                
#                 # If better path found
#                 if neighbor_state not in g_cost or new_cost < g_cost[neighbor_state]:
#                     g_cost[neighbor_state] = new_cost
#                     came_from[neighbor_state] = current_state
                    
#                     # Calculate f-value using minimum distance to any food point
#                     h_value = min([self.heuristic(neighbor, food) for food in food_points]) if food_points else 0
#                     f_n = new_cost + h_value
                    
#                     heapq.heappush(pq, (f_n, new_cost, neighbor, new_power))
            
#             if current in g.corners:
#                 for direction in ["UP", "DOWN", "LEFT", "RIGHT"]:
#                     teleport_result = g.teleport(current, direction)
#                     if teleport_result != current:
#                         teleport_state = (teleport_result, current_power) 
                        
#                         # If better path found through teleport
#                         teleport_cost = cost + 1
#                         if teleport_state not in g_cost or teleport_cost < g_cost[teleport_state]:
#                             g_cost[teleport_state] = teleport_cost
#                             came_from[teleport_state] = current_state
                            
#                             # Calculate f-value
#                             h_value = min([self.heuristic(teleport_result, food) for food in food_points]) if food_points else 0
#                             f_n = teleport_cost + h_value
                            
#                             heapq.heappush(pq, (f_n, teleport_cost, teleport_result, current_power))
#         print(f"Closest food: {closest_food}, Path to food: {path_to_food}, Ending power steps: {ending_power_steps}")
#         return closest_food, path_to_food, ending_power_steps
    
#     def get_valid_neighbors(self, g: Maze, pos: tuple, power_steps: int) -> list:

#         r, c = pos
#         directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Right, Down, Left, Up
#         neighbors = []
        
#         for dr, dc in directions:
#             new_r, new_c = r + dr, c + dc
            
#             # Check if position is within maze bounds
#             if 0 <= new_r < g.rows and 0 <= new_c < g.cols:
#                 # Can go through walls in power mode
#                 if power_steps > 0 or (new_r, new_c) not in g.walls:
#                     neighbors.append((new_r, new_c))
#         print(f"Valid neighbors for {pos} with power steps {power_steps}: {neighbors}")
        
#         return neighbors
    
#     def heuristic(self, node: tuple, goal: tuple) -> int:
#         return abs(node[0] - goal[0]) + abs(node[1] - goal[1])
    
#     def convert_path_to_actions(self, path: list, walls: set) -> list:

#         if not path or len(path) < 2:
#             return []
            
#         actions = []
#         for i in range(1, len(path)):
#             prev_pos = path[i-1]
#             curr_pos = path[i]
            
#             # Check for teleportation (non-adjacent positions)
#             if abs(prev_pos[0] - curr_pos[0]) > 1 or abs(prev_pos[1] - curr_pos[1]) > 1:
#                 actions.append(f"TELEPORT from {prev_pos} to {curr_pos}")
#             else:
#                 # Regular movement
#                 if curr_pos[0] < prev_pos[0]:
#                     action = "UP"
#                 elif curr_pos[0] > prev_pos[0]:
#                     action = "DOWN"
#                 elif curr_pos[1] < prev_pos[1]:
#                     action = "LEFT"
#                 elif curr_pos[1] > prev_pos[1]:
#                     action = "RIGHT"
#                 else:
#                     continue 

#                 if curr_pos in walls:
#                     action += " (through wall)"
                
#                 actions.append(action)
        
#         return actions

from search import Search
import heapq
from maze import Maze

class AStar(Search):
    def search(self, g: Maze, src: tuple, dst: tuple) -> tuple:
        expanded = []
        all_foods = list(g.get_all_goals())  # All food points to eat
        
        if not all_foods:
            return expanded, []

        # Store the complete path from the starting position to all food points
        final_path = []
        current_pos = src
        
        # Keep track of remaining food points and pie locations
        remaining_foods = set(all_foods)
        pie_locations = set(g.pies_nodes)
        
        # Keep track of power mode steps
        power_mode_steps = 0
        
        # Continue until all food points are eaten
        while remaining_foods:
            # Find the closest food point from current position
            closest_food, path_to_food, new_power_steps = self.find_closest_food(
                g, current_pos, remaining_foods, pie_locations, power_mode_steps
            )
            
            if not path_to_food:  # If no path found to any remaining food
                break
                
            # Add the path to the final path (excluding the starting position to avoid duplicates)
            if final_path:
                final_path.extend(path_to_food[1:])
            else:
                final_path.extend(path_to_food)
            
            # Update the current position
            current_pos = closest_food
            
            # Remove eaten food
            if closest_food in remaining_foods:
                remaining_foods.remove(closest_food)
            
            # Update power mode steps to the value after reaching the food
            power_mode_steps = new_power_steps
            
            # Update pie locations (remove any pies eaten along the path)
            for pos in path_to_food:
                if pos in pie_locations:
                    pie_locations.remove(pos)
            
            # Add nodes to expanded (excluding duplicates)
            for node in path_to_food:
                if node not in expanded:
                    expanded.append(node)
        
        # Convert final path to movement actions
        # print(final_path)
        actions = self.convert_path_to_actions(final_path, g.walls)
        return expanded, actions
    
    def find_closest_food(self, g: Maze, start: tuple, food_points: set, pie_locations: set, initial_power_steps: int) -> tuple:
        if not food_points:
            return None, [], 0
            
        pq = []  # Priority queue
        
        # Initialize with starting state: (f-value, tie-breaker, position, power_steps, path_cost)
        heapq.heappush(pq, (0, 0, start, initial_power_steps, 0))
        
        # For tracking visited states to avoid cycles
        visited = set()
        
        # For reconstructing the path
        came_from = {(start, initial_power_steps): None}
        
        # Track the best food found so far
        best_food = None
        best_path = []
        best_power_steps = 0
        best_cost = float('inf')
        
        while pq:
            _, _, current, power_steps, path_cost = heapq.heappop(pq)
            
            # Skip if already visited this state
            state = (current, power_steps)
            if state in visited:
                continue
                
            visited.add(state)
            
            # Check if we've reached a food point
            if current in food_points and path_cost < best_cost:
                best_food = current
                best_power_steps = power_steps
                best_cost = path_cost
                
                # Reconstruct path
                path = []
                curr_state = state
                while curr_state is not None:
                    path.append(curr_state[0])  # Add just the position
                    curr_state = came_from.get(curr_state)
                best_path = list(reversed(path))
                
                # We could continue searching for potentially better paths
                # but for efficiency, we can break here if desired
                # break
            
            # Get valid neighbors considering walls and power mode
            neighbors = self.get_valid_neighbors(g, current, power_steps)
            
            for neighbor, is_teleport in neighbors:
                # Calculate new power steps
                new_power = power_steps
                
                # If we find a pie, reset power mode
                if neighbor in pie_locations:
                    new_power = 5
                else:
                    # Decrease power steps by 1 unless already at 0
                    new_power = max(0, new_power - 1)
                
                # Calculate new path cost (teleport costs 1, normal move costs depend on maze)
                move_cost = 1 if is_teleport else g.get_cost(current, neighbor)
                new_cost = path_cost + move_cost
                
                # Only consider this neighbor if we haven't visited it with same or better power
                neighbor_state = (neighbor, new_power)
                if neighbor_state not in visited:
                    # Calculate heuristic - Manhattan distance to closest food
                    h_value = min([self.heuristic(neighbor, food) for food in food_points])
                    
                    # Adjust heuristic if in power mode (can go through walls)
                    if new_power > 0:
                        h_value = h_value * 0.8  
                    
                    f_value = new_cost + h_value
                    heapq.heappush(pq, (f_value, new_cost, neighbor, new_power, new_cost))
                    came_from[neighbor_state] = state
        
        return best_food, best_path, best_power_steps
    
    def get_valid_neighbors(self, g: Maze, pos: tuple, power_steps: int) -> list:
        r, c = pos
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)] 
        neighbors = []
        
        for dr, dc in directions:
            new_r, new_c = r + dr, c + dc
            
            if 0 <= new_r < g.rows and 0 <= new_c < g.cols:
                # Can go through walls in power mode
                if power_steps > 0 or (new_r, new_c) not in g.walls:
                    neighbors.append(((new_r, new_c), False))  

        if pos in g.corners:
            for direction in ["UP", "DOWN", "LEFT", "RIGHT"]:
                teleport_result = g.teleport(pos, direction)
                if teleport_result != pos: 
                    neighbors.append((teleport_result, True))  
        return neighbors
    
    def heuristic(self, node: tuple, goal: tuple) -> int:
        return abs(node[0] - goal[0]) + abs(node[1] - goal[1])
    
    def convert_path_to_actions(self, path: list, walls: set) -> list:
        actions = []
    
        if not path or len(path) < 2:
            return []
            
        for i in range(1, len(path)):
            prev_pos = path[i-1]
            curr_pos = path[i]
            
            if abs(prev_pos[0] - curr_pos[0]) > 1 or abs(prev_pos[1] - curr_pos[1]) > 1:
                continue
            else:
                if curr_pos[0] < prev_pos[0]:
                    action = "UP"
                    # print(f"Moving UP from {prev_pos} to {curr_pos}")
                elif curr_pos[0] > prev_pos[0]:
                    action = "DOWN"
                    # print(f"Moving DOWN from {prev_pos} to {curr_pos}")
                elif curr_pos[1] < prev_pos[1]:
                    action = "LEFT"
                    # print(f"Moving LEFT from {prev_pos} to {curr_pos}")
                elif curr_pos[1] > prev_pos[1]:
                    action = "RIGHT"
                    # print(f"Moving RIGHT from {prev_pos} to {curr_pos}")
                else:
                    continue 
                
            actions.append(action)
        # print(f"Actions: {actions}")
        return actions