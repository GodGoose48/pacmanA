from maze import Maze
from mazeGame import MazeGame
from astar import AStar

def main():
    maze_file = "layout/layout2.txt" 
    
    maze = Maze(maze_file)
    astar = AStar()

    expanded, actions = astar.search(maze, maze.get_start_node(), None)
    
    print(f"Solution found!")
    # print(f"Total steps: {len(actions)}")
    # best_food, best_path, best_power_steps = astar.find_closest_food(maze, maze.get_start_node())
    # print(f"best path: {best_path}")
    
    game = MazeGame(maze_file)
    game.run_with_action(actions)
    # print(f"action when inout: {actions}")
    # game.run()


if __name__ == "__main__":
    main()