from maze import Maze
from problem import Problem

class PacmanProblem(Problem):
    def __init__(self, Maze):

        self.start_state = Maze.start_node()
        self.food = Maze.get_all_goals()
        self.walls = Maze.getWalls()
        self.costFn = lambda x: 1 # uniform cost
        self.goal = Maze.getNumFood()
        self.expanded = 0
        self.heuristicInfo = {}  # A dictionary for the heuristic to store information

    def getStartState(self):
        return self.start_state

    def isGoalState(self, Maze):
        return Maze.getNumFood() == 0

    def getSuccessors(self, state):
        """
        Given a state, returns a list of legal successors to the state.

        Each successor should be a tuple of (next_state, action, cost),
        where 'next_state' is a GameState, 'action' is a Directions
        (e.g., 'North'), and 'cost' is a number.

        Note that you must expose the legal successors using the
        'getLegalActions' method of the GameState class.
        """
        successors = []
        for action in state.getLegalActions():
            # Execute the action to get the next state
            next_state = state.generateSuccessor(0, action)
            # Check if the next state is valid (not a wall)
            if next_state.getPacmanPosition() != state.getPacmanPosition():
                successors.append((next_state, action, self.costFn(next_state)))
        self.expanded += 1
        return successors

    def getCostOfActions(self, actions):
        """
        Returns the cost of a particular sequence of actions.  If those actions
        lead to an illegal state, the cost is 999999999999
        """
        x, y = self.getStartState().getPacmanPosition()
        cost = 0
        for action in actions:
            # figure out the next state and see whether its' legal
            dx, dy = Actions.directionToVector(action)
            x, y = int(x + dx), int(y + dy)
            if self.walls[x][y]:
                return 999999999999
            cost += 1
        return cost
    
def solvePacmanProblem(problem, heuristic=None):
    """
    Uses A* search to find an optimal path for Pacman to eat all the food.

    Returns a tuple of (path, cost), where 'path' is a list of actions
    (e.g., ['North', 'East', 'West']) and 'cost' is the total cost of the path.
    """
    closed = set()
    fringe = util.PriorityQueue()
    start_state = problem.getStartState()
    start_node = (start_state, [], 0)  # (state, actions, cost)
    fringe.push(start_node, heuristic(start_state, problem) if heuristic else 0)

    while not fringe.isEmpty():
        state, actions, cost = fringe.pop()

        if problem.isGoalState(state):
            return actions, cost

        if (state.getPacmanPosition(), state.getFood().count()) in closed:
            continue

        closed.add((state.getPacmanPosition(), state.getFood().count()))

        for next_state, action, step_cost in problem.getSuccessors(state):
            new_actions = actions + [action]
            new_cost = cost + step_cost
            next_node = (next_state, new_actions, new_cost)
            fringe.push(next_node, new_cost + (heuristic(next_state, problem) if heuristic else 0))

    return None, None  # No solution found