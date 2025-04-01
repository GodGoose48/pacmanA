class Maze:
    def __init__(self, layout_file):
        self.layout = self.load_layout(layout_file)
        self.rows = len(self.layout)
        self.cols = len(self.layout[0]) if self.rows > 0 else 0

        self.start_node = None
        self.foods_nodes = set()
        self.pies_nodes = set()
        self.walls = set()
        self.power_mode_steps = 0

        for r in range(self.rows):
            for c in range(self.cols):
                char = self.layout[r][c]
                if char == 'P':
                    self.start_node = (r, c)
                elif char == '.':
                    self.foods_nodes.add((r, c))
                elif char == 'O':
                    self.pies_nodes.add((r, c))
                elif char == '%':
                    self.walls.add((r, c))

        self.corners = [(1, 1), (1, self.cols - 2), (self.rows - 2, 1), (self.rows - 2, self.cols - 2)]
        # self.opposite_corners = {corner: self.corners[3 - i] for i, corner in enumerate(self.corners)}

    def load_layout(self, layout_file):
        with open(layout_file, 'r') as f:
            return [list(line.strip()) for line in f]

    # def find_char(self, char):
    #     for r in range(self.rows):
    #         for c in range(self.cols):
    #             if self.layout[r][c] == char:
    #                 return (r, c)
    #     return None

    # def find_all_char(self, char):
    #     locations = []
    #     for r in range(self.rows):
    #         for c in range(self.cols):
    #             if self.layout[r][c] == char:
    #                 locations.append((r, c))
        # return locations
        
    # def get_neighbors(self, node):
    #     r, c = node
    #     directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    #     return [(r + dr, c + dc) for dr, dc in directions if self.is_valid_move(r + dr, c + dc)]
    
    # def get_neighbors(self, node):
    #     # Ensure node is a tuple (r, c)
    #     if not isinstance(node, tuple) or len(node) != 2:
    #         return []  # Return empty list if node is not valid

    #     r, c = node
    #     directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Các hướng đi cơ bản: phải, xuống, trái, lên
    #     neighbors = []

    #     for dr, dc in directions:
    #         new_r, new_c = r + dr, c + dc
    #         if self.is_valid_move(new_r, new_c):
    #             neighbors.append((new_r, new_c))

    #     # Kiểm tra teleport ở các góc và thêm node sau teleport nếu cần
    #     for direction in ["UP", "DOWN", "LEFT", "RIGHT"]:
    #         teleport_node = self.teleport(node, direction)
    #         if teleport_node != node and teleport_node not in neighbors:
    #             neighbors.append(teleport_node)

    #     return neighbors

    def is_wall(self, pos):
        r, c = pos
        return self.layout[r][c] == '%'


    # Problem
    def get_start_node(self):
        return self.start_node
    
    def is_goal(self, node):
        return node in self.foods_nodes

    def get_all_goals(self):
        return self.foods_nodes

    def is_bonus(self, node):
        return node in self.pies_nodes
    
    def get_cost(self, node1, node2):
        return 1

    
    # def is_valid_move(self, x, y, can_go_through_walls=False):
    #     if not (0 <= x < self.rows and 0 <= y < self.cols):
    #         return False 

    #     if not can_go_through_walls and (x, y) in self.walls:
    #         return False 

    #     return True
    def is_valid_move(self, x, y):
        if not (0 <= x < self.rows and 0 <= y < self.cols):
            return False 

        if self.power_mode_steps > 0:
            return True  
        
        return (x, y) not in self.walls 
    
    def decrement_power_mode(self):
        if self.power_mode_steps > 0:
            self.power_mode_steps -= 1

    def teleport(self, current_pos, direction):
        if current_pos not in self.corners:
            return current_pos
            
        # Top-left
        if current_pos == (1, 1):
            if direction == "UP": 
                return (self.rows - 1, 1)  
            elif direction == "LEFT": 
                return (1, self.cols - 1)  
        
        # Top-right
        elif current_pos == (1, self.cols - 2):
            if direction == "UP":
                return (self.rows - 1, self.cols - 2)  
            elif direction == "RIGHT":  
                return (1, 0)  
        
        # Bottom-left  
        elif current_pos == (self.rows - 2, 1):
            if direction == "DOWN":  
                return (0, 1) 
            elif direction == "LEFT": 
                return (self.rows - 2, self.cols - 1)  
        
        # Bottom-right 
        elif current_pos == (self.rows - 2, self.cols - 2):
            if direction == "DOWN":  
                return (0, self.cols - 2)  
            elif direction == "RIGHT":  
                return (self.rows - 2, 0)  
    
        return current_pos
