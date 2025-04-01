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

        self.images = {
            '%': pygame.image.load("sprites/wall.png"),
            '.': pygame.image.load("sprites/food.png"),
            'O': pygame.image.load("sprites/bonus.png"),
            'P': pygame.image.load("sprites/player.png"),
            ' ': pygame.image.load("sprites/empty.png"),
        }

        # Scale images
        for key in self.images:
            self.images[key] = pygame.transform.scale(self.images[key], (self.cell_size, self.cell_size))

        # start position
        self.player_pos = self.maze.start_node
        self.start_moved = False

        self.path_history = []
        self.wall_crossings = []  

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
        # for pos in self.path_history:
        #     r, c = pos
        #     x, y = c * self.cell_size, r * self.cell_size
        #     # Draw a small circle to represent footprint
        #     pygame.draw.circle(self.screen, (100, 100, 255, 128), 
        #                       (x + self.cell_size//2, y + self.cell_size//2), 
        #                       self.cell_size//6)
                              
        # Highlight wall crossings in power mode
        # for pos in self.wall_crossings:
        #     r, c = pos
        #     x, y = c * self.cell_size, r * self.cell_size
        #     # Draw a red X to show wall crossing
        #     pygame.draw.line(self.screen, (255, 0, 0), 
        #                     (x + 5, y + 5), 
        #                     (x + self.cell_size - 5, y + self.cell_size - 5), 3)
        #     pygame.draw.line(self.screen, (255, 0, 0), 
        #                     (x + self.cell_size - 5, y + 5), 
        #                     (x + 5, y + self.cell_size - 5), 3)

        # Draw player
        px, py = self.player_pos
        player_x, player_y = py * self.cell_size, px * self.cell_size
        
        # Use power mode player sprite if in power mode
        if self.maze.power_mode_steps > 0:
            # Center the larger glow image
            glow_size = self.images['O'].get_width()
            offset = (glow_size - self.cell_size) // 2
            self.screen.blit(self.images['O'], 
                             (player_x - offset, player_y - offset))
        else:
            self.screen.blit(self.images['P'], (player_x, player_y))
            
        # Draw status bar
        status_y = self.maze.rows * self.cell_size + 10
        
        # # Power mode status
        # power_text = f"Power Mode: {'ON' if self.maze.power_mode_steps > 0 else 'OFF'}"
        # if self.maze.power_mode_steps > 0:
        #     power_text += f" ({self.maze.power_mode_steps} steps left)"
        # power_surf = self.font.render(power_text, True, (255, 255, 0) if self.maze.power_mode_steps > 0 else (255, 255, 255))
        # self.screen.blit(power_surf, (10, status_y))
        
        # # Food count
        # food_text = f"Food Remaining: {len(self.maze.foods_nodes)}"
        # food_surf = self.font.render(food_text, True, (255, 255, 255))
        # self.screen.blit(food_surf, (250, status_y))
        
        # Update display
        pygame.display.flip()

    # def draw(self):
    #     self.screen.fill((0, 0, 0))
        
    #     coord_font = pygame.font.SysFont('Arial', 8)
    
    #     for r in range(self.maze.rows):
    #         for c in range(self.maze.cols):
    #             x, y = c * self.cell_size, r * self.cell_size
    #             char = self.maze.layout[r][c]
    #             self.screen.blit(self.images.get(char, self.images[' ']), (x, y))
                
    #             if char in ['%', '.', 'O']:  
    #                 coord_text = f"({r},{c})"
    #                 coord_surf = coord_font.render(coord_text, True, (255, 255, 255))
    #                 self.screen.blit(coord_surf, (x + 2, y + 2))
        
    #     # for pos in self.path_history:
    #     #     r, c = pos
    #     #     x, y = c * self.cell_size, r * self.cell_size
        
    #     #     pygame.draw.circle(self.screen, (100, 100, 255, 128), 
    #     #                       (x + self.cell_size//2, y + self.cell_size//2), 
    #     #                       self.cell_size//6)

    #     # for pos in self.wall_crossings:
    #     #     r, c = pos
    #     #     x, y = c * self.cell_size, r * self.cell_size
    #     #     # Draw a red X to show wall crossing
    #     #     pygame.draw.line(self.screen, (255, 0, 0), 
    #     #                     (x + 5, y + 5), 
    #     #                     (x + self.cell_size - 5, y + self.cell_size - 5), 3)
    #     #     pygame.draw.line(self.screen, (255, 0, 0), 
    #     #                     (x + self.cell_size - 5, y + 5), 
    #     #                     (x + 5, y + self.cell_size - 5), 3)

    #     #     cross_text = f"({r},{c})"
    #     #     cross_surf = coord_font.render(cross_text, True, (255, 100, 100))
    #     #     self.screen.blit(cross_surf, (x + 2, y + self.cell_size - 10))
    
    #     # Draw player
    #     px, py = self.player_pos
    #     player_x, player_y = py * self.cell_size, px * self.cell_size
        
    #     if self.maze.power_mode_steps > 0:
    #         glow_size = self.images['O'].get_width()
    #         offset = (glow_size - self.cell_size) // 2
    #         self.screen.blit(self.images['O'], 
    #                          (player_x - offset, player_y - offset))
    #     else:
    #         self.screen.blit(self.images['P'], (player_x, player_y))

    #     player_text = f"Player: ({px},{py})"
    #     player_coord_surf = self.font.render(player_text, True, (255, 255, 0))
    #     self.screen.blit(player_coord_surf, (10, self.height - 50))
    #     status_y = self.maze.rows * self.cell_size + 10
        
    #     power_text = f"Power Mode: {'ON' if self.maze.power_mode_steps > 0 else 'OFF'}"
    #     if self.maze.power_mode_steps > 0:
    #         power_text += f" ({self.maze.power_mode_steps} steps left)"
    #     power_surf = self.font.render(power_text, True, (255, 255, 0) if self.maze.power_mode_steps > 0 else (255, 255, 255))
    #     self.screen.blit(power_surf, (10, status_y))

    #     food_text = f"Food Remaining: {len(self.maze.foods_nodes)}"
    #     food_surf = self.font.render(food_text, True, (255, 255, 255))
    #     self.screen.blit(food_surf, (250, status_y))

    #     pygame.display.flip()

    def move_player(self, direction):
        r, c = self.player_pos
        moves = {'UP': (-1, 0), 'DOWN': (1, 0), 'LEFT': (0, -1), 'RIGHT': (0, 1)}
        
        is_wall_crossing = False

        if direction in moves:
            dr, dc = moves[direction]
            new_r, new_c = r + dr, c + dc

            is_wall_crossing = (new_r, new_c) in self.maze.walls and self.maze.power_mode_steps > 0
            
            if self.maze.is_valid_move(new_r, new_c):
                if self.player_pos not in self.path_history:
                    self.path_history.append(self.player_pos)
                
                if is_wall_crossing:
                    self.wall_crossings.append((new_r, new_c))
                
                if not self.start_moved:
                    self.maze.layout[self.maze.start_node[0]][self.maze.start_node[1]] = ' '
                    self.start_moved = True

                self.player_pos = (new_r, new_c)

                # eat food
                if self.player_pos in self.maze.foods_nodes:
                    self.maze.foods_nodes.remove(self.player_pos)
                    self.maze.layout[new_r][new_c] = ' ' 

                # eat bonus 
                if self.player_pos in self.maze.pies_nodes:
                    self.maze.pies_nodes.remove(self.player_pos)
                    self.maze.layout[new_r][new_c] = ' '
                    self.maze.power_mode_steps = 5  
                elif self.maze.power_mode_steps > 0:
                    self.maze.power_mode_steps -= 1
                    
        # For debugging (now safe to use is_wall_crossing)
        # print(f"Position: {self.player_pos}, Power mode: {self.maze.power_mode_steps}, Wall crossing: {is_wall_crossing}")
        print

    def run(self):
        running = True
        clock = pygame.time.Clock()
        run_counter = 0

        while running:
            self.draw()
            clock.tick(10)  
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.player_pos = self.maze.teleport(self.player_pos, "UP")
                        self.move_player("UP")
                        run_counter += 1
                        print(f"Run counter: {run_counter}")
                    elif event.key == pygame.K_DOWN:
                        self.player_pos = self.maze.teleport(self.player_pos, "DOWN")
                        self.move_player("DOWN")
                        run_counter += 1
                        print(f"Run counter: {run_counter}")
                    elif event.key == pygame.K_LEFT:
                        self.player_pos = self.maze.teleport(self.player_pos, "LEFT")
                        self.move_player("LEFT")
                        run_counter += 1
                        print(f"Run counter: {run_counter}")
                    elif event.key == pygame.K_RIGHT:
                        self.player_pos = self.maze.teleport(self.player_pos, "RIGHT")
                        self.move_player("RIGHT")
                        run_counter += 1
                        print(f"Run counter: {run_counter}")
            
        pygame.quit()
      
    def run_with_action(self, action):
        running = True
        run_counter = 0

        for event in action:
            if not running:
                break  

            for quit in pygame.event.get():
                if quit.type == pygame.QUIT:
                    running = False
                if len(self.maze.foods_nodes) == 0:
                    running = False
            self.draw()
            pygame.display.update()  
            pygame.time.delay(100)  

            if event == "UP":
                self.player_pos = self.maze.teleport(self.player_pos, "UP")
                self.move_player("UP")
            elif event == "DOWN":
                self.player_pos = self.maze.teleport(self.player_pos, "DOWN")
                self.move_player("DOWN")
            elif event == "LEFT":
                self.player_pos = self.maze.teleport(self.player_pos, "LEFT")
                self.move_player("LEFT")
            elif event == "RIGHT":
                self.player_pos = self.maze.teleport(self.player_pos, "RIGHT")
                self.move_player("RIGHT")

            run_counter += 1
            # print(f"Run counter: {run_counter}")
            
        if len(self.maze.foods_nodes) == 0:
                pygame.display.flip()
                pygame.time.wait(1500)
        
        print(f"Game completed in {run_counter} steps")

        pygame.quit()