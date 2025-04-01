# from maze import Maze
# from astar import AStar
# from mazeGame import MazeGame

# def main():
#     maze_file = "layout.txt"  # Đường dẫn đến file bản đồ
#     maze = Maze(maze_file)
#     astar = AStar()

#     # Tìm đường đi từ Pacman đến tất cả thức ăn
#     start = maze.get_start_node()
#     goals = maze.get_all_goals()

#     current_position = start
#     final_path = []

#     for goal in goals:
#         expanded, path = astar.search(maze, current_position, goal)
#         if path:
#             final_path.extend(path[1:])  # Thêm đường đi (bỏ vị trí bắt đầu)
#             current_position = goal
#         else:
#             print("Không tìm thấy đường đến", goal)
#             return

#     # Khởi động game và cho Pacman tự chạy theo đường tìm được
#     game = MazeGame(maze_file)
#     game.run_from_aStar(final_path)

# if __name__ == "__main__":
#     main()

# main.py - Run the Pacman solution

# from maze import Maze
# from mazeGame import MazeGame
# from astar import AStar

# def main():
#     # Set the path to your maze file
#     maze_file = "layout.txt"
    
#     # Initialize maze and A* search
#     maze = Maze(maze_file)
#     astar = AStar()
    
#     print("Calculating optimal path to eat all food...")
    
#     # Run A* to find path to all food points
#     expanded, actions = astar.search(maze, maze.get_start_node(), None)
    
#     # Print solution information
#     print(f"Solution found!")
#     print(f"Total steps: {len(actions)}")
#     print("\nMovement sequence:")
#     for i, action in enumerate(actions):
#         print(f"Step {i+1}: {action}")
    
#     print("\nRunning visualization...")
    
#     # Initialize game and run with actions
#     game = MazeGame(maze_file)
#     game.run_with_actions(actions)

# if __name__ == "__main__":
#     main()


# main.py - Run the Pacman solution

import os
import pygame
from maze import Maze
from mazeGame import MazeGame
from astar import AStar

def main():
    # Set the path to your maze file
    maze_file = "layout.txt"  # Update this to your actual file path
    
    # Check if the file exists
    if not os.path.exists(maze_file):
        print(f"Error: Maze file '{maze_file}' not found.")
        return
    
    # Initialize maze and A* search
    maze = Maze(maze_file)
    astar = AStar()
    
    print("Calculating optimal path to eat all food...")
    
    # Run A* to find path to all food points
    expanded, actions = astar.search(maze, maze.get_start_node(), None)
    
    # Print solution information
    print(f"Solution found!")
    print(f"Total steps: {len(actions)}")
    print("\nMovement sequence:")
    for i, action in enumerate(actions):
        print(f"Step {i+1}: {action}")
    
    
    game = MazeGame(maze_file)
    game.run_with_actions(actions)


if __name__ == "__main__":
    main()