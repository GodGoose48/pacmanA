# import pygame
# from maze import Maze

# class MazeGame:
#     def __init__(self, maze_file, cell_size=30):
#         pygame.init()

#         # Load maze
#         self.maze = Maze(maze_file)
#         self.cell_size = cell_size

#         # screen size
#         self.width = self.maze.cols * self.cell_size
#         self.height = self.maze.rows * self.cell_size
#         self.screen = pygame.display.set_mode((self.width, self.height))
#         pygame.display.set_caption("TASK 2 - PACMAN")

#         # Load images
#         self.images = {
#             '%': pygame.image.load("sprites/wall.png"),
#             '.': pygame.image.load("sprites/food.png"),
#             'O': pygame.image.load("sprites/bonus.png"),
#             'P': pygame.image.load("sprites/player.png"),
#             ' ': pygame.image.load("sprites/empty.png"),
#             # 'T': pygame.image.load("sprites/teleport.png") 
#         }

#         for key in self.images:
#             self.images[key] = pygame.transform.scale(self.images[key], (self.cell_size, self.cell_size))

#         # Set player start position
#         self.player_pos = self.maze.start_node
#         self.start_moved = False  

#     def draw(self):
#         self.screen.fill((0, 0, 0)) 

#         for r in range(self.maze.rows):
#             for c in range(self.maze.cols):
#                 x, y = c * self.cell_size, r * self.cell_size
#                 char = self.maze.layout[r][c]

#                 # if (r, c) in self.maze.corners:
#                 #     char = 'T'

#                 self.screen.blit(self.images.get(char, self.images[' ']), (x, y))

#         # Draw player on top
#         px, py = self.player_pos
#         self.screen.blit(self.images['P'], (py * self.cell_size, px * self.cell_size))

#         pygame.display.flip()

#     def move_player(self, direction):
#         r, c = self.player_pos
#         moves = {'UP': (-1, 0), 'DOWN': (1, 0), 'LEFT': (0, -1), 'RIGHT': (0, 1)}

#         if direction in moves:
#             new_r, new_c = r + moves[direction][0], c + moves[direction][1]

#             # Move only if it's a valid position
#             if self.maze.is_valid_move(new_r, new_c):
#                 if not self.start_moved:
#                     self.maze.layout[self.maze.start_node[0]][self.maze.start_node[1]] = ' '
#                     self.start_moved = True

#                 self.player_pos = (new_r, new_c)

#                 # Eat food (replace '.' with ' ')
#                 if self.player_pos in self.maze.foods_nodes:
#                     self.maze.foods_nodes.remove(self.player_pos)
#                     self.maze.layout[new_r][new_c] = ' ' 

#                 # Eat bonus (replace 'O' with ' ')
#                 if self.player_pos in self.maze.pies_nodes:
#                     self.maze.pies_nodes.remove(self.player_pos)
#                     self.maze.layout[new_r][new_c] = ' '  

#     # Add this method to your MazeGame class in mazeGame.py

#     def run_with_actions(self, actions):
#         running = True
#         clock = pygame.time.Clock()
        
#         for i, action in enumerate(actions):
#             if not running:
#                 break
            
#             self.draw()
#             clock.tick(5)  # Slower speed for better visualization
            
#             # Handle teleportation
#             if isinstance(action, str) and action.startswith("TELEPORT"):
#                 # Extract destination coordinates from the action string
#                 parts = action.split("to")
#                 if len(parts) == 2:
#                     dest_str = parts[1].strip()
#                     # Parse the coordinates - format is like "(r, c)"
#                     dest_str = dest_str.strip("()")
#                     dest_coords = tuple(map(int, dest_str.split(",")))
#                     self.player_pos = dest_coords
                    
#                     # Update game state
#                     if not self.start_moved:
#                         self.maze.layout[self.maze.start_node[0]][self.maze.start_node[1]] = ' '
#                         self.start_moved = True
                    
#                     # Handle food or bonus at the destination
#                     r, c = dest_coords
#                     if dest_coords in self.maze.foods_nodes:
#                         self.maze.foods_nodes.remove(dest_coords)
#                         self.maze.layout[r][c] = ' '
                    
#                     if dest_coords in self.maze.pies_nodes:
#                         self.maze.pies_nodes.remove(dest_coords)
#                         self.maze.layout[r][c] = ' '
#                         self.maze.power_mode_steps = 5  
#             else:
#                 # Regular movement
#                 self.move_player(action)
                
#                 # Decrease power mode steps
#                 if self.maze.power_mode_steps > 0:
#                     self.maze.power_mode_steps -= 1
            
#             # Handle events
#             for event in pygame.event.get():
#                 if event.type == pygame.QUIT:
#                     running = False
        
#         print(f"Game completed in {len(actions)} steps")
#         pygame.time.wait(1000)  
#         pygame.quit()

#     def run(self):
#         running = True
#         clock = pygame.time.Clock()

#         while running:
#             self.draw()
#             clock.tick(10)  # Limit FPS

#             for event in pygame.event.get():
#                 if event.type == pygame.QUIT:
#                     running = False
#                 elif event.type == pygame.KEYDOWN:
#                     if event.key == pygame.K_UP:
#                         self.player_pos = self.maze.teleport(self.player_pos, "UP")
#                         self.move_player("UP")
#                     elif event.key == pygame.K_DOWN:
#                         self.player_pos = self.maze.teleport(self.player_pos, "DOWN")
#                         self.move_player("DOWN")
#                     elif event.key == pygame.K_LEFT:
#                         self.player_pos = self.maze.teleport(self.player_pos, "LEFT")
#                         self.move_player("LEFT")
#                     elif event.key == pygame.K_RIGHT:
#                         self.player_pos = self.maze.teleport(self.player_pos, "RIGHT")
#                         self.move_player("RIGHT")

#         pygame.quit()
        
#     def run_from_aStar(self, path):
#         running = True
#         clock = pygame.time.Clock()
#         counter = 0

#         for move in path:
#             counter += 1
#             if not running:
#                 break  

#             self.draw()
#             clock.tick(10)

#             current_r, current_c = self.player_pos
#             next_r, next_c = move

#             if next_r < current_r:
#                 direction = "UP"
#             elif next_r > current_r:
#                 direction = "DOWN"
#             elif next_c < current_c:
#                 direction = "LEFT"
#             else:
#                 direction = "RIGHT"

#             self.player_pos = self.maze.teleport(self.player_pos, direction)
#             self.move_player(direction)            

#             for event in pygame.event.get():
#                 if event.type == pygame.QUIT:
#                     running = False
#         print("Total moves:", counter)
#         pygame.quit()

import pygame
from maze import Maze

class MazeGame:
    def __init__(self, maze_file, cell_size=30):
        pygame.init()

        # Load maze
        self.maze = Maze(maze_file)
        self.cell_size = cell_size

        # Screen size
        self.width = self.maze.cols * self.cell_size
        self.height = self.maze.rows * self.cell_size + 50  # Extra space for status bar
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("TASK 2 - PACMAN")

        # Load images
        self.images = {
            '%': pygame.image.load("sprites/wall.png"),
            '.': pygame.image.load("sprites/food.png"),
            'O': pygame.image.load("sprites/bonus.png"),
            'P': pygame.image.load("sprites/player.png"),
            'P_POWER': pygame.image.load("sprites/player.png"),  # You can create a special power mode player sprite
            ' ': pygame.image.load("sprites/empty.png"),
        }

        # Scale images
        for key in self.images:
            self.images[key] = pygame.transform.scale(self.images[key], (self.cell_size, self.cell_size))
            
            # Add a glow effect to power mode player
            if key == 'P_POWER':
                # Create a larger surface with some padding for the glow effect
                glow_surf = pygame.Surface((self.cell_size + 10, self.cell_size + 10), pygame.SRCALPHA)
                # Draw a yellow circle as the glow
                pygame.draw.circle(glow_surf, (255, 255, 0, 128), (glow_surf.get_width()//2, glow_surf.get_height()//2), self.cell_size//2 + 5)
                # Draw the player sprite in the center
                glow_surf.blit(self.images['P'], (5, 5))
                self.images[key] = glow_surf

        # Set player start position
        self.player_pos = self.maze.start_node
        self.start_moved = False
        
        # Font for status bar
        self.font = pygame.font.SysFont('Arial', 16)
        
        # Path visualization
        self.path_history = []
        self.wall_crossings = []  # Store positions where player crosses walls

    def draw(self):
        # Fill background
        self.screen.fill((0, 0, 0))
        
        # Draw maze elements
        for r in range(self.maze.rows):
            for c in range(self.maze.cols):
                x, y = c * self.cell_size, r * self.cell_size
                char = self.maze.layout[r][c]
                self.screen.blit(self.images.get(char, self.images[' ']), (x, y))
        
        # Draw path history (faint footprints)
        for pos in self.path_history:
            r, c = pos
            x, y = c * self.cell_size, r * self.cell_size
            # Draw a small circle to represent footprint
            pygame.draw.circle(self.screen, (100, 100, 255, 128), 
                              (x + self.cell_size//2, y + self.cell_size//2), 
                              self.cell_size//6)
                              
        # Highlight wall crossings in power mode
        for pos in self.wall_crossings:
            r, c = pos
            x, y = c * self.cell_size, r * self.cell_size
            # Draw a red X to show wall crossing
            pygame.draw.line(self.screen, (255, 0, 0), 
                            (x + 5, y + 5), 
                            (x + self.cell_size - 5, y + self.cell_size - 5), 3)
            pygame.draw.line(self.screen, (255, 0, 0), 
                            (x + self.cell_size - 5, y + 5), 
                            (x + 5, y + self.cell_size - 5), 3)

        # Draw player
        px, py = self.player_pos
        player_x, player_y = py * self.cell_size, px * self.cell_size
        
        # Use power mode player sprite if in power mode
        if self.maze.power_mode_steps > 0:
            # Center the larger glow image
            glow_size = self.images['P_POWER'].get_width()
            offset = (glow_size - self.cell_size) // 2
            self.screen.blit(self.images['P_POWER'], 
                             (player_x - offset, player_y - offset))
        else:
            self.screen.blit(self.images['P'], (player_x, player_y))
            
        # Draw status bar
        status_y = self.maze.rows * self.cell_size + 10
        
        # Power mode status
        power_text = f"Power Mode: {'ON' if self.maze.power_mode_steps > 0 else 'OFF'}"
        if self.maze.power_mode_steps > 0:
            power_text += f" ({self.maze.power_mode_steps} steps left)"
        power_surf = self.font.render(power_text, True, (255, 255, 0) if self.maze.power_mode_steps > 0 else (255, 255, 255))
        self.screen.blit(power_surf, (10, status_y))
        
        # Food count
        food_text = f"Food Remaining: {len(self.maze.foods_nodes)}"
        food_surf = self.font.render(food_text, True, (255, 255, 255))
        self.screen.blit(food_surf, (250, status_y))
        
        # Update display
        pygame.display.flip()

    def move_player(self, direction):
        r, c = self.player_pos
        moves = {'UP': (-1, 0), 'DOWN': (1, 0), 'LEFT': (0, -1), 'RIGHT': (0, 1)}

        if direction in moves:
            dr, dc = moves[direction]
            new_r, new_c = r + dr, c + dc

            # Check if the move would cross a wall in power mode
            is_wall_crossing = (new_r, new_c) in self.maze.walls and self.maze.power_mode_steps > 0
            
            # Move only if it's a valid position
            if self.maze.is_valid_move(new_r, new_c):
                # Add current position to path history before moving
                if self.player_pos not in self.path_history:
                    self.path_history.append(self.player_pos)
                
                # Mark wall crossing
                if is_wall_crossing:
                    self.wall_crossings.append((new_r, new_c))
                
                # Handle first move from start position
                if not self.start_moved:
                    self.maze.layout[self.maze.start_node[0]][self.maze.start_node[1]] = ' '
                    self.start_moved = True

                # Update player position
                self.player_pos = (new_r, new_c)

                # Eat food
                if self.player_pos in self.maze.foods_nodes:
                    self.maze.foods_nodes.remove(self.player_pos)
                    self.maze.layout[new_r][new_c] = ' ' 

                # Eat bonus (activate power mode)
                if self.player_pos in self.maze.pies_nodes:
                    self.maze.pies_nodes.remove(self.player_pos)
                    self.maze.layout[new_r][new_c] = ' '
                    self.maze.power_mode_steps = 5  # Activate power mode

    def run_with_actions(self, actions):
        running = True
        clock = pygame.time.Clock()
        step_count = 0
        
        while step_count < len(actions) and running:
            action = actions[step_count]
            
            # Process events before drawing
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    # Allow manual control with spacebar to pause/resume
                    if event.key == pygame.K_SPACE:
                        # Wait for another spacebar press
                        paused = True
                        while paused and running:
                            for pause_event in pygame.event.get():
                                if pause_event.type == pygame.QUIT:
                                    running = False
                                    paused = False
                                elif pause_event.type == pygame.KEYDOWN and pause_event.key == pygame.K_SPACE:
                                    paused = False
                            
                            # Continue to update the display during pause
                            self.draw()
                            pygame.display.flip()
                            clock.tick(30)
            
            if not running:
                break
            
            # Draw current state
            self.draw()
            
            # Show current action on screen
            action_text = f"Step {step_count+1}/{len(actions)}: {action}"
            action_surf = self.font.render(action_text, True, (255, 255, 255))
            self.screen.blit(action_surf, (10, self.height - 30))
            pygame.display.flip()
            
            # Handle teleportation
            if isinstance(action, str) and action.startswith("TELEPORT"):
                # Extract destination coordinates from the action string
                parts = action.split("to")
                if len(parts) == 2:
                    dest_str = parts[1].strip()
                    # Parse the coordinates - format is like "(r, c)"
                    dest_str = dest_str.strip("()")
                    dest_coords = tuple(map(int, dest_str.split(",")))
                    
                    # Add current position to path history before teleporting
                    if self.player_pos not in self.path_history:
                        self.path_history.append(self.player_pos)
                    
                    # Update player position
                    self.player_pos = dest_coords
                    
                    # Update game state
                    if not self.start_moved:
                        self.maze.layout[self.maze.start_node[0]][self.maze.start_node[1]] = ' '
                        self.start_moved = True
                    
                    # Handle food or bonus at the destination
                    r, c = dest_coords
                    if dest_coords in self.maze.foods_nodes:
                        self.maze.foods_nodes.remove(dest_coords)
                        self.maze.layout[r][c] = ' '
                    
                    if dest_coords in self.maze.pies_nodes:
                        self.maze.pies_nodes.remove(dest_coords)
                        self.maze.layout[r][c] = ' '
                        self.maze.power_mode_steps = 5  # Activate power mode
            else:
                # Regular movement
                self.move_player(action)
            
            # Decrease power mode steps after moving
            if self.maze.power_mode_steps > 0:
                self.maze.power_mode_steps -= 1
            
            # Increment step counter
            step_count += 1
            
            # Display updated state
            self.draw()
            pygame.display.flip()
            
            # Control speed
            clock.tick(30)  # Adjust for speed (lower = slower)
            
            # Check for win condition
            if len(self.maze.foods_nodes) == 0:
                win_font = pygame.font.SysFont('Arial', 36)
                win_text = win_font.render("ALL FOOD COLLECTED!", True, (0, 255, 0))
                text_rect = win_text.get_rect(center=(self.width//2, self.height//2))
                self.screen.blit(win_text, text_rect)
                pygame.display.flip()
                pygame.time.wait(3000)  # Display win message for 3 seconds
        
        print(f"Game completed in {step_count} steps")
        if running:
            pygame.time.wait(1000)  # Wait before closing
        pygame.quit()

