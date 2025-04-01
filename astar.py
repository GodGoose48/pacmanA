from search import Search
import heapq
from maze import Maze

class AStar(Search):
    def search(self, g: Maze, src: tuple, dst: tuple) -> tuple:
        expanded = []
        all_foods = list(g.get_all_goals()) 
        
        if not all_foods:
            return expanded, []

        final_path = []
        current_pos = src
        
        remaining_foods = set(all_foods)
        pie_locations = set(g.pies_nodes)
        power_mode_steps = 0
        
        while remaining_foods:
            closest_food, path_to_food, new_power_steps = self.find_closest_food(
                g, current_pos, remaining_foods, pie_locations, power_mode_steps
            )
            
            if not path_to_food: 
                break
            if final_path:
                final_path.extend(path_to_food[1:])
            else:
                final_path.extend(path_to_food)
        
            current_pos = closest_food
            if closest_food in remaining_foods:
                remaining_foods.remove(closest_food)
            
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