import pygame
from maze import Maze

class MazeGame:
    def __init__(self, maze_file, cell_size=30):
        pygame.init()

        # Load maze
        self.maze = Maze(maze_file)
        self.cell_size = cell_size

        # screen size
        self.width = self.maze.cols * self.cell_size
        self.height = self.maze.rows * self.cell_size
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("TASK 2 - PACMAN")

        # Load images
        self.images = {
            '%': pygame.image.load("sprites/wall.png"),
            '.': pygame.image.load("sprites/food.png"),
            'O': pygame.image.load("sprites/bonus.png"),
            'P': pygame.image.load("sprites/player.png"),
            ' ': pygame.image.load("sprites/empty.png"),
            # 'T': pygame.image.load("sprites/teleport.png") 
        }

        for key in self.images:
            self.images[key] = pygame.transform.scale(self.images[key], (self.cell_size, self.cell_size))

        # Set player start position
        self.player_pos = self.maze.start_node
        self.start_moved = False  

    def draw(self):
        self.screen.fill((0, 0, 0)) 

        for r in range(self.maze.rows):
            for c in range(self.maze.cols):
                x, y = c * self.cell_size, r * self.cell_size
                char = self.maze.layout[r][c]

                # if (r, c) in self.maze.corners:
                #     char = 'T'

                self.screen.blit(self.images.get(char, self.images[' ']), (x, y))

        # Draw player on top
        px, py = self.player_pos
        self.screen.blit(self.images['P'], (py * self.cell_size, px * self.cell_size))

        pygame.display.flip()

    def move_player(self, direction):
        r, c = self.player_pos
        moves = {'UP': (-1, 0), 'DOWN': (1, 0), 'LEFT': (0, -1), 'RIGHT': (0, 1)}

        if direction in moves:
            new_r, new_c = r + moves[direction][0], c + moves[direction][1]

            # Move only if it's a valid position
            if self.maze.is_valid_move(new_r, new_c):
                if not self.start_moved:
                    self.maze.layout[self.maze.start_node[0]][self.maze.start_node[1]] = ' '
                    self.start_moved = True

                self.player_pos = (new_r, new_c)

                # Eat food (replace '.' with ' ')
                if self.player_pos in self.maze.foods_nodes:
                    self.maze.foods_nodes.remove(self.player_pos)
                    self.maze.layout[new_r][new_c] = ' ' 

                # Eat bonus (replace 'O' with ' ')
                if self.player_pos in self.maze.pies_nodes:
                    self.maze.pies_nodes.remove(self.player_pos)
                    self.maze.layout[new_r][new_c] = ' '  

    def run(self):
        running = True
        clock = pygame.time.Clock()

        while running:
            self.draw()
            clock.tick(10)  # Limit FPS

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.player_pos = self.maze.teleport(self.player_pos, "UP")
                        self.move_player("UP")
                    elif event.key == pygame.K_DOWN:
                        self.player_pos = self.maze.teleport(self.player_pos, "DOWN")
                        self.move_player("DOWN")
                    elif event.key == pygame.K_LEFT:
                        self.player_pos = self.maze.teleport(self.player_pos, "LEFT")
                        self.move_player("LEFT")
                    elif event.key == pygame.K_RIGHT:
                        self.player_pos = self.maze.teleport(self.player_pos, "RIGHT")
                        self.move_player("RIGHT")

        pygame.quit()
        
    def run_from_aStar(self, path):
        running = True
        clock = pygame.time.Clock()
        counter = 0

        for move in path:
            counter += 1
            if not running:
                break  

            self.draw()
            clock.tick(20)

            current_r, current_c = self.player_pos
            next_r, next_c = move

            if next_r < current_r:
                direction = "UP"
            elif next_r > current_r:
                direction = "DOWN"
            elif next_c < current_c:
                direction = "LEFT"
            else:
                direction = "RIGHT"

            self.player_pos = self.maze.teleport(self.player_pos, direction)
            self.move_player(direction)            

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
        print("Total moves:", counter)
        pygame.quit()



