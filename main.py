from maze import Maze
from astar import AStar
from mazeGame import MazeGame

def main():
    maze_file = "layout.txt"  # Đường dẫn đến file bản đồ
    maze = Maze(maze_file)
    astar = AStar()

    # Tìm đường đi từ Pacman đến tất cả thức ăn
    start = maze.get_start_node()
    goals = maze.get_all_goals()

    current_position = start
    final_path = []

    for goal in goals:
        expanded, path = astar.search(maze, current_position, goal)
        if path:
            final_path.extend(path[1:])  # Thêm đường đi (bỏ vị trí bắt đầu)
            current_position = goal
        else:
            print("Không tìm thấy đường đến", goal)
            return

    # Khởi động game và cho Pacman tự chạy theo đường tìm được
    game = MazeGame(maze_file)
    game.run_from_aStar(final_path)

if __name__ == "__main__":
    main()
